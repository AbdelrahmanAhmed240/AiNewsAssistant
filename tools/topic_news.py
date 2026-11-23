from .news_search import search_recent_news

def news_by_topics(topic: str):
    """
    Search for the latest news related to a specific topic.

    Use this tool when the user wants to explore news about a subject,
    industry, field, or particular area of interest.
    """
    if not topic or not topic.strip():
        return "Please provide a valid news topic."

    query = f"Latest news about {topic.strip()}"

    return search_recent_news(query)