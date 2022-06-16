#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image

TITLE = "Customer Behaviour Analysis"

img_laptop = Image.open('assets/laptop-analyze.jpg')

st.set_page_config(
    page_title = f"{TITLE}",
    page_icon='📞',
    menu_items={
        'Get Help': 'https://github.com/NikkiSatmaka',
        'Report a bug': 'https://github.com/NikkiSatmaka',
        'About': '# Customer Retainer Operation',
    }
)

col1, col2 = st.columns(2)
with col1:
    st.title(TITLE)
with col2:
    st.image(img_laptop, width=300)

st.markdown("## The big picture")
st.image(
    'assets/eda/churn-total-bar.png',
    caption='customers who churn'
)
st.markdown(
    """
    The above bar chart shows the total number of customers who have stopped
    their subscription.
    It shows that most of the customers are satisfied with our services, as 
    most of them are not going to stop their subscription.
    """
)

st.markdown("## Customers who subscribe to the phone service")
col1, col2 = st.columns(2)
with col1:
    st.image(
        'assets/eda/phone-total.png',
        caption='customers who subscribe to the phone service'
    )
    st.markdown(
        """
        The above bar chart shows the total number of customers who have subscribed
        to the phone service. Clearly 90% use a phone service.
        """
    )

with col2:
    st.image(
        'assets/eda/phone-internet-total.png',
        width=280,
        caption='customers who subscribe to the phone service and internet'
    )
    st.markdown(
        """
        Grouping them furher by internet services, we can see that all customers
        who do not have a phone service, subscribe to the DSL internet.
        """
    )

st.markdown("## Chance of customers with an internet service stopping their subscription")
st.image(
    'assets/eda/internet-churn-chance.png',
    width=300,
    caption='chances of customers who have an internet service stopping their subscription'
)
st.markdown(
    """
    Customers who uses Fiber Optic Internet Service are more likely to stop their subscription.
    """
)

st.markdown("## Customers according to their contract details")
st.image(
    'assets/eda/contract-total-bar.png',
    caption='customers according to their contract details'
)
st.markdown(
    """
    We can see here that most customers are on a month-to-month contract.
    They also mostly have paperless billing.
    The most common payment method is electronic check.
    """
)

st.markdown("## Chance of customers stopping their subscription according to their contract details")
st.image(
    'assets/eda/contract-churn-chance.png',
    caption='chances of customers stopping their subscription according to their contract details'
)
st.markdown(
    """
    Customers who are on a month-to-month contract are more likely to stop their subscription.
    So are customers who have paperless billing and pay by electronic check.
    """
)

st.markdown("## Customers according to how long they have been with us")
st.image(
    'assets/eda/tenure-churn.png',
    caption='customers according to how long they have been with us'
)
st.markdown(
    """
    We can see that customers who have been with us for less than a year are more likely to stop their subscription.
    Meanwhile, customers who have been with us for more than a year are more likely to stay with us.
    """
)