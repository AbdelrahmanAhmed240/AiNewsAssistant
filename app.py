
import random
import streamlit as st

from tools.news_search import fetch_latest_headlines
from tools.live_news import live_news_search
from tools.topic_news import news_by_topics
from tools.location_news import news_by_location


# Page configuration
st.set_page_config(
    page_title="AI News Assistant",
    page_icon="📰",
    layout="wide"
)


# Styling
st.markdown("""
<style>
.stApp { background: #f5f7fc; }
.block-container { max-width: 1150px; padding-top: 2rem; }

.hero {
    background: linear-gradient(120deg, #111c40, #2563eb);
    padding: 38px;
    border-radius: 20px;
    margin-bottom: 30px;
}
.hero h1 { color: white; font-size: 38px; }
.hero p { color: #dbeafe; font-size: 16px; margin-bottom: 0; }

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
}

.stButton button, .stLinkButton a {
    border-radius: 9px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# Header
st.markdown("""
<div class="hero">
    <h1>📰 AI News Assistant</h1>
    <p>Stay informed. Explore stories. Understand the world with AI.</p>
</div>
""", unsafe_allow_html=True)


# Homepage headlines
@st.cache_data(ttl=600, show_spinner=False)
def get_headlines():
    return fetch_latest_headlines()


if "featured" not in st.session_state:
    with st.spinner("Discovering the latest headlines..."):
        news = get_headlines()
        st.session_state.featured = random.sample(news, min(3, len(news)))


st.subheader("✨ Latest Headlines")
st.caption("A selection of recent stories from around the world.")

if st.button("🔄 Refresh Headlines"):
    get_headlines.clear()
    with st.spinner("Finding fresh headlines..."):
        news = get_headlines()
        st.session_state.featured = random.sample(news, min(3, len(news)))

articles = st.session_state.featured

if articles:
    columns = st.columns(len(articles))

    for col, article in zip(columns, articles):
        with col:
            with st.container(border=True):
                st.caption(article.get("source", "Latest News"))
                st.markdown(f"**{article.get('title', 'Untitled')}**")

                if article.get("published"):
                    st.caption(f"📅 {article['published']}")

                if article.get("url"):
                    st.link_button(
                        "Read Full Story ↗",
                        article["url"],
                        use_container_width=True
                    )
else:
    st.info("No headlines available. Try refreshing later.")


# Display search results
def display_articles(articles):
    if not articles:
        st.info("No articles found. Try another search.")
        return

    st.success(f"Found {len(articles)} articles.")

    for article in articles:
        with st.container(border=True):
            st.subheader(article.get("title", "Untitled Article"))

            source = article.get("source", "News")
            published = article.get("published")
            st.caption(f"{source}" + (f" • {published}" if published else ""))

            summary = article.get("summary")

            if isinstance(summary, dict):
                st.write(summary.get("short_summary", "No summary available."))

                points = summary.get("key_points", [])
                if points:
                    with st.expander("Key Points"):
                        for point in points:
                            st.write(f"• {point}")
            else:
                st.write("No summary available for this article.")

            if article.get("url"):
                st.link_button("Read Original Article ↗", article["url"])


# Reusable search panel
def search_panel(title, placeholder, key, search_function):
    st.subheader(title)

    with st.form(key=f"{key}_form"):
        query = st.text_input("Enter your search", placeholder=placeholder)
        submitted = st.form_submit_button("🔎 Search", use_container_width=True)

    result_key = f"{key}_results"

    if submitted:
        if query.strip():
            with st.spinner("Searching news and generating summaries..."):
                st.session_state[result_key] = search_function(query.strip())
        else:
            st.warning("Please enter a search query.")

    if result_key in st.session_state:
        display_articles(st.session_state[result_key])


# Search section
st.divider()
st.subheader("🔎 Explore the News")
st.caption("Find stories by keyword, topic, or location.")

tab1, tab2, tab3 = st.tabs([
    "🌍 General News",
    "🏷️ Topics",
    "📍 Location"
])

with tab1:
    search_panel(
        "Search the News",
        "e.g. Latest AI developments",
        "general",
        live_news_search
    )

with tab2:
    search_panel(
        "Explore a Topic",
        "e.g. Artificial Intelligence",
        "topic",
        news_by_topics
    )

with tab3:
    search_panel(
        "Explore by Location",
        "e.g. Egypt or London",
        "location",
        news_by_location
    )