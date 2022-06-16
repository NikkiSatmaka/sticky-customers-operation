#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import requests
from PIL import Image

from packages.options import gender_options, no_yes_options
from packages.options import no_phone_service_options, no_internet_service_options
from packages.options import MultipleLines_options, InternetService_full_options
from packages.options import InternetService_reduced_options
from packages.options import Contract_options, PaymentMethod_options

TITLE = "Customer Behaviour Prediction"

sub1 = "Customer's Basic Info"
sub2 = "Base Services"
sub3 = "Additional Internet Services"
sub4 = "Contract Details"

msg_0_res = "There's a huge chance that this customer will stick with us."
msg_0_act = "That's great. Celebrate for a bit, then analyze the next customer."
msg_0_add = "Let's toast for this small win"
msg_1_res = "Uh-Oh!! It's highly likely that this customer won't stick!"
msg_1_act = "Stay calm. Contact them ASAP, find out what their concerns are, and make them stick!"
msg_1_add = "Here's a four-leaf clover for you"
msg_goodluck = "Good Luck!"

img_crystal = Image.open('assets/crystal-ball.jpg')
img_res_0 = Image.open('assets/toast-wine.jpg')
img_res_1 = Image.open('assets/four-leaf-clover.jpg')

SENIORCITIZEN_MAP = {"No": 0, "Yes": 1}

st.set_page_config(
    page_title = f"{TITLE}",
    page_icon='📞',
    menu_items={
        'Get Help': 'https://github.com/NikkiSatmaka',
        'Report a bug': 'https://github.com/NikkiSatmaka',
        'About': '# Sticky Customers Operation',
    }
)

# URL = "http://127.0.0.1:5000/predict"  # for testing
URL = "https://telco-churn-backend.herokuapp.com/predict"  # for deployment

col1, col2 = st.columns(2)
with col1:
    st.title(TITLE)
with col2:
    st.image(img_crystal, width=300)

st.subheader(sub1)

col1, col2 = st.columns(2)

with col1:
    gender = st.radio(
        "Gender",
        gender_options,
        index=0,
        help="Customer's Gender. Default is Female."
    )

    SeniorCitizen_key = st.radio(
        "Senior Citizen",
        no_yes_options,
        index=0,
        help="Is customer a Senior Citizen? 65 years old or older."
    )

    Partner = st.radio(
        "Partner Status",
        no_yes_options,
        index=0,
        help="Does customer have a partner?"
    )

with col2:
    Dependents = st.radio(
        "Dependents",
        no_yes_options,
        index=0,
        help="Does customer have dependents?"
    )

    tenure = st.number_input(
        "Tenure",
        min_value=0,
        max_value=120,
        value=0,
        step=1,
        help="Total number of months the customer has been subscribing."
    )

st.subheader(sub2)

col1, col2 = st.columns(2)

with col1:
    PhoneService = st.selectbox(
        "Phone Service",
        no_yes_options,
        index=0,
        help="Does customer have phone service?"
    )

    # switch options caused by the selection of PhoneService
    if PhoneService == "No":
        MultipleLines_options = no_phone_service_options
        InternetService_options = InternetService_reduced_options
    else:
        MultipleLines_options = no_yes_options
        InternetService_options = InternetService_full_options

    MultipleLines = st.selectbox(
        "Multiple Lines",
        MultipleLines_options,
        index=0,
        help="Does customer have multiple phone lines?"
    )

with col2:
    InternetService = st.selectbox(
        "Internet Service",
        InternetService_options,
        index=0,
        help="Does customer have internet service?"
    )

    # switch options caused by the selection of InternetService
    if InternetService == "No":
        AddInternetService_options = no_internet_service_options
    else:
        AddInternetService_options = no_yes_options

st.subheader(sub3)

col1, col2 = st.columns(2)

with col1:
    OnlineSecurity = st.selectbox(
        "Online Security",
        AddInternetService_options,
        index=0,
        help="Does customer have additional online security service?"
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        AddInternetService_options,
        index=0,
        help="Does customer have additional online backup service?"
    )

    DeviceProtection = st.selectbox(
        "Device Protection",
        AddInternetService_options,
        index=0,
        help="Does customer have additional device protection service?"
    )

with col2:
    TechSupport = st.selectbox(
        "Tech Support",
        AddInternetService_options,
        index=0,
        help="Does customer have additional tech support service?"
    )

    StreamingTV = st.selectbox(
        "Streaming TV",
        AddInternetService_options,
        index=0,
        help="Does customer use a third-party streaming TV service?"
    )

    StreamingMovies = st.selectbox(
        "Streaming Movies",
        AddInternetService_options,
        index=0,
        help="Does customer use a third-party streaming movies service?"
    )

st.subheader(sub4)

col1, col2 = st.columns(2)

with col1:
    Contract = st.selectbox(
        "Contract Type",
        Contract_options,
        index=0,
        help="What kind of contract does customer have?"
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        no_yes_options,
        index=0,
        help="Does customer choose paperless billing?"
    )

    PaymentMethod = st.selectbox(
        "Payment Method",
        PaymentMethod_options,
        index=0,
        help="How does customer pay?"
    )

with col2:
    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=1000.0,
        value=0.0,
        step=0.5,
        help="Monthly charges of customer."
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=MonthlyCharges,
        max_value=1000000.0,
        value=MonthlyCharges,
        step=0.5,
        help="Total charges of customer."
    )


# map the input data to the format that the backend expects
SeniorCitizen = SENIORCITIZEN_MAP[SeniorCitizen_key]

# store user input in a dictionary
data = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

col1, col2, col3 = st.columns(3)
with col2:
    predict = st.button("Predict")

with st.spinner('Predicting...'):
    # inferencing
    if predict:
        # communicate
        r = requests.post(URL, json=data)
        res = r.json()

        if r.status_code == 200:
            result = res['result']['class_name']
            if result == 'Not Churn':
                st.success(msg_0_res)
                st.subheader(msg_0_act)
                st.subheader(msg_goodluck)
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.write(msg_0_add)
                    st.image(img_res_0, width=300)
            else:
                st.warning(msg_1_res)
                st.subheader(msg_1_act)
                st.subheader(msg_goodluck)
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.write(msg_1_add)
                    st.image(img_res_1, width=300)

        elif r.status_code == 400:
            st.title("There's an error in the input data!")
            st.write(res['message'])