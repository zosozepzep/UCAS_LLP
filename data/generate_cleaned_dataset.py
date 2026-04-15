import json
import re
import random

# 生成原始数据
def generate_raw_data(num_records=1000):
    raw_data = []
    
    # 定义一些可能的提示类型
    prompt_types = ["question", "command", "request", "instruction", "query"]
    
    # 定义一些常见的提示内容
    prompt_contents = [
        "如何使用Python进行数据分析",
        "解释什么是机器学习",
        "编写一个计算斐波那契数列的函数",
        "如何提高代码的可读性",
        "解释什么是神经网络",
        "如何使用Git进行版本控制",
        "编写一个简单的Web服务器",
        "解释什么是API",
        "如何优化数据库查询",
        "解释什么是云计算"
    ]
    
    # 生成数据
    for i in range(num_records):
        # 生成原始提示，可能包含噪声
        base_content = random.choice(prompt_contents)
        noise = random.choice(["", "  ", "\n", "\t", "   ", "!!", "???"])
        raw_prompt = noise + base_content + noise
        
        # 生成一些变体
        if random.random() > 0.5:
            raw_prompt = raw_prompt.upper()
        elif random.random() > 0.5:
            raw_prompt = raw_prompt.lower()
        
        # 生成标签
        label = random.choice(prompt_types)
        
        # 生成ID
        record_id = f"D{i+1}"
        
        raw_data.append({
            "id": record_id,
            "raw_prompt": raw_prompt,
            "label": label
        })
    
    return raw_data

# 清洗数据
def clean_data(raw_data):
    cleaned_data = []
    
    for record in raw_data:
        # 去除首尾空白字符
        cleaned_prompt = record["raw_prompt"].strip()
        
        # 统一转换为小写
        cleaned_prompt = cleaned_prompt.lower()
        
        # 去除多余的标点符号
        cleaned_prompt = re.sub(r'[!]+', '!', cleaned_prompt)
        cleaned_prompt = re.sub(r'[?]+', '?', cleaned_prompt)
        
        # 去除多余的空格
        cleaned_prompt = re.sub(r'\s+', ' ', cleaned_prompt)
        
        cleaned_data.append({
            "id": record["id"],
            "raw_prompt": record["raw_prompt"],
            "cleaned_prompt": cleaned_prompt,
            "label": record["label"]
        })
    
    return cleaned_data

# 主函数
def main():
    # 生成原始数据
    raw_data = generate_raw_data(1000)
    
    # 清洗数据
    cleaned_data = clean_data(raw_data)
    
    # 保存为JSON文件
    output_file = "cleaned_dataset.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
    
    print(f"已生成{len(cleaned_data)}条清洗和标注后的数据，保存至{output_file}")
    
    # 显示前5条数据作为示例
    print("\n前5条数据示例：")
    for i, record in enumerate(cleaned_data[:5]):
        print(f"\n示例{i+1}:")
        print(f"ID: {record['id']}")
        print(f"原始提示: '{record['raw_prompt']}'")
        print(f"清洗后提示: '{record['cleaned_prompt']}'")
        print(f"标签: {record['label']}")

if __name__ == "__main__":
    main()