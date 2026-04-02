import streamlit as st
import datetime

def main():
    # --- UI CONFIGURATION ---
    st.set_page_config(page_title="My Command Centre", layout="wide")
    st.title("⚡ Personal Intelligence Dashboard")
    # print("Hello, World!")
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
    tab1, tab2, tab3 = st.tabs(mytabs)

    with tab1:
        st.subheader(mytabs[0])
        st.header("Today's Summary")
        st.write("Here you can see a summary of today's activities and stats.") 

    with tab2:
        st.subheader(mytabs[1])
        st.header("Performance Trends")
        st.write("This section will show your performance trends and insights over time.") 

    with tab3:
        st.subheader(mytabs[2])
        st.header("Quick Actions")
        st.write("This section will provide quick access to your most used features and tools.")

if __name__ == "__main__":
    main()