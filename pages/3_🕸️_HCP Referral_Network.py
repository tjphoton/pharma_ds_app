import streamlit as st
import pandas as pd
import altair as alt
import networkx
import plotly.figure_factory as ff

# import numpy as np
# import matplotlib.pyplot as plt

st.set_page_config(page_title="HCP referring network", page_icon="🕸️")
st.sidebar.header("HCP Referring Network Analysis")

st.title("HCP Referring Network Analysis")
st.write(
    """This demo illustrates HCP referring network from a mock anonymous sample data. Enjoy!"""
)

st.image("figures/hcp_network.png", width=600)

df_refer = pd.read_csv("data/Refer.csv")

mcol1, mcol2, mcol3, mcol4 = st.columns([0.1, 2.5, 0.3, 5])

with mcol2:
    st.write("")
    st.write("")
    st.write("")
    hcp_selected = st.radio("Which doctor:",
                             ["None Selected",
                              "NPI8998",
                              "NPI7995",
                              "NPI7606",
                              "NPI4602",
                              "NPI9503",
                              "NPI2485"])

with mcol4:
    if hcp_selected == "NPI4602":
        st.image("figures/hcp_network_zoom_NPI_4602.png", width=300)
    elif hcp_selected == "NPI8998":
        st.image("figures/hcp_network_zoom_NPI_8998.png", width=300)
    elif hcp_selected == "NPI7606":
        st.image("figures/hcp_network_zoom_NPI_7606.png", width=300)
    elif hcp_selected == "NPI7995":
        st.image("figures/hcp_network_zoom_NPI_7995.png", width=300)
    elif hcp_selected == "NPI9503":
        st.image("figures/hcp_network_zoom_NPI_9503.png", width=300)
    elif hcp_selected == "NPI2485":
        st.image("figures/hcp_network_zoom_NPI_2485.png", width=300)
    else:
        st.image("figures/hcp_network_zoom_NPI.png", width=300)


st.table(df_refer[df_refer.isin([hcp_selected]).any(axis=1)])

st.markdown(""" ###### © 2022 Xinjie Qiu℠""")