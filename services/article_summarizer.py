import json
from config import get_llm

llm = None

def get_summarizer_llm():
    global llm

    if llm is None:
        llm = get_llm(temperature=0, max_tokens=1024)

    return llm

def summarize_article(content: str):
    """Generate an AI summary and key points from an article."""

    if not content or len(content.strip()) < 500:
        return None
    prompt = """
You are a professional news summarization assistant.
Analyze the following news article and return ONLY valid JSON:
{
    "short_summary": "One concise paragraph of approximately 80-100 words.",
    "key_points": [
        "First important point",
        "Second important point",
        "Third important point"
    ]
}
Rules:
- Use only information from the article.
- Do not invent facts or external information.
- Preserve important names, dates, and numbers.
- Include 3 to 5 key points.
- Do not use Markdown code fences.
ARTICLE:
""" + content

    try:
        response = get_summarizer_llm().complete(prompt)
        return json.loads(response.text.strip())

    except json.JSONDecodeError as e:
        print(f"Invalid summary JSON: {e}")
        return None

    except Exception as e:
        print(f"Article summarization failed: {e}")
        return None