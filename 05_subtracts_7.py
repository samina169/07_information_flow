import streamlit as st

# Title of the app
st.title("Subtract 7 from a Number")

# Add a description
st.write("This app subtracts 7 from the number you provide.")

# Input for the user to enter a number
number = st.number_input("Enter a number:")

# Check if the user has entered a number
if st.button("Subtract 7"):
    result = number - 7
    st.write(f"The result of subtracting 7 from {number} is: {result}")
