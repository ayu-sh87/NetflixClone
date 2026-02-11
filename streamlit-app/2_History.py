import streamlit as st
import pandas as pd

st.title("Prediction History")

if "history" in st.session_state and st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df)
else:
    st.info("No predictions yet.")
