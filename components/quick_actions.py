import streamlit as st

SHORTCUTS = [
    {"label": "GitHub", "url": "https://github.com/ericklie95"},
    {"label": "Google Calendar", "url": "https://calendar.google.com"},
    {"label": "Google Sheets", "url": "https://sheets.google.com"},
    {"label": "Gmail", "url": "https://mail.google.com"},
]


def display_quick_actions():
    st.header("Quick Actions")
    st.write("Your most-used links and shortcuts.")

    cols = st.columns(4)
    for i, shortcut in enumerate(SHORTCUTS):
        with cols[i % 4]:
            st.link_button(shortcut["label"], shortcut["url"], use_container_width=True)
