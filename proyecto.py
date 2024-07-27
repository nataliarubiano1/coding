#TITULO: Tratados internacionales de colombia
#Fuente de datos: https://www.datos.gov.co/Estad-sticas-Nacionales/Tratados-internacionales-de-Colombia/fdir-hk5z/about_data
#Intro: Relaciona informacion detallada de tratados internacionales del pais con otros estados/paises internacionales
#Objetivo principal: Top 10 de los tratados que han tenido mas 'Potencia' con el pais


#Librerias
import pandas as pd
import os
import numpy as num
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

#Descripcion datasets

path = os.getcwd()
print(os.listdir())

documento = [x for x in os.listdir() if "Tratados_" in x]
#'Tratado' = Nombre del acuerdo internacional
documento

if len(documento) == 0:
    raise FileNotFoundError("Ningun documento con 'Tratados' ha sido encontrado")
elif len(documento) > 1:
    raise ValueError("Varios documentos con 'Tratados' han sido encontrados. Por favor espicificar su busqueda.")

file_path = os.path.join(path, documento[0])
df = pd.read_csv(file_path, sep = ",")

print(df.head())
print(df.shape)
print(df["Nombre del Tratado"].value_counts().head(10))

#Tabla de tratatados

df["Nombre del Tratado"].value_counts().head(10).plot(kind = "bar")
#"head" = Paises que esten dentro del top 10
plt.title('Top 10 Tratados')
plt.xlabel("Nombre de tratado")
plt.ylabel("Frecuencia")
plt.xticks(rotation = 45, ha="right")
plt.tight_layout()
plt.show()
df.columns
df["Fecha de Adopcion"].unique()
#'Fecha de adopcion'= Fecha en que el tratado fue adoptado o firmado

#filtracion/busqueda interes de datos

interes = input("Ingresa Nombre de Tratado: ").upper()
lista = set(df["Fecha de Adopcion"].unique())
try:
    filtracion = [x for x in lista if interes in x]
    if len(filtracion) > 0:
        print(filtracion)
        informacion = df[df["Nombre del Tratado"].isin(filtracion)]
        informacion
    else:
        print("No se encontró nada al respecto")
except:
    print("Error. No se encuentra lo que está buscando")