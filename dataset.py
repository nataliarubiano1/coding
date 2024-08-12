import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
path= os.getcwd()
print(path)
files = os.listdir()
file_name= [x for x in files if 'Cost' in x][0]
print(file_name)
##--FIGURA1--##

#Lectura del dataset y sacar valores clave
csv = pd.read_csv(os.path.join(path,file_name), sep = ",")
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
plt.xlabel("Country", fontsize=14)
plt.ylabel("Average Cost of Living Index", fontsize=14)
plt.title("Top 10 Countries by Cost of Living Index",fontsize=16, weight='bold')
plt.xticks(rotation=45, ha="right",fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7) 
plt.tight_layout() 
plt.text(
    x=5, y=90, 
    s="Aca se presencia los 10 países con el promedio más alto de índice de costo de vida", 
    ha='center', va='bottom', fontsize=12, color="black", fontweight = "bold"
)
plt.tight_layout()
plt.show()


##--FIGURA2--## (No es necesario volver a leer si ya esta en el ambiente el dataframe)
#Prepara y organiza la visualizacion de los datos 
dataframe2 = pd.DataFrame(csv[["Country", "Groceries Index"]])
pais = dataframe2["Country"].value_counts().head()
alimentos = dataframe2["Groceries Index"].value_counts().head()
alimentos_pais = dataframe2.groupby("Country")["Groceries Index"].mean()

#Creacion de la grafica
plt.subplot(1,2,1)
#alimentos.plot(kind="pie", autopct = "%1.01f%%", labels = pais.index)
plt.pie(
    alimentos, 
    autopct="%1.1f%%",
    labels= pais.index,
    colors= sns.color_palette('Set2', n_colors=len(pais.index))
)
plt.title("Alimentos")
plt.tight_layout()
plt.text(
    x=4, y=.3, 
    s="En cambio acá, se puede ver el porcentaje de \nindices de comestibles de ciertos paises", 
    ha='center', va='top', fontsize=12, color="black", fontweight="bold"
)
plt.show()


##--FIGURA3--##

df=csv.copy()

#variables
costo = df["Cost of Living Index"]
renta = df["Rent Index"]
costo_renta = df["Cost of Living Plus Rent Index"]
restaurante = df["Restaurant Price Index"]
local = df["Local Purchasing Power Index"]

#ajsutes de graficas
plt.style.use("ggplot")
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10,8))
plt.subplots_adjust(wspace=0.5)
ax1.barh(costo, renta, color='skyblue')
ax1.set_title("Indice de costo/renta de vida", fontsize=14, weight='bold')

ax2.scatter(renta, local, color='orange')
ax2.set_xlabel("Renta", fontsize=12)
ax2.set_ylabel("Compra Locales", fontsize=12)
ax2.set_title("Renta y compras locales", fontsize=14, weight='bold')

print(local)
print(costo)
sns.scatterplot(x=local,y=costo, ax= ax3, palette='Set2')
ax3.set_xlabel("Country", fontsize=12)
ax3.set_ylabel("Compras Locales", fontsize=12)
ax3.set_title("Compras Locales",fontsize=14, weight='bold')
plt.figtext(
    x=0.5, y=-0.1, 
    s="Finalizando las graficas, esto es un promedio de lo que se gastaria en diferentes ocasiones", 
    ha='center', va='top', fontsize=12, color="black", fontweight = "bold",
    bbox=dict(facecolor='white', alpha=0.5)
)
plt.tight_layout()
plt.show()

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
