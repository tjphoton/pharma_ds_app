import streamlit as st
import pandas as pd
import altair as alt
# import numpy as np
# import matplotlib.pyplot as plt

st.set_page_config(page_title="Channel Optimization", page_icon="📊")
st.sidebar.header("Channel Optimization")

st.title("Digital Channel Selection and Optimization")
st.write(
    """This demo illustrates a channel optimization model from a mock anonymous sample data. Enjoy!"""
)

st.image("figures/channel.png", width=600)
st.image("figures/efficiency.png", width=600)

st.markdown(""" ###### © 2022 Xinjie Qiu℠""")