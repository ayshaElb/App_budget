# Pilotage Budget V3

**Pilotage Budget V3** est une application web interactive construite avec [Streamlit](https://streamlit.io/) pour gérer et suivre votre budget de manière simple et visuelle. Elle vous permet de répartir vos revenus en différentes "enveloppes" budgétaires et de suivre vos dépenses au quotidien pour éviter les dépassements.

## ✨ Fonctionnalités Principales

- **Configuration Prévisionnelle** : Définissez votre revenu mensuel total et ajustez facilement la répartition en % de vos enveloppes (Dépenses fixes, Variables, Épargne, Loisirs) grâce aux curseurs interactifs.
- **Pilotage Visuel (Dashboard)** : Suivez en temps réel l'état de chaque enveloppe (montant max, montant consommé, reste à dépenser) avec des barres de progression visuelles.
- **Saisie des Dépenses (Réel)** : Enregistrez rapidement vos achats et catégorisez-les dans les enveloppes correspondantes.
- **Historique** : Visualisez l'intégralité de vos transactions sur une table dynamique (possibilité de la réinitialiser au besoin).
- **Sauvegarde Continue** : Vos données (revenus, configuration, historique) sont sauvegardées localement au sein d'un fichier JSON (`mon_budget_complet.json`).

## 🛠️ Prérequis et Installation

Assurez-vous d'avoir Python d'installé. Vous aurez ensuite besoin des bibliothèques suivantes pour faire tourner le script :

- `streamlit`
- `pandas`

Vous pouvez les installer en utilisant `pip` directement depuis votre terminal :

```bash
pip install streamlit pandas
```

## 🚀 Démarrer l'application

Une fois les dépendances installées, ouvrez un terminal depuis le dossier contenant le fichier `app_budgetV3.py` et tapez la commande suivante :

```bash
streamlit run app_budgetV3.py
```

L'application web s'ouvrira automatiquement dans votre navigateur par défaut (en général sur le port `localhost:8501`).

## 📂 Gestion des données

Lors de la première utilisation, un fichier nommé `mon_budget_complet.json` sera généré automatiquement à la racine de votre dossier. Il contient toutes vos configurations et votre historique de transactions. 
*(Astuce : Si le total de votre répartition est différent de 100%, l'application vous affichera un message d'alerte dans le menu latéral).*
