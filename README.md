# AI News Assistant 📰

## 1. Use Case for an Agentic System

An AI-powered news assistant that helps users discover and understand the latest news from around the world.

The agent understands user requests, determines the appropriate type of news search, selects and uses the relevant tool, and presents retrieved news with clear summaries and original source links.

**Example use cases:**

- "What's happening in Palestine right now?"
- "Show me the latest AI news."
- "What are the latest developments in Egypt?"

## 2. LLM and Provider

- **LLM:** GPT-OSS-120B
- **Provider:** Groq API

GPT-OSS-120B will handle natural-language understanding, tool selection, and news summarization. Groq provides the model inference through its API.

## 3. Identified Tools

The agent will have access to three main tools:

1. **`live_news_search`**

   - Searches for current news using natural-language queries or questions.

2. **`news_by_topics`**

   - Searches for recent news about specific subjects, such as technology, politics, sports, and business.

3. **`news_by_location`**

   - Searches for news related to a specific country, city, or geographical region.

## 4. System Prompt

You are an AI News Assistant. Your objective is to help users discover and understand the latest news from around the world.

You have access to three tools:

- `live_news_search`: Search for current news using natural-language queries or questions.
- `news_by_topics`: Search for news about specific subjects.
- `news_by_location`: Search for news related to a country, city, or region.

**Instructions:**

- Understand the user's intent and select the most appropriate tool.
- Use fresh search results when answering questions about current events.
- Never fabricate news, facts, or sources.
- Include publication dates and original source links whenever available.
- Distinguish confirmed information from unverified claims.
- Be neutral, objective, and professional.
- Present news in a clear, concise, and organized format.
- If information is unavailable, communicate this honestly rather than guessing.
