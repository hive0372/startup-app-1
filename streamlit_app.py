import streamlit as st
import requests

st.title("🔎 Keyword-based Web Search (via SerpAPI)")

api_key = "077fd1a463d500878454573862f5f76b4f4f3ad6f7a2e754e22c6e458a9dbaa7"  # Replace with your key

query = st.text_input("Enter keyword to search news for:", value="startup funding")

if st.button("Search"):
    url = f"https://serpapi.com/search.json?q={query}&hl=en&gl=us&api_key={api_key}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        if "organic_results" in data:
            st.subheader("📰 Top Search Results")
            for result in data["organic_results"][:10]:
                st.markdown(f"- **[{result['title']}]({result['link']})**")
        else:
            st.warning("No results found.")
    else:
        st.error("Failed to fetch results from SerpAPI.")
