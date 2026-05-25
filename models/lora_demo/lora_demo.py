import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    pipeline
)
from datasets import load_dataset
from peft import LoraConfig, get_peft_model

# ========= 1.设备 =========
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device:", device)

# ========= 2.模型 =========
model_name = "sshleifer/tiny-gpt2"  # 小型GPT-2模型，适合演示

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
model.gradient_checkpointing_enable()
# ========= 3.LoRA 配置 =========
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["c_attn"],  # GPT2关键层
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# ========= 4.数据 =========
dataset = load_dataset("wikitext", "wikitext-2-raw-v1")

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

# 数据量控制
train_dataset = tokenized["train"].select(range(5000))

training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=1,
    logging_steps=20,
    save_steps=200,
    fp16=True,  # GPU加速
    gradient_accumulation_steps=4,
    report_to="none"
)

# ========= 5.训练 =========
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)
# ========= 6.开始训练 =========
trainer.train()

# ========= 7.保存LoRA =========
model.save_pretrained("./lora_adapter")

# ========= 8.推理测试 =========
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)

print("\n=== Inference Test ===")
result = pipe("Machine learning is", max_length=256)
print(result[0]["generated_text"])
print("LoRA training complete and saved.")