import json
from model_api import generate
from temp_exp_results import save_results

def multi_experiment():
    with open("data/test_cases.json", "r", encoding="utf-8") as f:
        test_cases = json.load(f)
    temperatures = [0.3, 0.7, 1.2]
    results = []
    for case in test_cases:
        prompt = case["input"]
        for t in temperatures:
            output = generate(prompt, temperature=t)
            results.append({
                "prompt": prompt,
                "temperature": t,
                "output": output
            })
    return results
if __name__ == "__main__":
    results = multi_experiment()
    save_results(results, filepath="data/multi_exp_results.json")
    print("多温度多prompt实验完成，结果已保存到data/multi_exp_results.json")