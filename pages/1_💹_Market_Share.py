import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Market Share", page_icon="💊")
st.sidebar.header("Market Share Analysis")

st.title("Market Share Analysis")
st.write(
    """This demo illustrates a market share analysis result from the mock anonymous sample data. Enjoy!"""
)

df_market = pd.read_csv("data/MarketShare.csv")

drug_selected = st.multiselect("Which drug(s):",
                                df_market['Brand'].unique(),
                                df_market['Brand'].unique())


st.write("")
st.write("")

df_market['Year'] = pd.DatetimeIndex(pd.to_datetime(df_market["Date"])).year

year_range = st.slider(
     "Which Year(s):", 2015, 2022, (2015, 2022))

df_selected = df_market.loc[(df_market["Brand"].isin(drug_selected)) &
                            (df_market["Year"] >= year_range[0]) &
                            (df_market["Year"] <= year_range[1])
                            ]

st.write("")
st.write("")

selection = alt.selection_multi(fields=['Brand'], bind='legend')

c = alt.Chart(df_selected, title="Drug Market Share (by Patient Numbers)")\
    .mark_area()\
    .encode(
        x=alt.X("Date:T", axis=alt.Axis(format='%Y/%m', domain=False, tickSize=0)),
        y=alt.Y("Patients:Q", stack='center'),
        color=alt.Color('Brand:N',scale=alt.Scale(scheme='category20b')),
        order=alt.Order('sum(Patients):Q', sort='ascending'),
        opacity=alt.condition(selection, alt.value(1), alt.value(0.1)))\
    .properties(
        width=650,
        height=600)\
    .add_selection(
        selection)
st.altair_chart(c, use_container_width=True)

with st.expander("See the market share data"):
    st.table(df_market)

st.markdown(""" ###### © 2022 Xinjie Qiu℠""")
