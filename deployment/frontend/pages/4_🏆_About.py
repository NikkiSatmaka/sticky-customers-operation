#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image

TITLE = "About Me"

# variables
profile = Image.open("assets/profile.png")
github_img = Image.open("assets/github-logo.png")
linkedin_img = Image.open("assets/linkedin-logo.png")
instagram_img = Image.open("assets/instagram-logo.png")
stsi_book_img = Image.open("assets/stsi-book.png")

github_url = "[GitHub](https://github.com/NikkiSatmaka)"
linkedin_url = "[LinkedIn](https://www.linkedin.com/in/nikkisatmaka/)"
instagram_url = "[Instagram](https://www.instagram.com/nikkisatmaka/)"
book_url = "[Grab My book on Tokopedia](https://www.tokopedia.com/ryanfilbertofficial/buku-simple-trading-simple-investing)"


st.set_page_config(
    page_title = f"{TITLE}",
    page_icon='📞',
    menu_items={
        'Get Help': 'https://github.com/NikkiSatmaka',
        'Report a bug': 'https://github.com/NikkiSatmaka',
        'About': '# Customer Retainer Operation',
    }
)

# Title of the main page
st.title(TITLE)

col1, col2 = st.columns(2)
col1.image(profile, width=300)

col2.markdown(
    """
    I'm Nikki Satmaka, a Data Scientist, Financial Market Practitioner and Analyst,
    Quantitave Finance Enthusiast. I'm a Co-Author of "Simple Trading Simple Investing"
    together with Ryan Filbert's Team.

    I can help you provide insights from data especially regarding the financial markets.
    This app is a sample portfolio of mine to display what you can do with data, computer,
    and a bit of imagination.
    """
)

st.markdown("--------------------")
st.markdown("Connect with me on")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image(github_img, width=50)
    st.markdown(github_url, unsafe_allow_html=True)

with col2:
    st.image(linkedin_img, width=50)
    st.markdown(linkedin_url, unsafe_allow_html=True)

with col3:
    st.image(instagram_img, width=50)
    st.markdown(instagram_url, unsafe_allow_html=True)

with col4:
    st.image(stsi_book_img, width=50)
    st.markdown(book_url, unsafe_allow_html=True)