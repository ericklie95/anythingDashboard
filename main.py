import streamlit as st
import datetime

def main():
    # --- UI CONFIGURATION ---
    st.set_page_config(page_title="My Command Centre", layout="wide")
    st.title("⚡ Personal Intelligence Dashboard")
    sidebar_display()
    main_layout()

'''
Sidebar display would include the following:
1. Sign up/sign in form.
    - Need to be safe account management with password to each users.
    - Data will be sent and saved (also retrieved later on) via Google Sheets API.
    - Password will be hashed.
2. Help button
    - Show quickly what each tabs do. Tabs need to be referred globally.
'''
def sidebar_display():
    sidebar = st.sidebar
    sidebar.title("Sidebar")

    daily_form = sidebar.form("daily_log_form")
    today = datetime.date.today().strftime("%d-%m-%Y")
    daily_form.write(f"Logging stats for: {today}")
    
    ''' ### Plan to remove this.
    sidebar.header("📝 Daily Log")
    warmup = st.checkbox("6:30 AM Breakfast & Warm-up")
    teaser = st.checkbox("12:00 PM Lunch & Teaser")
    review = st.checkbox("6:00 PM Dinner & Review")
    '''

    if daily_form.form_submit_button("Save to Cloud"):
        success = True # TODO: Implement the logic to save the logged stats to Google Sheets using the Sheets API
        if success:
            sidebar.success("Successfully signed in!")
            st.cache_data.clear() # Force clear cache so analytics tab updates
        else:
            sidebar.error("Failed to sign in - Failed saving to Google Sheets.")


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

'''
TODO: Need to create the tabs - can it be dynamic and configured for each users?
Within this tab:
    1. Show the first tab as weather overview. Location should be automatically set.
    TODO: Free weather API, option to change location.
    2. Show the second tab as Calendar and Task from Google Calendar.
    TODO: Google Calendar sync via API.
'''
def display_todays_overview(subheader, header):
    st.subheader(subheader)
    st.header(header)
    st.write("Here you can see a summary of today's activities and stats.")

'''
This will be an interactive report that allows end-user to use filter.

This tab will have two more tabs within it:
    - First tab is for the details of the list.
    TODO: Implement this list so it syncs via Google API, allow import file (CSV or Excel).
    - Second tab is for the interactive graph.
    Interactive graph will allow user to choose which graph they need.
'''
def display_performance_analytics(subheader, header):
    st.subheader(subheader)
    st.header(header)
    st.write("This section will show your performance trends and insights over time.")

'''
This tab will be a custom 
'''
def display_quick_actions(subheader, header):
    st.subheader(subheader)
    st.header(header)
    st.write("Access your most used features and shortcuts here.")
    
if __name__ == "__main__":
    main()