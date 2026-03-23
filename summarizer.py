import requests
import os

# 获取我们在 GitHub Secrets 中新配置的环境变量
API_KEY = os.getenv("API_KEY")

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
            {"role": "user", "content": f"""
             请将以下英文论文摘要提炼为适合在工作群内阅读的中文快讯。要求：\n
             1. 语言直白凝练，不要使用过于生涩的长句。\n
             2. 直接点明这篇论文的最大创新点和应用价值。\n
             3. 总字数严格控制在 200 字以内，分两到三句话输出。\n\n
             摘要原文：\n{text}"""
            }
        ]
    }

    r = requests.post(url, headers=headers, json=payload)
    
    # 【新增代码】检查响应状态，如果不是成功返回，打印出详细错误
    if r.status_code != 200:
        print(f"请求智谱 API 失败！状态码: {r.status_code}")
        print(f"错误详情: {r.text}")
        return f"摘要生成失败 (API Error: {r.status_code})"
    
    # 尝试解析，如果仍然没有 choices 字段，也打印出实际内容
    try:
        return r.json()["choices"][0]["message"]["content"]
    except KeyError:
        print(f"解析结果失败，API 实际返回了: {r.text}")
        return "摘要格式解析失败"
