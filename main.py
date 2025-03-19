import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit App Title
st.title("📊 Data-Driven Streamlit Dashboard")

# Upload CSV File
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Display Data
    st.subheader("📜 Dataset Preview")
    st.write(df.head())

    # Show Summary
    st.subheader("📊 Dataset Summary")
    st.write(df.describe())

    # Select Column for Visualization
    column = st.selectbox("Select a column for visualization", df.columns)

    # Generate Charts
    if df[column].dtype in ['int64', 'float64']:  # Numeric data
        fig = px.histogram(df, x=column, title=f"Distribution of {column}")
        st.plotly_chart(fig)

    elif df[column].dtype == 'object':  # Categorical data
        fig = px.bar(df[column].value_counts(), title=f"Counts of {column}")
        st.plotly_chart(fig)

    # Data Filtering
    st.subheader("🔍 Data Filtering")
    filter_value = st.text_input(f"Filter rows where {column} contains:")
    if filter_value:
        filtered_df = df[df[column].astype(str).str.contains(filter_value, case=False)]
        st.write(filtered_df)

    # Download Processed Data
    st.subheader("⬇️ Download Processed Data")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")

else:
    st.warning("Please upload a CSV file to start analyzing data.")

