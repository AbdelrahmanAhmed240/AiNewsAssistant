
import os
from dotenv import load_dotenv

load_dotenv()

# LLM configuration
GROQ_LLM_MODEL = "openai/gpt-oss-120b"

# Embedding configuration
EMBED_MODEL = "BAAI/bge-small-en-v1.5"

# ChromaDB configuration
CHROMA_PATH = "./ai_news_chroma_db"
COLLECTION = "news_articles"


def get_llm(**kwargs):
    """Initialize and return Groq LLM."""

    from llama_index.llms.openai_like import OpenAILike

    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is missing from .env")

    return OpenAILike(
        model=GROQ_LLM_MODEL,
        api_base="https://api.groq.com/openai/v1",
        api_key=groq_api_key,
        is_chat_model=True,
        is_function_calling_model=True,
        **kwargs
    )


def get_embed_model():
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding

    return HuggingFaceEmbedding(model_name=EMBED_MODEL)
