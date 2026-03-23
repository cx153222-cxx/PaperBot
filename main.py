from arxiv_fetch import get_arxiv_papers
from summarizer import summarize
from feishu import send_feishu

def build_report():
    papers = get_arxiv_papers()
    report = "📚 Arxiv Daily - cs.IR\n\n"
    for i, paper in enumerate(papers):
        summary = summarize(paper["summary"])
        report += f"""
{i+1}. {paper["title"]} 
总结:
{summary}
链接:
{paper["url"]}
-----------------
"""

    return report


if __name__ == "__main__":
    report = build_report()
    print(report)
    send_feishu(report)
