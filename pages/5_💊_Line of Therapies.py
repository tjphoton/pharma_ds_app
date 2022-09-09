import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="LOT", page_icon="💊")
st.sidebar.header("Line of Therapies Analysis")

st.title("Line of Therapies Analysis")
st.write(
    """This demo illustrates a line of therapies analysis from a mock anonymous sample data. Enjoy!"""
)

df_lot = pd.read_csv("data/LOT.csv")

selection = alt.selection_multi(fields=['Brand'], bind='legend')

c = alt.Chart(df_lot, title="Percentage Share in EAch Line of Therapies")\
    .mark_area().encode(
        x=alt.X("LOT:N"),
        y=alt.Y("Percentage:Q", stack='center', axis=alt.Axis(format='.0%')),
        color=alt.Color('Brand:N'),
        order=alt.Order('sum(Percentage):Q', sort='ascending'),
        opacity=alt.condition(selection, alt.value(1), alt.value(0.1)))\
    .properties(
        width=650,
        height=500)\
    .add_selection(
        selection)

st.altair_chart(c, use_container_width=True)

with st.expander("A more prettier graph created with Tableau®"):
    st.image("figures/LOT.png", width=450)

with st.expander("See the line of therapies data"):
    st.table(df_lot)

st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")