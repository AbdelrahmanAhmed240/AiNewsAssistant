from .news_search import search_recent_news

def live_news_search(query: str):
    """
    Search for the latest news using a natural-language query or question.

    Use this tool when the user asks about current events, breaking news,
    or wants to search for news using a specific question.
    """
    if not query or not query.strip():
        return "Please provide a valid news query."

    return search_recent_news(query.strip())