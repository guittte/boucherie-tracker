import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title("Mon Application Streamlit Propre et Sans HTML")

# Création de données d'exemple
data = {
    'Nom': [f'Produit {i}' for i in range(1, 11)],
    'Quantité': np.random.randint(10, 100, 10),
    'Prix': np.round(np.random.uniform(5.0, 150.0, 10), 2),
    'En Stock': np.random.choice([True, False], 10)
}
df = pd.DataFrame(data)

st.header("Affichage des données avec st.dataframe")
st.write("Ceci est un tableau interactif affichant toutes les données :")
st.dataframe(df)

st.header("Affichage des données avec st.table")
st.write("Ceci est un tableau statique affichant les 5 premières lignes :")
st.table(df.head(5))

st.header("Utilisation de st.columns pour la mise en page")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Section 1")
    st.write("Contenu pour la première colonne. Nous pouvons y mettre des widgets ou du texte.")
    st.metric(label="Ventes Aujourd'hui", value="1 200 €", delta="20 €")

with col2:
    st.subheader("Section 2")
    st.write("Contenu pour la deuxième colonne. Idéal pour organiser des éléments liés.")
    selected_product = st.selectbox("Sélectionnez un produit", df['Nom'].tolist())
    st.write(f"Vous avez sélectionné : {selected_product}")

with col3:
    st.subheader("Section 3")
    st.write("Contenu pour la troisième colonne. Parfait pour les informations complémentaires ou les graphiques.")
    st.progress(70)
    st.caption("Progression de la tâche")

st.header("Un exemple de graphique simple (optionnel)")
st.line_chart(df['Prix'])
st.write("Graphique des prix des produits.")

if st.button("Actualiser les données"):
    st.success("Les données ont été actualisées (logique non implémentée).")
