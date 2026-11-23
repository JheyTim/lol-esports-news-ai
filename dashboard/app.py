import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import streamlit as st

# Dashboard configuration
API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="LoL Esports News AI", page_icon="📰", layout="wide")

# DASHBOARD TITLE
st.title("📰 League of Legends Esports News AI")

st.caption("Initial project dashboard")

st.divider()


# API REQUEST FUNCTION
def get_api_data(endpoint):

    url = f"{API_BASE_URL}{endpoint}"

    with urlopen(url, timeout=5) as response:
        response_data = response.read()

    return json.loads(response_data.decode("utf-8"))


# BACKEND HEALTH CHECK
st.subheader("Backend connection")

if st.button("Check API connection"):
    try:
        result = get_api_data("/health")

        if result["status"] == "healthy":
            st.success("FastAPI backend is connected!")

        else:
            st.warning("The backend returned an unexpected status.")

    except (HTTPError, URLError, TimeoutError, ValueError) as error:
        st.error(f"Unable to connect to FastAPI: {error}")


# ARTICLE DISPLAY
st.divider()

st.subheader("Collected News Articles")

if st.button("Load articles"):
    try:
        articles = get_api_data("/articles")

        if articles:
            st.dataframe(articles, use_container_width=True)

            st.success(f"Retrieved {len(articles)} articles.")

        else:
            st.info("No articles found in the database.")

    except (HTTPError, URLError, TimeoutError, ValueError) as error:
        st.error(f"Unable to retrieve articles: {error}")
