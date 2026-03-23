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
        "model": "glm-4-flash", 
        "messages": [
            {"role": "user", "content": f"""
            作为一位资深计算机科学研究员，请阅读以下英文论文摘要，并严格按照规定的格式，提炼出一份高质量的中文学术快讯。
            
            【内容要求】
            1. 语言需高度精炼、专业直白，拒绝废话。
            2. 必须精准捕捉模型、算法或系统的具体细节。
            3. 突出与传统基线(Baseline)或以往方法的差异。
            4. 总字数严格控制在 250 字以内。
            
            【严格输出格式】
            📌 主要内容：[用一句话概括论文研究的特定场景或试图解决的核心痛点]
            💡 核心创新：[用一到两句话具体说明提出的新模型架构、算法机制或理论框架]
            🚀 优势与突破：[明确对比以往方案，指出该创新在性能、效率、成本或机制上带来的颠覆性区别和具体优势]
            
            摘要原文：
            {text}"""
            }
        ]
    }

    r = requests.post(url, headers=headers, json=payload)
    return r.json()["choices"][0]["message"]["content"]
