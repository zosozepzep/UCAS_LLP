import requests
def generate(prompt, temperature):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "gemma4:e2b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "top_p": 0.9,
            "top_k": 40,
            "repeat_penalty": 1.1,
            "num_predict": 1000,
        }
    }
    res = requests.post(url, json=data)
    return res.json()["response"]
#example
#print(generate("what is AI?", temperature=0.7))
