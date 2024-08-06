import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

##--FIGURA1--##

#Lectura del dataset y sacar valores clave
csv = pd.read_csv("Cost_of_Living_Index_by_Country_2024.csv", sep = ",")
dataframe = pd.DataFrame(csv[["Rank", "Country", "Cost of Living Index"]])
rank = dataframe["Rank"].value_counts().head(10)
country = dataframe["Country"].value_counts().head(10)
vivienda_index = dataframe["Cost of Living Index"]

#Prepara la visualizacion de los datos
dataframe["Cost of Living Index"] = pd.to_numeric(dataframe["Cost of Living Index"], errors='coerce')
country_index = dataframe.groupby("Country")["Cost of Living Index"].mean()
top_10 = country_index.nlargest(10)

#Creacion de la grafica
plt.figure(figsize=(12, 8))
plt.bar(top_10.index, top_10.values, color='skyblue')
plt.xlabel("Country")
plt.ylabel("Average Cost of Living Index")
plt.title("Top 10 Countries by Cost of Living Index")
plt.xticks(rotation=45, ha="right")
plt.grid(True, linestyle='--', alpha=0.7) 
plt.tight_layout() 
plt.text(
    x=5, y=90, 
    s="Aca se presencia los 10 países con el promedio más alto de índice de costo de vida", 
    ha='center', va='bottom', fontsize=12, color="black", fontweight = "bold"
)
plt.show()


##--FIGURA2--##
csv = pd.read_csv("Cost_of_Living_Index_by_Country_2024.csv", sep = ",")
#Prepara y organiza la visualizacion de los datos 
dataframe2 = pd.DataFrame(csv[["Country", "Groceries Index"]])
pais = dataframe2["Country"].value_counts().head()
alimentos = dataframe2["Groceries Index"].value_counts().head()
alimentos_pais = dataframe2.groupby("Country")["Groceries Index"].mean()

#Creacion de la grafica
plt.subplot(1,2,1)
alimentos.plot(kind="pie", autopct = "%1.01f%%", labels = pais.index)
plt.title("Alimentos")
plt.tight_layout()
plt.text(
    x=4, y=.3, 
    s="En cambio acá, se puede ver el porcentaje de \nindices de comestibles de ciertos paises", 
    ha='center', va='top', fontsize=12, color="black", fontweight="bold"
)
plt.show()


##--FIGURA3--##

df=pd.read_csv("Cost_of_Living_Index_by_Country_2024.csv")

#variables
costo = df["Cost of Living Index"]
renta = df["Rent Index"]
costo_renta = df["Cost of Living Plus Rent Index"]
restaurante = df["Restaurant Price Index"]
local = df["Local Purchasing Power Index"]

#ajsutes de graficas
plt.style.use("ggplot")
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10,8))
plt.subplots_adjust(wspace=.5)
ax1.barh(costo, renta)
ax1.set_title("Indice de costo/renta de vida")
ax2.scatter(renta, local)
ax2.set_title("Renta y compras locales")
ax3 = sns.barplot(local)
ax3.set_title("Compras Locales")
plt.text(
    x=-120, y=-16, 
    s="Finalizando las graficas, esto es un promedio de lo que se gastaria en diferentes ocasiones", 
    ha='center', va='top', fontsize=12, color="black", fontweight = "bold"
)

#gastos variados
fig, ax1 = plt.subplots(figsize= (12,10))
left, bottom, width, height = [0.6, 0.2, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax1.barh(costo, renta)
ax2.scatter(restaurante, local, color = "blue")
plt.text(
    x=4, y= 600, 
    s="Se ven dos graficas. \nUna donde se ve un promedio entre los gastos en restaurantes \ny las compras locales (azul). \nEn cambio la otra grafica se ve un promedio entre el costo y la renta", 
    ha='center', va='top', fontsize=12, color="black", fontweight="bold"
)
plt.show()
