import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Diagnosis Journey", page_icon="🩺")
st.sidebar.header("Patient Diagnosis Journey Analysis")

st.title("Patient Diagnosis Journey Analysis")
st.write(
    """This demo illustrates a patient diagnosis journey from a mock anonymous sample data. Enjoy!"""
)


df_medical = pd.read_csv("data/Medical.csv")

df_medical_diagnosis = pd.melt(df_medical.loc[:,:"DIAGNOSIS_E_CODE_2"],
                          id_vars=["Patient_ID","CLAIM_DATE"],
                          value_vars=['DA', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
                                      'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16',
                                      'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24',
                                      'D25', 'D26','DIAGNOSIS_E_CODE_1', 'DIAGNOSIS_E_CODE_2'],
                          value_name="CODE")[["Patient_ID","CLAIM_DATE","CODE"]].dropna()

df_diagnosis_code = pd.read_csv("data/Diagnosis.csv")
df_patient_diagnosis = df_medical_diagnosis.merge(df_diagnosis_code[['CODE', 'CODE_DESCRIPTION']],
                                                  on="CODE")

df_patient_diagnosis["Code and Description"] = df_patient_diagnosis['CODE'] + " " + df_patient_diagnosis['CODE_DESCRIPTION']

diagnosis_selected = st.multiselect("Which diagnosis code(s)",
                                    df_patient_diagnosis['Code and Description'].value_counts().index.tolist(),
                                    ["L40 Psoriasis",
                                     "L400 Psoriasis vulgaris",
                                     "L401 Generalized pustular psoriasis",
                                     "L402 Acrodermatitis continua",
                                     "L403 Pustulosis palmaris et plantaris",
                                     "L404 Guttate psoriasis",
                                     # "L405 Arthropathic psoriasis",
                                     "L4050 Arthropathic psoriasis, unspecified",
                                     "L4051 Distal interphalangeal psoriatic arthropathy",
                                     "L4052 Psoriatic arthritis mutilans",
                                     "L4053 Psoriatic spondylitis",
                                     "L4054 Psoriatic juvenile arthropathy",
                                     "L4059 Other psoriatic arthropathy",
                                     "L408 Other psoriasis",
                                     "L409 Psoriasis, unspecified"
                                     ])


patient_id = st.selectbox(
    'Which patient?',
    df_patient_diagnosis[df_patient_diagnosis["Code and Description"].isin(diagnosis_selected)][["Patient_ID", "CODE"]]
    .groupby("Patient_ID")
    .count()
    .sort_values('CODE', ascending=False).index.tolist()
)

patient_selected = df_patient_diagnosis[(df_patient_diagnosis["Patient_ID"] == patient_id) &
                                        (df_patient_diagnosis["Code and Description"].isin(diagnosis_selected))
                                        ]

c = alt.Chart(patient_selected).mark_circle(size=100).encode(
    x=alt.X('CLAIM_DATE:T', axis=alt.Axis(labelAngle=90)),
    y=alt.Y('CODE:N'),
    color='CODE'
).properties(
    width=650,
    height=600
)
st.altair_chart(c, use_container_width=True)

with st.expander("See the journey data"):
    st.table(patient_selected.sort_values('CLAIM_DATE', ascending=True))

st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")