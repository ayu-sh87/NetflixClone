import streamlit as st
import json

st.set_page_config(page_title="AI Platform", layout="centered")

# Load users
with open("users.json") as f:
    users = json.load(f)

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------- Login Screen ----------
if not st.session_state.logged_in:

    st.title("AI Duplicate Detection Platform")
    st.write("Please log in to continue.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")

# ---------- After Login ----------
else:
    st.sidebar.success(f"Logged in as {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("Welcome to AI Duplicate Detection Platform")
    st.write("Use the sidebar to navigate between pages.")
