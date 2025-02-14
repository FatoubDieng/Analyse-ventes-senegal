# Importation des bibliothèques
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.show()
print(" Le script a bien démarré !")


#  Chargement des données
df = pd.read_csv("ventes_senegal.csv")

#  Afficher les premières lignes
print(" Aperçu du dataset :")
print(df.head())

#  Vérifier les informations du dataset
print("\n Infos du dataset :")
print(df.info())

# Vérifier les valeurs manquantes
print("\n Valeurs manquantes :")
print(df.isnull().sum())

#  Statistiques générales
print("\n Statistiques générales :")
print(df.describe())

#  Analyse des ventes par produit
produits_top = df.groupby("Produit")["Total_Vente"].sum().sort_values(ascending=False)

#  Affichage des meilleures ventes
plt.figure(figsize=(10, 5))
sns.barplot(x=produits_top.index, y=produits_top.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("🔝 Meilleurs Produits en termes de Ventes")
plt.xlabel("Produit")
plt.ylabel("Total des Ventes (FCFA)")
plt.show()

# Analyse des ventes par région
regions_top = df.groupby("Region")["Total_Vente"].sum().sort_values(ascending=False)

#  Affichage des meilleures régions
plt.figure(figsize=(8, 4))
sns.barplot(x=regions_top.index, y=regions_top.values, palette="coolwarm")
plt.title("📍 Ventes par Région")
plt.xlabel("Région")
plt.ylabel("Total des Ventes (FCFA)")
plt.show()
