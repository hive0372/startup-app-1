import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Web Scraper Search", layout="wide")
st.title("🔎 Keyword Web Scraper (DuckDuckGo, No API)")

query = st.text_input("Enter your keyword:", "startup funding")

if st.button("Search"):
    with st.spinner("Scraping web results from DuckDuckGo..."):
        try:
            results = []
            with DDGS() as ddgs:
                for r in ddgs.text(query, max_results=10):
                    results.append(r)

            if not results:
                st.warning("No results found.")
            else:
                st.subheader("🔗 Top Search Results")
                for i, res in enumerate(results, 1):
                    st.markdown(f"{i}. **[{res['title']}]({res['href']})**  \n{res['body']}")

        except Exception as e:
            st.error(f"Error occurred: {e}")

st.markdown("---")
st.markdown("⚠️ Demo tool using unofficial DuckDuckGo search. Not suitable for heavy scraping.")
