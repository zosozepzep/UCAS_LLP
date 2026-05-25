import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    pipeline
)
from datasets import Dataset
from peft import LoraConfig, get_peft_model

# ========= 1. 设备 =========
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device:", device)

# ========= 2. 模型 =========
model_name = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

# 显存优化（5070推荐）
model.gradient_checkpointing_enable()

# ========= 3. LoRA =========
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["c_attn"],  # GPT2结构
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# ========= 4. 加载本地数据 =========
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

pairs = []
for i in range(len(lines) - 1):
    if lines[i].startswith("You:") and lines[i+1].startswith("Me:"):
        pair = lines[i].strip() + "\n" + lines[i+1].strip()
        pairs.append(pair)

dataset = Dataset.from_dict({"text": pairs})

# ========= 5. tokenize =========
def tokenize_function(examples):
    tokenized = tokenizer(
        examples["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

tokenized = dataset.map(tokenize_function, batched=True)
train_dataset = tokenized

# ========= 6. 训练参数 =========
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=5,
    logging_steps=10,
    fp16=True,
    report_to="none"
)

# ========= 7. Trainer =========
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

# ========= 8. 开始训练 =========
trainer.train()

# ========= 9. 保存 LoRA =========
model.save_pretrained("./lora_adapter_chat")

# ========= 10. model_generate =========

# ========= 11. 单轮测试 =========
print("\n=== Test ===")

prompt = "You: Hello\nMe:"

inputs = tokenizer(prompt, return_tensors="pt").to(device)

outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.2,
    pad_token_id=tokenizer.eos_token_id
)

output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

response = output_text.split("Me:")[-1].split("You:")[0].strip()

print("Me:", response)

# ========= 12. 多轮对话 =========
print("\n=== Chat Mode (type 'exit' to quit) ===")

history = ""

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    prompt = history + f"You: {user_input}\nMe:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.eos_token_id
    )

    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # 提取回答
    response = output_text.split("Me:")[-1].split("You:")[0].strip()

    print("Me:", response)

    # 保存上下文
    history += f"You: {user_input}\nMe: {response}\n"