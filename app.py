import streamlit as st
from components.sidebar import sidebar_display
from components.overview import display_todays_overview
from components.analytics import display_performance_analytics
from components.quick_actions import display_quick_actions


def run():
    st.set_page_config(page_title="My Command Centre", layout="wide")
    st.title("⚡ Personal Intelligence Dashboard")

    sidebar_display()

    if not st.session_state.get("authenticated"):
        st.info("👈 Sign in from the sidebar to access your dashboard.")
        return

    tab1, tab2, tab3 = st.tabs(["📅 Today's Overview", "📈 Performance Analytics", "⚡ Quick Actions"])

<<<<<<< HEAD
<<<<<<< HEAD
    '''
=======
>>>>>>> ec38d21 (making it modular for each visible tabs have its own file)
=======
>>>>>>> ec38d21 (making it modular for each visible tabs have its own file)
    with tab1:
        display_todays_overview()

    with tab2:
        display_performance_analytics()

    with tab3:
        display_quick_actions()
<<<<<<< HEAD
<<<<<<< HEAD
    '''
=======
>>>>>>> ec38d21 (making it modular for each visible tabs have its own file)
=======
>>>>>>> ec38d21 (making it modular for each visible tabs have its own file)
