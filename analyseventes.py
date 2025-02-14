import pandas as pd  # Manipulation des données
import matplotlib.pyplot as plt  # Création de graphiques
import seaborn as sns  # Visualisation avancée

# Vérification du bon démarrage du script
print(" Le script a bien démarré !")

#  Chargement des données  
df = pd.read_csv("ventes_senegal.csv")  # Charge le fichier CSV

#  Aperçu des premières lignes  
print(" Aperçu du dataset :")
print(df.head())  # Affiche les 5 premières lignes

#  Informations sur le dataset  
print("\n Infos du dataset :")
print(df.info())  # Affiche les types de données et les valeurs manquantes

#  Vérification des valeurs manquantes  
print("\n Valeurs manquantes :")
print(df.isnull().sum())  # Compte les valeurs manquantes par colonne

#  Statistiques générales  
print("\n Statistiques générales :")
print(df.describe())  # Statistiques sur les colonnes numériques

# Analyse des ventes par produit  
produits_top = df.groupby("Produit")["Total_Vente"].sum().sort_values(ascending=False)
# Trie les produits du plus vendu au moins vendu

# Affichage des meilleures ventes par produit  
plt.figure(figsize=(10, 5))  # Définition de la taille du graphique
sns.barplot(x=produits_top.index, y=produits_top.values, palette="viridis")  # Graphique en barres
plt.xticks(rotation=45)  # Rotation des noms des produits
plt.title(" Meilleurs Produits en termes de Ventes")  # Titre du graphique
plt.xlabel("Produit")  # Étiquette axe X
plt.ylabel("Total des Ventes (FCFA)")  # Étiquette axe Y
plt.show()  # Affichage du graphique

#  Analyse des ventes par région  
regions_top = df.groupby("Region")["Total_Vente"].sum().sort_values(ascending=False)
# Trie les régions du plus vendu au moins vendu

#  Affichage des ventes par région  
plt.figure(figsize=(8, 4))
sns.barplot(x=regions_top.index, y=regions_top.values, palette="coolwarm")  # Graphique en barres
plt.title("Ventes par Région")
plt.xlabel("Région")
plt.ylabel("Total des Ventes (FCFA)")
plt.show()
