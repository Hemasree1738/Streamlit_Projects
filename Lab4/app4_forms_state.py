import streamlit as st

st.title("Forms + Session State")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1
st.write("Counter:", st.session_state.count)

with st.form("login_form"):
    st.subheader("Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit:
    if user == "admin" and pwd == "1234":
        st.session_state.logged_in = True
        st.success("Login successful!")
    else:
        st.error("Invalid credentials")

if st.session_state.get("logged_in"):
    st.info("Welcome, admin! You are now logged in.")

# Exercise 1 and 2: Reset and Add 5 buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Increment "):
        st.session_state.count += 1

with col2:
    if st.button("Add 5"):
        st.session_state.count += 5

with col3:
    if st.button("Reset"):
        st.session_state.count = 0

st.write("Counter:", st.session_state.count)

# Exercise 3: To-do list with session state
if "todos" not in st.session_state:
    st.session_state.todos = []

with st.form("todo_form", clear_on_submit=True):
    task = st.text_input("New Task")
    add = st.form_submit_button("Add Task")

if add and task:
    st.session_state.todos.append(task)

st.subheader("Your Tasks")
for i, t in enumerate(st.session_state.todos):
    st.write(f"{i + 1}. {t}")

if st.button("Clear All"):
    st.session_state.todos = []
    st.rerun()
