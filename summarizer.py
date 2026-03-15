import requests
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def summarize(text):

    url = "https://api.deepseek.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": f"请用3句话总结这篇论文:\n{text}"}
        ]
    }

    r = requests.post(url, headers=headers, json=payload)

    return r.json()["choices"][0]["message"]["content"]