import requests
import os

# 获取我们在 GitHub Secrets 中新配置的环境变量
ZHIPU_API_KEY = os.getenv("API_KEY")

def summarize(text):
    # 智谱的 API 端点
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "glm-4-flash", # 使用免费的模型
        "messages": [
            {"role": "user", "content": f"请用中文简练地总结这篇论文摘要:\n{text}"}
        ]
    }

    r = requests.post(url, headers=headers, json=payload)
    
    # 解析并返回结果
    return r.json()["choices"][0]["message"]["content"]
