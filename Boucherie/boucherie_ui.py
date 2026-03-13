import streamlit as st

# Données de stocks
stocks_data = [
    {"product": "Boeuf", "quantity_kg": 20},
    {"product": "Porc", "quantity_kg": 15},
    {"product": "Agneau", "quantity_kg": 3},
    {"product": "Poulet", "quantity_kg": 10},
    {"product": "Veau", "quantity_kg": 2}
]

# Vérifier les stocks bas
low_stock_products = [item["product"] for item in stocks_data if item["quantity_kg"] < 5]

# Afficher l'alerte de stock bas si nécessaire
if low_stock_products:
    st.error("Alerte: Plusieurs produits sont en faible stock. Veuillez vérifier les quantités.")

st.title("Gestion des Stocks de la Boucherie")

st.subheader("Stocks Actuels")

# Afficher les stocks dans un tableau
st.table(stocks_data)
