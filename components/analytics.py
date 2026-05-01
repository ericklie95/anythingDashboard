import streamlit as st
import pandas as pd
from services import sheets


def display_performance_analytics():
    st.header("Performance Trends")

    with st.spinner("Loading data..."):
        try:
            records = sheets.read_sheet("data_to_visualise")
            df = pd.DataFrame(records)
        except Exception as e:
            st.warning(f"Could not load data: {e}")
            return

    if df.empty:
        st.info("No data available yet. Start logging to see trends.")
        return

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"]).sort_values("date")

    col1, col2 = st.columns(2)
    date_from = col1.date_input("From", value=df["date"].min().date())
    date_to = col2.date_input("To", value=df["date"].max().date())

    mask = (df["date"].dt.date >= date_from) & (df["date"].dt.date <= date_to)
    df = df[mask]

    if df.empty:
        st.info("No data in the selected range.")
        return

    df_indexed = df.set_index("date")

    if "github_commits" in df.columns:
        st.subheader("GitHub Commits per Day")
        st.bar_chart(df_indexed["github_commits"])

    if "notes" in df.columns:
        df["word_count"] = df["notes"].fillna("").apply(lambda x: len(str(x).split()))
        st.subheader("Notes Word Count")
        st.line_chart(df.set_index("date")["word_count"])

    st.divider()
    st.download_button(
        label="Export CSV",
        data=df.to_csv(index=False),
        file_name="logs.csv",
        mime="text/csv",
    )
