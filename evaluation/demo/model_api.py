import requests
def generate(prompt, temperature):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "gemma4:e4b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "top_p": 0.9,
            "top_k": 40,
            "repeat_penalty": 1.1,
            "num_predict": 800,
        }
    }
    res = requests.post(url, json=data)
    return res.json()["response"]

if __name__ == "__main__":
    prompt = "What is the meaning of life?"
    response = generate(prompt, temperature=0.7)
    print(response)
