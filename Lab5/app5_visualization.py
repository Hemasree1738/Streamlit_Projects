import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Data Visualization")

# Sample data
df = pd.DataFrame(
    np.random.randn(20, 3), columns=["Math", "Science", "English"]
)

st.subheader("Built-in Charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

st.subheader("Matplotlib Chart")
fig, ax = plt.subplots()
ax.hist(df["Math"], bins=10, color="skyblue")
ax.set_title("Math Score Distribution")
st.pyplot(fig)

# Exercise 1: Plotly chart
st.subheader("Plotly Chart")
fig_plotly = px.histogram(df, x="Math", nbins=10, title="Math Distribution")
st.plotly_chart(fig_plotly, use_container_width=True)

# Exercise 2: Scatter plot
st.subheader("Scatter Plot")
st.scatter_chart(df, x="Math", y="Science")

# Exercise 3: Metric showing mean
st.subheader("Summary Metric")
st.metric("Average Math Score", f"{df['Math'].mean():.2f}")
