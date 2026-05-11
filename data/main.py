
import pandas as pd 
import matplotlib.pyplot as plt 
pip install pandas matplotlib
# 1. Charger les données
df = pd.read_csv("data/data.csv")

# 2. Afficher les premières lignes
print("Aperçu des données :")
print(df.head())

# 3. Vérifier les valeurs manquantes
print("\nValeurs manquantes :")
print(df.isnull().sum())

# 4. Nettoyage (supprimer lignes avec NA)
df = df.dropna()

# 5. Statistiques descriptives
print("\nStatistiques descriptives :")
print(df.describe())

# 6. Comparaison par sexe
print("\nMoyennes par sexe :")
print(df.groupby("sexe").mean())

# 7. Graphique
df.boxplot(column="deplacements", by="sexe")
plt.title("Comparaison des déplacements selon le sexe")
plt.suptitle("")
plt.xlabel("Sexe")
plt.ylabel("Nombre de déplacements")
plt.show()

# 8. Sauvegarde des données propres
df.to_csv("results/data_clean.csv", index=False)

print("\nDonnées nettoyées sauvegardées !")