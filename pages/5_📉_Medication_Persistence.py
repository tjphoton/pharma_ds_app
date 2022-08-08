import streamlit as st
import pandas as pd
import altair as alt
# import numpy as np
# import matplotlib.pyplot as plt

st.set_page_config(page_title="Persistence", page_icon="📉")
st.sidebar.header("Medication Persistence Analysis")

st.title("Medication persistence Analysis")
st.write(
    """This demo illustrates a result of medication persistence from a mock anonymous sample data. Enjoy!"""
)

st.image("figures/persistence.png", width=600)

st.write(" Medication adherence measures how long patients remain on their treatment therapies.")
st.write(" Adherence drop off rate (the time at which patient population is reduced to 1/e ≈ 36.8%) for medicines:")
st.markdown("""
            - Rytary - 474 days
            - Gocovri – 267 days
            - Apokyn – 137 days
            - Nourianz – 115 days
            - Ongentys -  102 days
            - Inbrija – 22 days
            - Kynmobi – 21 days
            """)

st.markdown(""" ###### © 2022 Xinjie Qiu℠""")