import json
from model_api import generate
def run_temperature_experiment(prompt):
    temperatures = [0.3, 0.7, 1.2]
    results = []
    for t in temperatures:
        output = generate(prompt, temperature=t)
        results.append({
            "prompt": prompt,
            "temperature": t,
            "output": output
        })
    return results

def save_results(results, filepath):
    with open(filepath, "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=2, ensure_ascii=False)
#示例
if __name__ == "__main__":
    prompt = "Explain why AI is useful"
    results = run_temperature_experiment(prompt)
    save_results(results, filepath="data/results.json")
    print("实验完成，结果已保存到data/results.json")