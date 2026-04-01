import arxiv
import time

def get_arxiv_papers(query="cs.IR", limit=5):

    search = arxiv.Search(
        query=query,
        max_results=limit,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []

    try:
        for result in search.results():
            papers.append({
                "title": result.title,
                "summary": result.summary,
                "url": result.entry_id
            })

            time.sleep(1)  # 防止限流

    except Exception as e:
        print("arxiv error:", e)

    return papers
