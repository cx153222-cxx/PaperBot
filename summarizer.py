import requests
import os

# 获取环境变量
API_KEY = os.getenv("API_KEY")

# 修改函数：现在需要同时传入英文标题 (title) 和英文摘要 (abstract)
def summarize(title, abstract):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 更新 Prompt，增加翻译标题的要求和对应的输出格式
    prompt = f"""作为一位资深计算机科学研究员，请阅读以下英文论文的标题和摘要，并严格按照规定的格式，提炼出一份高质量的中文学术快讯。

【内容要求】
1. 准确、专业地翻译论文标题。
2. 语言需高度精炼、专业直白，拒绝废话。
3. 必须精准捕捉模型、算法或系统的具体细节。
4. 突出与传统基线(Baseline)或以往方法的差异。
5. 总字数严格控制在 300 字以内。

【严格输出格式】
🏷️ 中文标题：[此处输出论文标题的专业中文翻译]
📌 主要内容：[用一句话概括论文研究的特定场景或试图解决的核心痛点]
💡 核心创新：[用一到两句话具体说明提出的新模型架构、算法机制或理论框架]
🚀 优势与突破：[明确对比以往方案，指出该创新在性能、效率、成本或机制上带来的颠覆性区别和具体优势]

英文标题：
{title}

摘要原文：
{abstract}"""

    payload = {
        "model": "glm-4-flash",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post(url, headers=headers, json=payload)
    
    if r.status_code != 200:
        print(f"请求智谱 API 失败！状态码: {r.status_code}, 返回: {r.text}")
        return f"摘要生成失败 (API Error: {r.status_code})"
    
    try:
        return r.json()["choices"][0]["message"]["content"]
    except KeyError:
        return "摘要格式解析失败"
