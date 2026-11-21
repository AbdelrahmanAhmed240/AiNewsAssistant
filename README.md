# AI News Assistant 📰

An AI-powered news assistant that helps users discover and understand the latest news from around the world.

Users can search for current news using natural-language questions, explore news by specific topics, or find news related to a particular country, city, or region. The agent selects the appropriate search tool and presents relevant results with summaries and original source links.

## 1. Use Case

The application is designed for users who want to stay updated on current events and explore news from different subjects and locations.

Users can ask questions such as:

- What's happening in France right now?
- Show me the latest AI news.
- What are the latest developments in Egypt?
- Find recent news about football.

The agent understands the request, searches for relevant news, and summarizes the retrieved information.

## 2. LLM & Provider

- **Provider:** GroqCloud
- **Model:** GPT-OSS 120B
- **Model ID:** `openai/gpt-oss-120b`

**What they do:**

- **GroqCloud:** Provides API access to run the language model.
- **GPT-OSS 120B:** Understands user requests, selects tools, and summarizes news.

## 3. Agent Tools

The agent has access to three main tools.

**Tool 1: `live_news_search`**

- **Description:** Searches for current news using natural-language queries or questions.
- **Input:** `query` (string).
- **Output:** Relevant news articles and search results.

**Tool 2: `news_by_topics`**

- **Description:** Searches for recent news about specific subjects, such as politics, technology, sports, and business.
- **Input:** `topic` (string).
- **Output:** News articles related to the requested topic.

**Tool 3: `news_by_location`**

- **Description:** Searches for news related to a specific country, city, or geographical region.
- **Input:** `location` (string).
- **Output:** News articles related to the requested location.

## 4. System Prompt

The system prompt defines the agent's role, available tools, and behavior.

```text
You are an AI News Assistant. Your objective is to help
users discover and understand the latest news worldwide.

Available tools:
- live_news_search
- news_by_topics
- news_by_location

Instructions:
1. Understand the user's request before selecting a tool.
2. Choose the most appropriate tool for the request.
3. Use fresh search results for current news.
4. Summarize retrieved news clearly and accurately.
5. Include publication dates and original source links when available.
6. Never fabricate news, facts, or sources.
7. Distinguish confirmed information from unverified claims.
8. Mention conflicting reports when relevant.
9. If information is unavailable, communicate this honestly.

Tone:
Be neutral, objective, professional, and concise.
Avoid sensationalism and political bias.
```
