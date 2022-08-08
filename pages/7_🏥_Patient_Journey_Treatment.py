import streamlit as st
import pandas as pd
import altair as alt
# import numpy as np
# import matplotlib.pyplot as plt

st.set_page_config(page_title="Treatment Journey", page_icon="🏥")
st.sidebar.header("Patient Treatment Journey Analysis")

st.title("Patient Treatment Journey Analysis")
st.write(
    """This demo illustrates a patient treatment journey from a mock anonymous sample data. Enjoy!"""
)
# 📊 📈 📉 💹 📋 🚑 ⏳ ⌛ 🚑 💊 🩻 🏥 🩺 🛣️ 🌐 🕷️ 🕸️

df_pharmacy = pd.read_csv("data/Pharmacy.csv", dtype={"NDC11":str})
df_pharmacy = df_pharmacy[["Patient_ID", "DATE_OF_SERVICE", "NDC11"]].dropna().rename(columns={"NDC11": "NDC"})

df_drug = pd.read_csv("data/Drug.csv", dtype={"NDC":str})
df_drug = df_drug[["NDC", "ALL_INGREDIENTS"]]

df_pharmacy_drug = df_pharmacy.merge(df_drug, on="NDC")

drug_selected = st.multiselect("Which drug(s)",
                               df_pharmacy_drug["ALL_INGREDIENTS"].unique(),
                               ["etanercept || Enbrel",
                                "adalimumab || Humira",
                                "infliximab || Remicade",
                                "secukinumab || Cosentyx",
                                "ustekinumab || Stelara",
                                "certolizumab pegol || Cimzia",
                                "ixekizumab || Taltz",
                                "guselkumab || Tremfya",
                                "risankizumab || Skyrizi"
                                ])

patient_id = st.selectbox(
    'Which patient?',
    df_pharmacy_drug[df_pharmacy_drug["ALL_INGREDIENTS"].isin(drug_selected)][["Patient_ID", "ALL_INGREDIENTS"]]
    .groupby("Patient_ID")
    .nunique()
    .sort_values('ALL_INGREDIENTS', ascending=False).index.tolist()
)

patient_selected = df_pharmacy_drug[(df_pharmacy_drug["Patient_ID"] == patient_id) &
                                    (df_pharmacy_drug["ALL_INGREDIENTS"].isin(drug_selected))
                                    ]

c = alt.Chart(patient_selected).mark_circle(size=100).encode(
    x=alt.X('DATE_OF_SERVICE:T', axis=alt.Axis(labelAngle=90)),
    y=alt.Y('ALL_INGREDIENTS:N'),
    color=alt.Color('ALL_INGREDIENTS', legend=None)
).properties(
    width=650,
    height=600
)
st.altair_chart(c, use_container_width=True)

with st.expander("See the journey data"):
    st.table(patient_selected.sort_values('DATE_OF_SERVICE', ascending=True))

st.markdown(""" ###### © 2022 Xinjie Qiu℠""")