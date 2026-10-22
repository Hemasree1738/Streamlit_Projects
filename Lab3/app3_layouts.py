import numpy as np
import pandas as pd
import streamlit as st

st.title("Layouts Demo")

st.sidebar.header("Settings")
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])
font_size = st.sidebar.slider("Font Size", 10, 30, 15)

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Sales", "25 Lakh")
with col2:
    st.metric("Customers", "1,200")

tab1, tab2, tab3 = st.tabs(["Overview", "Analysis", "About"])
with tab1:
    st.write("Overview content here")
with tab2:
    st.write("Analysis content here")
with tab3:
    st.write("About this app")

with st.container():
    st.write("### Grouped Section")
    st.write("All these elements are inside one container.")

# Exercise 1
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    st.write("Left (narrow)")
with c2:
    st.write("Center (wide)")
with c3:
    st.write("Right (narrow)")

# Exercise 2
with st.expander("Details"):
    st.write("This content is hidden until expanded.")
    st.write("You can put anything here.")

# Exercise 3
df = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
tab1, tab2 = st.tabs(["Line", "Bar"])
with tab1:
    st.line_chart(df)
with tab2:
    st.bar_chart(df)
