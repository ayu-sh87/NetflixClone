import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analytics Dashboard")

if "history" in st.session_state and st.session_state.history:
    df = pd.DataFrame(st.session_state.history)

    counts = df["result"].value_counts().reset_index()
    counts.columns = ["Type", "Count"]

    fig = px.pie(counts, names="Type", values="Count",
                 title="Prediction Distribution")

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("No data available yet.")
