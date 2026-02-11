import streamlit as st
import helper
import pickle
import time
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

st.title("Duplicate Question Predictor")

q1 = st.text_area("Question 1")
q2 = st.text_area("Question 2")

if st.button("Analyze"):

    with st.spinner("AI is thinking..."):
        time.sleep(1.5)

    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.success("Duplicate Questions")
    else:
        st.error("Not Duplicate")

    # Save to history
    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append({
        "q1": q1,
        "q2": q2,
        "result": "Duplicate" if result else "Not Duplicate"
    })
