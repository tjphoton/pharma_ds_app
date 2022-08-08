import streamlit as st
import pandas as pd
import altair as alt
# import numpy as np
# import matplotlib.pyplot as plt

st.set_page_config(page_title="LOT", page_icon="💊")
st.sidebar.header("Line of Therapies Analysis")

st.title("Line of Therapies Analysis")
st.write(
    """This demo illustrates a line of therapies analysis from a mock anonymous sample data. Enjoy!"""
)

st.image("figures/LOT.png", width=600)

st.markdown(""" ###### © 2022 Xinjie Qiu℠""")