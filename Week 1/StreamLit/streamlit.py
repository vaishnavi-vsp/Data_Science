import streamlit as st
from PIL import Image

# Headings
st.title("First Streamlit Website")
st.header("Data Science Program")
st.subheader("2022")

# text
st.text("This is a sample text")

# Markdowns
st.markdown("### This is a markdown")
st.markdown("## This is a markdown")
st.markdown("# This is a markdown")

# Success, Info, Error, Warning
st.success("Success")
st.info("Information")
st.error("Error")
st.warning("Warning")

# Display code in coding format
st.write(range(10))

# Image display
img = Image.open("st.jpeg")
st.image(img, width=300)

# Checkbox
if st.checkbox("Check?"):
    st.text("Checkbox checked")


# Radio Button
gender = st.radio("Select gender: ", ('Male', 'Female', 'Prefer not to say'))
if (gender == 'Male'):
    st.success("Male")
elif (gender == 'Female'):
    st.success("Female")
else:
    st.success("Prefer not to say")

# Selection Box
lang = st.selectbox("Languages: ", ['English', 'Hindi', 'Marathi', 'Gujarati'])
st.write("Your selected hobby is ", lang)

# Multiselection
langs = st.multiselect(
    "Languages: ", ['English', 'Hindi', 'Marathi', 'Gujarati'])
st.write("You selected ", len(langs), " languages")

# Buttons
if (st.button("Click Me")):
    st.text("Button Clicked")

# Text Inputs
name = st.text_input("Enter Your Name: ", "Type Here")
if (st.button("Submit")):
    result = name.title()
    st.success(result)

# Sliders
rating = st.slider("How much would you rate this product?", 1, 5)
st.text('Rating: {}'.format(rating))
