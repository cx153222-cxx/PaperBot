from arxiv_fetch import get_arxiv_papers
from summarizer import summarize
from feishu import send_feishu

def build_report():
    papers = get_arxiv_papers()
    report = "📚 Arxiv Daily - cs.IR\n\n"
    for i, paper in enumerate(papers):
        summary = summarize(paper["summary"])
        # 使用 \n 进行换行，这样代码可以保持整齐的缩进，输出也不会有前置空格
        report += f"{i+1}. {paper['title']}\n"
        report += "总结:\n"
        report += f"{summary}\n"
        report += "链接:\n"
        report += f"{paper['url']}\n"
        report += "-----------------\n\n"

    return report


if __name__ == "__main__":
    report = build_report()
    print(report)
    send_feishu(report)
