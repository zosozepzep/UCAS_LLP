from model_api import generate
def run_experiment(prompt):
    temps = [0.3, 0.7, 1.0]
    results = {}
    for temp in temps:
        response = generate(prompt, temperature=temp)
        results[temp] = response
    return results
# Example
experiment_results = run_experiment("What is the meaning of life?")
for temp, result in experiment_results.items():
    print(f"\n----------------- Temperature: {temp} -----------------")
    print(result)
