import streamlit as st
import requests

# Give the Name of the Application
st.title('Prediction Churn of Customer')

# Create Submit Form
with st.form(key='form_parameters'):
    s = st.sidebar.selectbox(label='SeniorCitizen', options=[0,1])
    d = st.sidebar.selectbox(label='Dependents', options=['No', 'Yes'])
    t = st.number_input('Tenure', min_value=0, step=1, max_value=73)
    ins = st.sidebar.selectbox(label='InternetService', options=['No','DSL','Fiber optic'])
    con = st.sidebar.selectbox(label='Contract', options=['Month-to-month','One year','Two year'])
    pm = st.sidebar.selectbox(label='PaymentMethod', options=['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
    mc = st.number_input('MonthlyCharges', min_value=18.25, step=0.05,max_value=118.75)
    tc = st.number_input('TotalCharges', min_value=18.8, step=0.02,max_value=8684.8)

    submitted = st.form_submit_button('Predict')

# inference
if submitted:
    URL = 'https://churn-model-rizqirizmayani.koyeb.app/predict'
    param = {'SeniorCitizen': s,
    'Dependents': d,
    'tenure': t,
    'InternetService': ins,
    'Contract': con,
    'PaymentMethod': pm,
    'MonthlyCharges': mc,
    'TotalCharges': tc}

    r = requests.post(URL, json=param)
    if r.status_code == 200:
        res = r.json()
        st.title('Telco Customer Churn is {}'.format(res['label_names']))
    else:
        st.title("Unexpected Error")
        st.write(r.status_code)
