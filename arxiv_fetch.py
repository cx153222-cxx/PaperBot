import arxiv

def get_arxiv_papers(query="cs.IR", limit=5):
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
