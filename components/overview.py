import streamlit as st
from services import weather, github, calendar
import config


def display_todays_overview():
    st.header("Today's Summary")

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        st.subheader("📅 Today's Events")
        with st.spinner("Loading calendar..."):
            try:
                events = calendar.get_today_events()
                if events:
                    for event in events:
                        st.write(f"**{event['start']}** — {event['title']}")
                else:
                    st.info("No events today. (Connect Google Calendar to see events.)")
            except Exception as e:
                st.warning(f"Calendar unavailable: {e}")

    with col2:
        st.subheader("🌤 Weather")
        with st.spinner("Loading weather..."):
            try:
                data = weather.get_weather(config.WEATHER_LAT, config.WEATHER_LON)
                current = data["current"]
                daily = data["daily"]
                temp = current["temperature_2m"]
                high = daily["temperature_2m_max"][0]
                low = daily["temperature_2m_min"][0]
                st.metric("Now", f"{temp}°C")
                st.caption(f"High {high}°C / Low {low}°C")
            except Exception as e:
                st.warning(f"Weather unavailable: {e}")

    with col3:
        st.subheader("💻 GitHub")
        with st.spinner("Loading commits..."):
            try:
                if config.GITHUB_USERNAME:
                    count = github.get_today_commits(config.GITHUB_USERNAME)
                    st.metric("Commits today", count)
                else:
                    st.info("Set GITHUB_USERNAME in .env")
            except Exception as e:
                st.warning(f"GitHub unavailable: {e}")
