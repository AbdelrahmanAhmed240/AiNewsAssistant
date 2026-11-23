import trafilatura


def extract_article_content(url: str):
    """Extract and clean the main article text."""

    try:
        downloaded = trafilatura.fetch_url(url)

        if not downloaded:
            return None

        content = trafilatura.extract(
            downloaded,
            include_comments=False,
            include_tables=False,
            favor_precision=True
        )

        return content.strip() if content else None

    except Exception as e:
        print(f"Article extraction failed: {e}")
        return None