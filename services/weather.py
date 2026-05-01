import requests
import streamlit as st


@st.cache_data(ttl=1800)
def get_weather(lat: float, lon: float) -> dict:
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,weathercode"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&timezone=auto&forecast_days=1"
    )
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()
