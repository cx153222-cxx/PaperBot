import arxiv
import os

# 优先读取环境变量 ARXIV_QUERY，如果没有设置，则默认搜索 "cs.IR"
CURRENT_QUERY = os.getenv("ARXIV_QUERY", "cs.IR")

def get_arxiv_papers(query=CURRENT_QUERY, limit=5):
    search = arxiv.Search(
        query=query,
        max_results=limit,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []

    for result in search.results():
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "url": result.entry_id
        })

    return papers
