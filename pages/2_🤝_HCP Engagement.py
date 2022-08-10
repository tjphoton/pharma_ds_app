import streamlit as st

st.set_page_config(page_title="HCP Engagement", page_icon="🤝")
st.sidebar.header("HCP Engagement")

st.title("HCP Engagement")
st.write("")

mcol1, mcol2, mcol3 = st.columns(3)

with mcol1:
    st.markdown("### RWD Data")
    st.markdown("""
                - Medical claim
                - Pharmacy claim
                - EHR/EMR
                - HCP Specialty
                """)

with mcol3:
    st.markdown("### Market Research")
    st.markdown("""
                - Survey
                - Interview
                - Clinical trials
                - Secondary research
                """)

mcol1, mcol2, mcol3 = st.columns(3)

with mcol2:
    st.write("360° view of HCPs and their patient from data beyond ICD codes and Rx scripts")
    st.image("figures/HCP.png", width=200)
    st.write("HCPs as individual human beings ")

mcol1, mcol2, mcol3 = st.columns(3)

with mcol1:
    st.markdown("### Digital Behavior")
    st.markdown("""
                - Web
                - Search
                - Digital media
                - CRM
                - Engagement
                - Conversation
                """)

with mcol3:
    st.markdown("### SDOH Data")
    st.markdown("""
                - Demographics
                - Career stage
                - Affiliation
                - Role in practice
                - Finance 
                - Engagement preference (direct mail, email, F2F)
                - Digital channel preference
                - Confidence in using technology
                - Interests and attitudes towards travel
                """)

st.write("")
st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")