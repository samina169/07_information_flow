import streamlit as st

# Title of the app
st.title("Multiple Returns Selector")

# Add some introductory text
st.write("This app allows you to select multiple return options.")

# Example of a multi-select box
options = st.multiselect(
    'Select return options:',
    ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
)

# Display the selected options
if options:
    st.write("You selected:")
    for option in options:
        st.write(f"- {option}")
else:
    st.write("No options selected.")
