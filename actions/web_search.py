import webbrowser
from urllib.parse import quote_plus


def web_search(query: str):
    """Open a browser search for the given query using DuckDuckGo."""
    query = query or ''
    print(f"[ACTION] Searching the web for: {query}")
    url = f"https://duckduckgo.com/?q={quote_plus(query)}"
    webbrowser.open(url)
    print(f"[ACTION] Opened browser to: {url}")
    return {"query": query, "url": url}
