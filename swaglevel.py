from PIL import Image
import streamlit as st

"Behold. The greatest picture ever taken"
image = Image.open('Picture.jpg')
st.image(image, width=200,
         se_column_width=True)
