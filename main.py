import streamlit as st
import datetime

def main():
    # --- UI CONFIGURATION ---
    st.set_page_config(page_title="My Command Centre", layout="wide")
    st.title("⚡ Personal Intelligence Dashboard")
    sidebar_display()
    main_layout()

def sidebar_display():
    sidebar = st.sidebar
    sidebar.title("Sidebar")
    sidebar.header("📝 Daily Log")

    daily_form = sidebar.form("daily_log_form")
    today = datetime.date.today().strftime("%d-%m-%Y")
    daily_form.write(f"Logging stats for: {today}")
    warmup = st.checkbox("6:30 AM Breakfast & Warm-up")
    teaser = st.checkbox("12:00 PM Lunch & Teaser")
    review = st.checkbox("6:00 PM Dinner & Review")

    if daily_form.form_submit_button("Save to Cloud"):
        success = True # TODO: Implement the logic to save the logged stats to Google Sheets using the Sheets API
        if success:
            sidebar.success("Stats successfully logged!")
            st.cache_data.clear() # Force clear cache so analytics tab updates
        else:
            sidebar.error("Failed to save to Google Sheets.")
            

def main_layout():
    st.header("📊 Analytics")
    st.write("This section will display your performance analytics based on the logged data.")
    mytabs = ["📅 Today's Overview", "📈 Performance Analytics", "⚡ Quick Actions"]
    tab1, tab2, tab3 = st.tabs(mytabs)        

    with tab1:
        subheader = mytabs[0]
        header = "Today's Summary"
        display_todays_overview(subheader, header)

    with tab2:
        subheader = mytabs[1]
        header = "Performance Trends"
        display_performance_analytics(subheader, header)

    with tab3:
        subheader = mytabs[2]
        header = "Quick Actions"
        display_quick_actions(subheader, header)

def display_todays_overview(subheader, header):
    st.subheader(subheader)
    st.header(header)
    st.write("Here you can see a summary of today's activities and stats.")

def display_performance_analytics(subheader, header):
    st.subheader(subheader)
    st.header(header)
    st.write("This section will show your performance trends and insights over time.")

def display_quick_actions(subheader, header):
    st.subheader(subheader)
    st.header(header)
    st.write("Access your most used features and shortcuts here.")
    
if __name__ == "__main__":
    main()