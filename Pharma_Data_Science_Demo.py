import streamlit as st

def run():
    st.set_page_config(
        page_title="Pharma Data Science App",
        page_icon="🩺",
        initial_sidebar_state="expanded"
    )

    st.sidebar.success("Select a demo above.")

    st.title("Pharma Data Science Tools")
    st.markdown(""" #### © 2022 Xinjie Qiu℠""")
    st.write("")
    st.write("")

    mcol1, mcol2, mcol3 = st.columns(3)

    with mcol1:
        st.markdown("""##### Market share trend""")
        st.image("figures/marketshare.png", width=160)

    with mcol2:
        st.markdown("""##### Channel optimization""")
        st.image("figures/channel.png", width=220)

    with mcol3:
        st.markdown("""##### HCP referral network""")
        st.image("figures/hcp_network.png", width=170)


    mcol1, mcol2, mcol3 = st.columns(3)

    with mcol1:
        st.markdown("""##### Line of therapies""")
        st.image("figures/LOT.png", width=180)

    with mcol2:
        st.markdown("""##### Medication persistence""")
        st.image("figures/persistence.png", width=200)

    with mcol3:
        st.markdown("""##### Diagnosis journey""")
        st.image("figures/journey_diagnosis.png", width=180)

    st.write("")
    st.write("")
    st.write("")
    st.markdown("""
                **👈 Select a demo from the sidebar** to see some examples
                of what the Pharma Data Science Tools can do!
                """)

if __name__ == "__main__":
    run()