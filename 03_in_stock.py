import streamlit as st

# Title of the app
st.title("In Stock Checker")

# Add a description
st.write("This app checks if an item is in stock.")

# Input for the user to enter the item name
item_name = st.text_input("Enter the item name:")

# Input for the user to enter the stock quantity
stock_quantity = st.number_input("Enter the stock quantity:", min_value=0)

# Check if the item is in stock
if st.button("Check Stock"):
    if stock_quantity > 0:
        st.write(f"The item '{item_name}' is in stock with {stock_quantity} units available.")
    else:
        st.write(f"The item '{item_name}' is out of stock.")
