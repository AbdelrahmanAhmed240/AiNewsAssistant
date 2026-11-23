
import requests
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

GOOGLE_NEWS_URL = "https://news.google.com/rss/search"


def fetch_rss(query, limit=15):
    """Fetch RSS items from Google News."""
    response = requests.get(
        GOOGLE_NEWS_URL,
        params={
            "q": query,
            "hl": "en-US",
            "gl": "US",
            "ceid": "US:en"
        },
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )
    response.raise_for_status()
    return ET.fromstring(response.content).findall(".//item")[:limit]


def get_article_metadata(item):
    """Extract basic information without downloading the article."""
    return {
        "title": item.findtext("title"),
        "url": item.findtext("link"),
        "source": (
            item.find("source").text
            if item.find("source") is not None else "News"
        ),
        "published": item.findtext("pubDate")
    }


def fetch_latest_headlines(query="latest world news", limit=15):
    """Fetch headlines only; no article extraction or AI summarization."""
    try:
        return [get_article_metadata(item) for item in fetch_rss(query, limit)]
    except Exception as e:
        print(f"Headline fetching failed: {e}")
        return []


def process_article(item):
    """Decode, extract, and summarize one article."""
    from gnews_decoder import decode
    from services.article_extractor import extract_article_content
    from services.article_summarizer import summarize_article

    article = get_article_metadata(item)
    google_url = article["url"]

    try:
        publisher_url = decode(google_url)

        if publisher_url:
            article["url"] = publisher_url
            content = extract_article_content(publisher_url)
            article["content"] = content
            article["summary"] = (
                summarize_article(content) if content else None
            )
        else:
            article.update(content=None, summary=None)

    except Exception as e:
        print(f"Article processing failed: {e}")
        article.update(content=None, summary=None)

    return article


def search_recent_news(query: str):
    """Search, extract, and summarize up to three news articles."""
    if not query or not query.strip():
        return []

    try:
        items = fetch_rss(query.strip(), limit=3)

        # Process articles concurrently instead of one by one.
        with ThreadPoolExecutor(max_workers=3) as executor:
            articles = list(executor.map(process_article, items))

        return articles

    except requests.RequestException as e:
        print(f"Google News search failed: {e}")
        return []

    except ET.ParseError as e:
        print(f"Invalid RSS response: {e}")
        return []

    except Exception as e:
        print(f"News search failed: {e}")
        return []