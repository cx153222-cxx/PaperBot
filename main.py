import os
from arxiv_fetch import get_arxiv_papers
from summarizer import summarize
from feishu import send_feishu

# 读取环境变量 ID 作为日报标题，如果没有则默认叫 "cs.IR"
ID = os.getenv("ID", "cs.IR")

def build_report():
    papers = get_arxiv_papers()
    report = f"📚 Arxiv Daily - {ID}\n\n"
    
    for i, paper in enumerate(papers):
        # 现在同时把标题和摘要传给大模型
        result = summarize(paper["title"], paper["summary"])
        
        # 拼接最终的文本
        report += f"{i+1}. {paper['title']}\n"
        report += f"{result}\n"  # 直接贴上大模型返回的结构化文本（含中文标题和总结）
        report += "链接:\n"
        report += f"{paper['url']}\n"
        report += "----------------------\n\n"

    return report

if __name__ == "__main__":
    report = build_report()
    print(report)
    send_feishu(report)
