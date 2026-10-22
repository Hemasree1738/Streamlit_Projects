import pandas as pd
import streamlit as st

st.title("Upload CSV and Analyze")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Statistics")
    st.write(df.describe())

    st.subheader("Filter by Column")
    col = st.selectbox("Choose column", df.columns)
    value = st.text_input("Filter value")

    if value:
        filtered = df[df[col].astype(str).str.contains(value, case=False)]
        st.dataframe(filtered)

    st.subheader("Sort")
    sort_col = st.selectbox("Sort by", df.columns, key="sort")
    st.dataframe(df.sort_values(sort_col))

# Exercise 1: Download button
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="processed.csv",
    mime="text/csv",
)

# Exercise 2: Handle missing values
st.subheader("Missing Values")
st.write(df.isnull().sum())
option = st.radio("Handle missing:", ["Keep", "Drop", "Fill with 0"])

if option == "Drop":
    df = df.dropna()
elif option == "Fill with 0":
    df = df.fillna(0)

st.dataframe(df)

# Exercise 3: Group by and aggregate
if "name" in df.columns:
    group_col = st.selectbox("Group by", df.columns)
    num_cols = df.select_dtypes("number").columns
    if len(num_cols) > 0:
        agg = df.groupby(group_col)[num_cols].mean()
        st.dataframe(agg)
