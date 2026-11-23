from tools.news_search import search_recent_news

articles = search_recent_news("Latest artificial intelligence news")

for article in articles:
    print("\nTITLE:", article["title"])
    print("SOURCE:", article["source"])
    print("DATE:", article["published"])
    print("URL:", article["url"])
    print("CONTENT:", article["content"][:500] if article["content"] else None)
    print("SUMMARY:", article["summary"])