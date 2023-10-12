from collections import namedtuple
import pandas as pd
import streamlit as st
from PIL import Image

image = Image.open('googles.png')

st.image(image, use_column_width=True)

st.write("""
# # TI Collector Web App :rage3: 

***
""")

st.header('Provide the TI Input Source')

source_input = "https://yourtisource.com\n"

ti = st.text_area("TI Source input", source_input, height=250)
ti = source_input.splitlines()
ti = '\n'.join(source_input) # Concatenates list to string

st.write("""
***
""")

st.header('Validate Input Sources')
ti
