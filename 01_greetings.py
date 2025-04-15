import streamlit as st

# Title of the app
st.title("Greetings App")

# Add a greeting message
st.write("Hello! Welcome to the Greetings App.")

# Input for the user's name
name = st.text_input("Enter your name:")

# Display a personalized greeting if a name is provided
if name:
    st.write(f"Hello, {name}! It's great to see you!")
