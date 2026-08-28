import streamlit as st
from src.controller import get_all_jobs
from src.data_cleaning import clean_data

st.set_page_config(page_title="Job Dashboard", page_icon="💼", layout="wide")

st.markdown("## 💼 Job Market Analyzer Dashboard")
st.markdown("---")

# Sidebar
st.sidebar.header("🔍 Search Jobs")
role = st.sidebar.text_input("Job Role", "Data")
location = st.sidebar.text_input("Location", "India")

if "df" not in st.session_state:
    st.session_state.df = None

# Fetch data
if st.sidebar.button("🚀 Search Jobs"):
    with st.spinner("⏳ Fetching jobs..."):
        data = get_all_jobs(role, location)
        df = clean_data(data)
        st.session_state.df = df

    st.success(f"✅ {len(df)} Jobs Found")

# Display
if st.session_state.df is not None:
    df = st.session_state.df.copy()

    # Filters
    st.markdown("### 🔎 Filter Jobs")
    col1, col2 = st.columns(2)

    with col1:
        company_filter = st.selectbox("Company", ["All"] + sorted(df["company"].unique()))
    with col2:
        location_filter = st.selectbox("Location", ["All"] + sorted(df["location"].unique()))

    if company_filter != "All":
        df = df[df["company"] == company_filter]

    if location_filter != "All":
        df = df[df["location"] == location_filter]

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Jobs", len(df))
    col2.metric("Companies", df["company"].nunique())
    col3.metric("Locations", df["location"].nunique())

    st.markdown("---")

    # Search
    search = st.text_input("🔍 Search jobs")
    if search:
        df = df[
            df["title"].str.contains(search, case=False, na=False) |
            df["company"].str.contains(search, case=False, na=False)
        ]

    # Clickable links
    df_display = df.copy()
    df_display["link"] = df_display["link"].apply(
        lambda x: f'<a href="{x}" target="_blank">🔗 View</a>' if x != "N/A" else "N/A"
    )

    st.write("### 📄 Job Listings")
    st.write(df_display.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Download
    csv = df.to_csv(index=False)
    st.download_button("📥 Download CSV", csv, "jobs_data.csv")

    st.markdown("---")

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📊 Jobs by Platform")
        st.bar_chart(df["source"].value_counts())

    with col2:
        st.write("### 🏢 Top Companies")
        st.bar_chart(df["company"].value_counts().head(10))

    st.write("### 📍 Top Locations")
    st.bar_chart(df["location"].value_counts().head(10))

else:
    st.info("👉 Use sidebar to search jobs")