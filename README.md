# Pilotage Budget V4

Bienvenue dans la **V4** de votre application de pilotage de budget personnel. Cette nouvelle version a été entièrement repensée et développée avec **Streamlit**, offrant une interface web moderne, dynamique et professionnelle.

## 🌟 Nouveautés de la V4

La V4 marque un tournant majeur par rapport aux versions précédentes sur Excel en introduisant une automatisation complète basée sur un système de grand livre (Ledger).

- **Interface Professionnelle** : Un design épuré, des polices modernes (Inter), et des cartes KPI dynamiques.
- **Automatisation Totale (Ledger)** : Vous ne remplissez plus la colonne "Réel" manuellement. Toutes les dépenses et revenus saisis dans le **Journal des Transactions** mettent à jour automatiquement vos tableaux de budget (Revenus, Dépenses, Épargnes, etc.).
- **Gestion Historique des Mois** : Créez de nouveaux mois, archivez les anciens et naviguez facilement dans votre historique sans perdre vos prévisions d'un mois à l'autre.
- **Sauvegarde Locale** : Toutes vos données sont sauvegardées de manière sécurisée et structurée dans le fichier `mon_budget_complet.json`.
- **Suivi Santé & Comptes** : Des modules dédiés pour le suivi de vos frais de santé avancés et le solde de vos différents comptes bancaires.

## 🛠️ Prérequis

Assurez-vous d'avoir Python installé sur votre machine. Ensuite, installez les dépendances nécessaires en exécutant la commande suivante dans votre terminal :

```bash
pip install streamlit pandas
```

## 🚀 Lancer l'Application

Pour démarrer votre tableau de bord, ouvrez un terminal dans le dossier du projet (`MonBudget`) et exécutez la commande :

```bash
streamlit run budget.py
```

L'application s'ouvrira automatiquement dans votre navigateur web.

## 📖 Guide d'Utilisation

1. **Prévisions** : En début de mois, remplissez la colonne "Prévu" pour vos revenus, dépenses fixes, variables, épargnes et dettes dans les tableaux correspondants.
2. **Journal des Transactions (Le Cerveau)** : Au fil du mois, ajoutez chaque entrée d'argent ou dépense dans le **Journal des transactions** en bas de page. 
   - *Important* : Sélectionnez bien la catégorie globale et la sous-catégorie pour que le montant s'impute correctement dans les tableaux supérieurs.
3. **Clôture et Nouveau Mois** : À la fin du mois, utilisez le bouton "➕ Clôturer et démarrer un nouveau mois" en haut de la page. Cela créera une copie de vos prévisions actuelles pour le nouveau mois, tout en remettant à zéro les montants réels et le journal.

## 📁 Structure du Projet

- `budget.py` : Le script principal contenant toute la logique et l'interface utilisateur Streamlit.
- `mon_budget_complet.json` : Votre base de données locale (générée automatiquement au premier lancement si elle n'existe pas). **Pensez à faire des sauvegardes régulières de ce fichier.**

---
*Développé pour un suivi financier serein et automatisé.*
