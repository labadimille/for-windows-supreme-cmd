def web_search(query: str):
    """Stub: perform a fake web search and print top result."""
    query = query or ''
    print(f"[ACTION] Searching the web for: {query}")
    # Fake result
    print(f"[ACTION] Top result: 'Result for {query}'")
    return {"query": query, "top_result": f"Result for {query}"}
