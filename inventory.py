import streamlit as st

st.title("Shampoo Inventory Management System")

# Product list and stock quantities (Cartons and Pieces)
products = [
    "BIO SHAMPOO FAMILY 720 ML", 
    "BIO SHAMPOO SMALL 130 ML", 
    "BIO ADVANCE ONION SHAMPOO 850 ML", 
    "BIO ADVANCE ALOE VERA SHAMPOO 850 ML", 
    "BIO ADVANCE ONION SHAMPOO SMALL 130 ML", 
    "BIO ADVANCE ALOE VERA SHAMPOO SMALL 130 ML"
]

cartons = [5, 10, 3, 4, 8, 6]
pieces = [12, 24, 6, 8, 15, 10]

# Display available stock
st.subheader("Current Stock Catalog")
for i in range(len(products)):
    st.write(f"• **{products[i]}** — Cartons: {cartons[i]} | Pieces: {pieces[i]}")

st.divider()

# Inputs to sell or process items
selected_product = st.text_input("Enter exact shampoo name to update:")
sell_ctn = st.number_input("Cartons to deduct:", min_value=0, step=1)
sell_pcs = st.number_input("Pieces to deduct:", min_value=0, step=1)

if st.button("Process Sale"):
    if selected_product in products:
        index = products.index(selected_product)
        
        # Check if we have enough cartons and pieces
        if cartons[index] >= sell_ctn and pieces[index] >= sell_pcs:
            cartons[index] -= sell_ctn
            pieces[index] -= sell_pcs
            st.success(f"Successfully updated stock for {selected_product}!")
        else:
            st.error("Not enough cartons or pieces available in stock!")
    else:
        st.error("Product not found! Please check the spelling.")

# Display updated inventory
st.subheader("Updated Inventory Status")
for i in range(len(products)):
    st.write(f"• **{products[i]}** — Cartons: {cartons[i]} | Pieces: {pieces[i]}")
