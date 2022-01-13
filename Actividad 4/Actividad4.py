# Actividad 4 patrones con K-Means
#Alison Magie Yáñez Dávila A01423011

#INSTRUCCIONES
#   -Carga tus datos
#   -Selecciona dos variables que consideres interesantes para este análisis.
#   -Determina un valor de k de acuerdo a los datos que tienes, las variables y una pregunta que quieres contestar con este análisis.
#   -Utilizando scikitlearn calcula los centros del algoritmo k-means

#Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Lectura de archivo csv haciendo uso de pandas
file='waterquality.csv'
df= pd.read_csv(file,encoding='latin1')
df=df.dropna(axis=0,how='any')

test=df[["BOD","NITRATE_N_NITRITE_N"]]
test=test.dropna(axis=0,how='any')

#Centroides
print("Centroides")
kmeans= KMeans (n_clusters=4).fit(test)
centroids=kmeans.cluster_centers_
print(centroids)

#Predicciones 
cla=kmeans.predict(test)

print("\nKMeans")
data={'BOD':[7],'NITRATE_N_NITRITE_N':[50]}
newdf=pd.DataFrame(data)
print(kmeans.predict(newdf))

plt.scatter(df["BOD"],df["NITRATE_N_NITRITE_N"],s=7, c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0],centroids[i][1],marker="o",c="red")

#Diseño
plt.title("gráfica 1 K-Means")
plt.xlabel("BOD")
plt.ylabel("NITRATE_N_NITRITE_N")


#Despliegue
plt.show()


