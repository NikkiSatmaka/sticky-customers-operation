#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image

TITLE = 'Sticky Customers Operation'
logo = Image.open('assets/sticky-notes.jpg')

st.set_page_config(
    page_title = f"Home - {TITLE}",
    page_icon='📞',
    menu_items={
        'Get Help': 'https://github.com/NikkiSatmaka',
        'Report a bug': 'https://github.com/NikkiSatmaka',
        'About': '# Sticky Customers Operation',
    }
)

# credit for source image

# Title of the main page
col1, col2 = st.columns(2)
with col1:
    st.image(logo, width=300)
with col2:
    st.title(TITLE)

st.header('Introduction')

st.markdown(
    """
    We strive to be the best telecommunication service provider in the world.
    In doing so, we strive to always improve our services to the best of our ability.

    Therefore, we conduct analysis of our customers' needs and provide the best possible service to them.
    We found that some of our customers are not satisfied with our services, which ended up in them stopping using our services.

    This **Sticky Customers Operation** is conducted to find out what we could improve on our services to make them better, by
    finding out what our customers are not satisfied with.

    Therefore, we will contact these dissatisfied customers, and ask them to provide us with feedback on what we can improve on.
    We will attempt to retain them as customers for as long as possible and make them sticky customers.

    Using our state-of-the-art technology, we will be able to easily find which customers are more likely to stop using our services.
    You can start by contacting these customers first.

    Simply navigate to the [Prediction](/Prediction) page using the sidebar on the left and input the information related to the customers.
    You will then find out which customers to contact.

    So what are you waiting for?
    Go to the [Prediction](/Prediction) page and start predicting!
    Ask for feedback and make our customers stick!
    """,
    unsafe_allow_html=True
)

expander = st.expander('Show the informations you need to input to predict')
expander.markdown(
    """
    - Customer's Basic Info
        1. Gender
        1. Senior Citizen
        1. Partner Status
        1. Dependents
        1. Tenure

    - Base Services
        1. Phone Service
        1. Multiple Lines
        1. Internet Service

    - Additional Internet Services
        1. Online Security
        1. Online Backup
        1. Device Protection
        1. Tech Support 
        1. Streaming TV
        1. Streaming Movies

    - Contract Details
        1. Contract Type
        1. Paperless Billing
        1. Payment Method
        1. Monthly Charges
        1. Total Charges
    """
)
