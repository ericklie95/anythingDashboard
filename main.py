import streamlit as st
import datetime

def main():
    # --- UI CONFIGURATION ---
    st.set_page_config(page_title="My Command Centre", layout="wide")
    st.title("⚡ Personal Intelligence Dashboard")
    sidebar_display()
    main_layout()

def sidebar_display():
    st.sidebar.title("Sidebar")
    # --- SIDEBAR: DAILY LOG ---
    with st.sidebar:
        st.header("📝 Daily Log")
        with st.form("daily_log_form"):
            today = datetime.date.today().strftime("%Y-%m-%d")
            today_commits = 0 # TODO: Fetch the number of commits for today from the GitHub API
            
            st.write(f"Logging stats for: {today}")
            warmup = st.checkbox("6:30 AM Breakfast & Warm-up")
            teaser = st.checkbox("12:00 PM Lunch & Teaser")
            dinner = st.checkbox("6:00 PM Dinner & Review")
            
            submitted = st.form_submit_button("Save to Cloud")
            if submitted:
                success = True # TODO: Implement the logic to save the logged stats to Google Sheets using the Sheets API
                if success:
                    st.success("Stats successfully logged!")
                    st.cache_data.clear() # Force clear cache so analytics tab updates
                else:
                    st.error("Failed to save to Google Sheets.")
            

def main_layout():
    st.header("📊 Analytics")
    st.write("This section will display your performance analytics based on the logged data.")

    mytabs = ["📅 Today's Overview", "📈 Performance Analytics", "⚡ Quick Actions"]
    tabs = st.tabs(mytabs)

    tab_definitions = [
        {
            "label": mytabs[0],
            "title": "Today's Summary",
            "body": "Here you can see a summary of today's activities and stats.",
        },
        {
            "label": mytabs[1],
            "title": "Performance Trends",
            "body": "This section will show your performance trends and insights over time.",
        },
        {
            "label": mytabs[2],
            "title": "Quick Actions",
            "body": "This section will provide quick access to your most used features and tools.",
        },
    ]

    for tab, tab_definition in zip(tabs, tab_definitions):
        render_tab_content(tab, tab_definition)


def render_tab_content(tab, tab_definition):
    tab.subheader(tab_definition["label"])
    tab.header(tab_definition["title"])
    tab.write(tab_definition["body"])

if __name__ == "__main__":
    main()