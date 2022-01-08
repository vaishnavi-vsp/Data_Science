import streamlit as st

st.title("BMI Calculator")
weight = st.number_input("Enter your weight in kilograms:")
htm = st.radio("Select your height metric format: ", ("cm", "metres", "feet"))
if (htm == "cm"):
    height = st.number_input('Height in cms')
    try:
        bmi = weight/((height/100)**2)
    except:
        st.error("Please enter some value for height")

elif (htm == "metres"):
    height = st.number_input('Height in metres')
    try:
        bmi = weight/(height**2)
    except:
        st.error("Please enter some value for height")

else:
    height = st.number_input('Height in feet')
    try:
        bmi = weight/((height/3.28)**2)
    except:
        st.error("Please enter some value for height")

if (st.button("Calculate BMI")):
    st.write('Your BMI index is: {}'.format(bmi))

    if (bmi < 16):
        st.error("You're severely underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You're underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("You're healthy!")
    elif (bmi >= 25 and bmi < 30):
        st.warning("You're overweight")
    elif(bmi >= 30):
        st.error("You're severely overweight")
