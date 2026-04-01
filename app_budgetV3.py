import streamlit as st
import json
import os
import pandas as pd

# --- CONFIGURATION ---
FICHIER_DONNEES = "mon_budget_complet.json"

# --- FONCTIONS DE SAUVEGARDE ---
def charger_tout():
    if os.path.exists(FICHIER_DONNEES):
        with open(FICHIER_DONNEES, "r", encoding="utf-8") as f:
            return json.load(f)
    # Valeurs par défaut si le fichier n'existe pas
    return {
        "revenu": 2000.0,
        "repartition": {"Fixe": 50, "Variable": 30, "Épargne": 10, "Loisirs": 10},
        "transactions": []
    }

def sauvegarder_tout(data):
    with open(FICHIER_DONNEES, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# --- INITIALISATION ---
if 'data' not in st.session_state:
    st.session_state.data = charger_tout()

st.set_page_config(layout="wide", page_title="Pilotage Budget V3")

# --- BARRE LATÉRALE : CONFIGURATION PRÉVISIONNELLE ---
with st.sidebar:
    st.header("🎯 Prévisionnel Mensuel")
    
    # Mise à jour du revenu
    st.session_state.data["revenu"] = st.number_input(
        "Revenu total (€)", 
        min_value=0.0, 
        value=float(st.session_state.data["revenu"])
    )
    
    st.subheader("Répartition des enveloppes (%)")
    # Sliders pour chaque catégorie
    for cat in st.session_state.data["repartition"]:
        st.session_state.data["repartition"][cat] = st.slider(
            f"{cat} (%)", 0, 100, st.session_state.data["repartition"][cat]
        )
    
    total_p = sum(st.session_state.data["repartition"].values())
    if total_p != 100:
        st.warning(f"Attention : Total = {total_p}% (doit faire 100%)")
    
    if st.button("💾 Sauvegarder la configuration"):
        sauvegarder_tout(st.session_state.data)
        st.success("Configuration enregistrée !")

# --- CALCUL DES ENVELOPPES ---
rev = st.session_state.data["revenu"]
enveloppes_montant = {
    cat: rev * (pct / 100) 
    for cat, pct in st.session_state.data["repartition"].items()
}

# --- INTERFACE PRINCIPALE ---
st.title("💰 Suivi Budgétaire : Prévisionnel vs Réel")

# Formulaire d'ajout de dépense
with st.expander("➕ Ajouter une dépense réelle", expanded=False):
    c1, c2, c3 = st.columns(3)
    with c1: nom_dep = st.text_input("Désignation")
    with c2: prix_dep = st.number_input("Montant (€)", min_value=0.0, step=1.0)
    with c3: cat_dep = st.selectbox("Catégorie", list(enveloppes_montant.keys()))
    
    if st.button("Enregistrer l'achat"):
        if nom_dep and prix_dep > 0:
            nouvelle = {"nom": nom_dep, "prix": prix_dep, "categorie": cat_dep}
            st.session_state.data["transactions"].append(nouvelle)
            sauvegarder_tout(st.session_state.data)
            st.rerun()

# --- DASHBOARD DE PILOTAGE ---
st.divider()
cols = st.columns(len(enveloppes_montant))

df_trans = pd.DataFrame(st.session_state.data["transactions"])

for i, (cat, budget_max) in enumerate(enveloppes_montant.items()):
    # Calcul du réel consommé
    if not df_trans.empty:
        consomme = df_trans[df_trans['categorie'] == cat]['prix'].sum()
    else:
        consomme = 0
    
    reste = budget_max - consomme
    ratio = min(consomme / budget_max, 1.0) if budget_max > 0 else 0
    
    with cols[i]:
        st.metric(label=cat, value=f"{consomme:.2f} €", delta=f"{reste:.2f} € restants")
        # Changement de couleur de la barre si dépassement
        couleur = "normal" if reste >= 0 else "inverse"
        st.progress(ratio)
        st.caption(f"Budget max : {budget_max:.0f} €")

# --- HISTORIQUE ---
if not df_trans.empty:
    st.divider()
    st.subheader("📝 Historique des transactions")
    st.dataframe(df_trans, use_container_width=True)
    if st.button("🗑️ Effacer tout l'historique"):
        st.session_state.data["transactions"] = []
        sauvegarder_tout(st.session_state.data)
        st.rerun()