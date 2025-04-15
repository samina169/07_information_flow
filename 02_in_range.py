import streamlit as st

# Title of the app
st.title("In Range Checker")

# Add a description
st.write("This app checks if a number is within a specified range.")

# Input for the user to enter a number
number = st.number_input("Enter a number:")

# Define the range
lower_bound = 1
upper_bound = 100

# Check if the number is in range
if st.button("Check"):
    if lower_bound <= number <= upper_bound:
        st.write(f"The number {number} is within the range of {lower_bound} to {upper_bound}.")
    else:
        st.write(f"The number {number} is outside the range of {lower_bound} to {upper_bound}.")
