import streamlit as st

# Title of the app
st.title("Choosing Returns")

# Add some introductory text
st.write("This is a simple Streamlit app to choose returns.")

# Example of a selection box
option = st.selectbox(
    'Select a return option:',
    ('Option 1', 'Option 2', 'Option 3')
)

# Display the selected option
st.write(f'You selected: {option}')
