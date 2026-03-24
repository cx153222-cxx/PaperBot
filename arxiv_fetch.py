import arxiv

# qu = '(cat:cs.NE OR cat:math.OC OR cat:cs.LG) AND (all:"surrogate-assisted" OR all:"Kriging" OR all:"black-box optimization")'
CURRENT_QUERY = os.getenv("ARXIV_QUERY", "cs.IR")

def get_arxiv_papers(query=qu, limit=7):
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
