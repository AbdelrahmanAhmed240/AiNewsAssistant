from .news_search import search_recent_news

def news_by_location(location: str):
    """
    Search for the latest news about events and developments
    in a specific geographical location.

    Use this tool when the user asks about news related to a
    country, city, region, or geographical area.
    """
    if not location or not location.strip():
        return "Please provide a valid location."

    query = f"Latest news about events and developments in {location.strip()}"

    return search_recent_news(query)