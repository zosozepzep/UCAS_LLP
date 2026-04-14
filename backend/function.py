import requests
import json

def generate(prompt, params):#调用接口生成文本
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "gemma4:e4b",
        "prompt": prompt,
        "stream": False,
        "temperature": params["temperature"], 
        "top_p": params["top_p"],
        "top_k": params["top_k"],
        "repeat_penalty": params["repeat_penalty"],
        "num_predict": params["num_predict"]
    }
    res = requests.post(url, json=data)
    result = res.json()
    if "response" in result:
        return result["response"]
    elif "error" in result:
        print("接口报错：", result["error"])
        return None
    else:
        print("未知返回：", result)
        return None

def get_valid_param(prompt, type_, allowed=None, min_=None, max_=None):#获得合法输入，并且可以指定类型、范围和允许的值
    while True:
        try:
            x = type_(input(prompt))
            if allowed and x not in allowed:
                print(f"请输入 {allowed}")
                continue
            if min_ is not None and x < min_:
                print(f"不能小于 {min_}")
                continue
            if max_ is not None and x > max_:
                print(f"不能大于 {max_}")
                continue
            return x
        except ValueError:
            print(f"请输入 {type_.__name__} 类型")

def get_parameters():#获取参数,并且可以指定参数的类型、范围和允许的值
    params = {}
    params["temperature"] = get_valid_param(
        "temperature (0~2): ",
        float,
        min_=0,
        max_=2
    )

    params["top_p"] = get_valid_param(
        "top_p (0~1): ",
        float,
        min_=0,
        max_=1
    )
    params["top_k"] = get_valid_param(
        "top_k (integer): ",
        int,
        allowed = [20, 40, 60, 80, 100]
    )
    params["repeat_penalty"] = get_valid_param(
        "repeat_penalty (0.8~1.2): ",
        float,
        min_=0.8,
        max_=1.2
    )
    params["num_predict"] = get_valid_param(
        "num_predict (1~2048): ",
        int,
        min_=1,
        max_=2048
    )
    return params

def load_experiments(filepath):#从json文件加载实验配置
    with open(filepath, "r", encoding="utf-8") as exp_file:
        return json.load(exp_file)

def run_experiments(filepath):#运行实验，加载实验配置，调用接口生成文本，并保存结果
    experiments = load_experiments(filepath)
    results = []
    for exp in experiments:
        print(f"Running: {exp['name']}")
        output = generate(
            exp["prompt"],
            exp["params"]
        )
        results.append({
            "name": exp["name"],
            "prompt": exp["prompt"],
            "params": exp["params"],
            "output": output
        })
    return results

def save_results(results, filepath):#保存结果到json文件
    with open(filepath, "w", encoding="utf-8") as result_file:
        json.dump(results, result_file, indent=2, ensure_ascii=False)
