import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Dashboard")

# Exercise 3: Date range filter
df = pd.DataFrame({
    "Year": np.random.choice([2022, 2023, 2024], 200),
    "Region": np.random.choice(["North", "South", "East", "West"], 200),
    "Product": np.random.choice(["A", "B", "C"], 200),
    "Sales": np.random.randint(1000, 10000, 200),
    "Date": pd.date_range("2022-01-01", periods=200, freq="D")
})

st.sidebar.header("Filters")
year = st.sidebar.multiselect("Year", df["Year"].unique(), default=df["Year"].unique())
region = st.sidebar.multiselect("Region", df["Region"].unique(), default=df["Region"].unique())
product = st.sidebar.multiselect("Product", df["Product"].unique(), default=df["Product"].unique())

# Exercise 3: Date range filter
date_range = st.sidebar.date_input(
    "Date range",
    value=(df["Date"].min(), df["Date"].max())
)

filtered = df[
    (df["Year"].isin(year)) &
    (df["Region"].isin(region)) &
    (df["Product"].isin(product))
]

# Exercise 3: Date range filter
if len(date_range) == 2:
    filtered = filtered[
        (filtered["Date"] >= pd.Timestamp(date_range[0])) &
        (filtered["Date"] <= pd.Timestamp(date_range[1]))
    ]

c1, c2, c3 = st.columns(3)
avg_sales = int(filtered["Sales"].mean()) if not filtered.empty else 0
c1.metric("Total Sales", f"{filtered['Sales'].sum():,}")
c2.metric("Avg Sales", f"{avg_sales:,}")
c3.metric("Records", len(filtered))

st.bar_chart(filtered.groupby("Region")["Sales"].sum())
st.line_chart(filtered.groupby("Year")["Sales"].sum())

# Exercise 1: Pie chart of sales by product
pie_data = filtered.groupby("Product")["Sales"].sum().reset_index()
fig = px.pie(pie_data, names="Product", values="Sales", title="Sales by Product")
st.plotly_chart(fig, use_container_width=True)

# Exercise 2: Download filtered CSV
csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button("Download Filtered CSV", csv, "filtered_sales.csv", "text/csv")

# Exercise 3: Date range filter

df ["Date"] = pd. date_range (" 2022 -01 -01 ", periods =200 , freq ="D")

date_range = st. sidebar.date_input (
    " Date range ",
    value =( df["Date"].min() , df["Date"]. max () )
)
if len( date_range ) == 2:
    filtered = filtered [
        ( filtered["Date"] >= pd. Timestamp ( date_range [0]) ) &
        ( filtered["Date"] <= pd. Timestamp ( date_range [1]) )
    ]
