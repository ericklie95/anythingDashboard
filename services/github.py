import datetime
import requests
import streamlit as st
import config


@st.cache_data(ttl=900)
def get_today_commits(username: str) -> int:
    today = datetime.date.today().isoformat()
    url = f"https://api.github.com/search/commits?q=author:{username}+committer-date:{today}"
    headers = {"Accept": "application/vnd.github.cloak-preview"}
    if config.GITHUB_TOKEN:
        headers["Authorization"] = f"token {config.GITHUB_TOKEN}"
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json().get("total_count", 0)
