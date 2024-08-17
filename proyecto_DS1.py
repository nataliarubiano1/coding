import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D
import numpy as np
import seaborn as sns
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")
path = os.getcwd()
print(path)
documentos = os.listdir()
doc_name = [x for x in documentos if "Wine" in x][0]

csv = pd.read_csv(os.path.join(path, doc_name), sep = ",")
df = pd.DataFrame(csv)

#Variables
acido_citrico = csv["citric acid"]
libre_sulfuro = csv["free sulfur dioxide"]
alcohol = csv["alcohol"]
calidad = csv["quality"]
total_sulfuro = csv["total sulfur dioxide"]

#figura1
plt.figure(figsize=(10,6))
#barra = df.groupby("quality").mean().reset_index()
sns.boxplot(data=df, x="quality", y='citric acid', hue="quality", palette="viridis")
plt.title("Distribucion de Acido Citrico", fontsize = 14)
plt.xlabel("Calidad", fontsize = 14)
plt.ylabel("Acido Citrico (promedio)", fontsize = 14)
plt.show()

#figura2
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x=libre_sulfuro, y=total_sulfuro)
plt.xlim(0,60)
plt.ylim(0,100)
plt.title("Productos Libres de Dioxido de azufre VS Productos y Totalidad de Azufre", fontsize = 14)
plt.xlabel("Libre de Dioxido de Azufre",fontsize = 14)
plt.ylabel("Total Dioxido de Azufre", fontsize=14)
plt.grid(True)
plt.show()

#figura3
figura = plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="alcohol", y='fixed acidity', hue="quality")
plt.title("Distribucion de Alcohol vs Acidez", fontsize = 14)
plt.xlabel("Alcohol", fontsize = 14)
plt.ylabel("Acidez", fontsize = 14)
plt.show()