# Obtención de estadísticas descriptivas
#Alison Magie Yáñez Dávila 

#Importando pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

####################################################################
#                     A c t i v i d a d  2
####################################################################
#INSTRUCCIONES
#Realizar un código que haga lo siguiente
#    -Carga de datos
#    -Mostrar número de variables y el número de registros
#    -Mostrar el nombre de las columnas
#    -Mostrar los tipos de datos
#    -Seleccionar dos columnas que al momento parezcan interesante
#    -Mostrar los valores únicos
#    -Mostrar los valores máximos y mínimos
#    -Mostrar la media, mediana y desviación estándar
#   

#Lectura de archivo csv haciendo uso de pandas
file='waterquality.csv'
df= pd.read_csv(file,encoding='latin1')

#Muestra de número de variables y número de registros
pd.set_option("display.max_rows",None,"display.max_columns",None)
print ("\nNumero de variables y registros") 
print(df.shape)

#Muestra del nombre de las columnas
print ("\nLista de nombre de columnas") 
print(df.columns)

#Muestra de tipos de datos
print ("\nTipos de datos")
print(df.dtypes)

#Columnas seleccionadas
print ("\nLas columnas seleccionadas para el siguiente analisis son:")

#########################
#       Columna 1
#########################
print ("\n#########################\n  TEMP  \n#########################")
columna1= df["TEMP"]
#Valores únicos
print("\nValores unicos")
print(columna1.unique())

#Media,mediana, desviación estandar
print("\nMedia")
print(columna1.mean())
print("\nMediana")
print( columna1.median())
print("\nDesviacion estandar")
print( columna1.std())

print("\nValor maximo")
print(columna1.max())
print("\nValor minimo")
print(columna1.min())

#########################
#       Columna 2
#########################
print ("\n#########################\n  DO  \n#########################")
columna2= df["DO"]
#Valores únicos
print("\nValores unicos")
print(columna2.unique())

#Media,mediana, desviación estandar
print("\nMedia")
print(columna2.mean())
print("\nMediana")
print( columna2.median())
print("\nDesviacion estandar")
print( columna2.std())

#Valor máximo y mínimo
print("\nValor maximo")
print(columna2.max())
print("\nValor minimo")
print(columna2.min())

#########################
#       Columna 3
#########################
print ("\n#########################\n  PH  \n#########################")
columna3= df["pH"]
#Valores únicos
print("\nValores unicos")
print(columna3.unique())

#Media,mediana, desviación estandar
print("\nMedia")
print(columna3.mean())
print("\nMediana")
print( columna3.median())
print("\nDesviacion estandar")
print( columna3.std())

#Valor máximo y mínimo
print("\nValor maximo")
print(columna3.max())
print("\nValor minimo")
print(columna3.min())

#########################
#       Columna 4
#########################
print ("\n#########################\n  Conductivity  \n#########################")
columna4= df["CONDUCTIVITY"]
#Valores únicos
print("\nValores unicos")
print(columna4.unique())

#Media,mediana, desviación estandar
print("\nMedia")
print(columna4.mean())
print("\nMediana")
print( columna4.median())
print("\nDesviacion estandar")
print( columna4.std())

#Valor máximo y mínimo
print("\nValor maximo")
print(columna4.max())
print("\nValor minimo")
print(columna4.min())


#########################
#       Columna 5
#########################
print ("\n#########################\n  BOD  \n#########################")
columna5= df["BOD"]
#Valores únicos
print("\nValores unicos")
print(columna5.unique())

#Media,mediana, desviación estandar
print("\nMedia")
print(columna5.mean())
print("\nMediana")
print( columna5.median())
print("\nDesviacion estandar")
print( columna5.std())

#Valor máximo y mínimo
print("\nValor maximo")
print(columna5.max())
print("\nValor minimo")
print(columna5.min())

#########################
#       Columna 6
#########################
print ("\n#########################\n Nitrate & Nitrite  \n######################### ")
columna6= df["NITRATE_N_NITRITE_N"]
#Valores únicos
print("\nValores unicos")
print(columna6.unique())

#Media,mediana, desviación estandar
print("\nMedia")
print(columna6.mean())
print("\nMediana")
print( columna6.median())
print("\nDesviacion estandar")
print( columna6.std())

#Valor máximo y mínimo
print("\nValor maximo")
print(columna6.max())
print("\nValor minimo")
print(columna6.min())

#########################
#       Columna 7
#########################
print ("\n#########################\n FECAL_COLIFORM  \n######################### ")
columna7= df["FECAL_COLIFORM"]
#Valores únicos
print("\nValores unicos")
print(columna7.unique())

#Media,mediana, desviación estandar
print("\nMedia")
print(columna7.mean())
print("\nMediana")
print( columna7.median())
print("\nDesviacion estandar")
print( columna7.std())

#Valor máximo y mínimo
print("\nValor maximo")
print(columna7.max())
print("\nValor minimo")
print(columna7.min())

#########################
#       Columna 8
#########################
print ("\n#########################\n TOTAL_COLIFORM  \n######################### ")
columna8= df["TOTAL_COLIFORM"]
#Valores únicos
print("\nValores unicos")
print(columna8.unique())

#Media,mediana, desviación estandar
print("\nMedia")
print(columna8.mean())
print("\nMediana")
print( columna8.median())
print("\nDesviacion estandar")
print( columna8.std())

#Valor máximo y mínimo
print("\nValor maximo")
print(columna8.max())
print("\nValor minimo")
print(columna8.min())



####################################################################
#                     A c t i v i d a d  3
####################################################################
# Mapas de calor y boxplots
#Alison Magie Yáñez Dávila 

#   -INSTRUCCIONES
#   -Cargar los datos.
#   -Selecciones dos columnas que al momento parezcan interesantes. Para éstas:
#   -Desplegar su histograma. 
#   -Desplegar el diagrama de cajas y bigotes.
#   -Si hay outliers, quítalos y vuelve a desplegar el diagrama con los nuevos datos.
#   -Despliega el mapa de calor de las correlaciones entre todas las variables numéricas. 
#    Escoge la visualización más adecuada y que aporte la mayor información posible para el análisis.

#Lectura de archivo csv haciendo uso de pandas
file='waterquality.csv'
df= pd.read_csv(file,encoding='latin1')

###########################
# Mapa de calor completo
###########################
plt.figure(figsize=(15,5))
sns.heatmap(df.corr(),annot=True,vmax=1,cmap="YlGnBu")
plt.show()


###########################
#           B O D 
###########################
bins=np.arange(0,df.BOD.max() +1.5) -0.5
bins = np.arange(0,30 +1.5) -0.5 #Establece rangos de visualización

#Muestra de histograma
df.hist(column="BOD", bins=bins,grid=False,color="cornflowerblue")
plt.show()

#Despliegue de cajas y bigotes
df=df[df.BOD<6.5]
df.boxplot(column=["BOD"])
plt.show()

#Mapa de calor
column=df.corr()[['BOD']].sort_values(by='BOD',ascending=False)
sns.heatmap(column,vmin=-1,vmax=1,annot=True,cmap='Blues')
plt.show()


##################################
# N I T R A T E  &  N I T R I T E
###################################
bins=np.arange(0,df.NITRATE_N_NITRITE_N.max() +1.5) -0.5
bins = np.arange(0,7 +1.5) -0.5 #Establece rangos de visualización

#Muestra de histograma
df.hist(column="NITRATE_N_NITRITE_N",grid=False,color="indigo")
plt.show()

#Despliegue de cajas y bigotes
df=df[df.NITRATE_N_NITRITE_N<2.5]
df.boxplot(column=["NITRATE_N_NITRITE_N"],grid=False)
plt.show()

#Mapa de calor 
column=df.corr()[['NITRATE_N_NITRITE_N']].sort_values(by='NITRATE_N_NITRITE_N',ascending=False)
sns.heatmap(column,vmin=-1,vmax=1,annot=True,cmap='Purples')
plt.show()

####################################################################
#                     A c t i v i d a d  3
####################################################################
# Actividad 4 patrones con K-Means
#Alison Magie Yáñez Dávila A01423011

#INSTRUCCIONES
#   -Carga tus datos
#   -Selecciona dos variables que consideres interesantes para este análisis.
#   -Determina un valor de k de acuerdo a los datos que tienes, las variables y una pregunta que quieres contestar con este análisis.
#   -Utilizando scikitlearn calcula los centros del algoritmo k-means

#Carga de librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Lectura de archivo csv haciendo uso de pandas
file='waterquality.csv'
df= pd.read_csv(file,encoding='latin1')
df=df.dropna(axis=0,how='any')


df = df[df["BOD"]<=20]
df = df[df["NITRATE_N_NITRITE_N"]<=4]

test=df[["BOD","NITRATE_N_NITRITE_N"]]
test=test.dropna(axis=0,how='any')

print("Centroides")
kmeans= KMeans (n_clusters=3).fit(test)
centroids=kmeans.cluster_centers_
print(centroids)

#Predicciones 
cla=kmeans.predict(test)


print("\nKMeans")
data={'BOD':[50],'NITRATE_N_NITRITE_N':[20]}
newdf=pd.DataFrame(data)
print(kmeans.predict(newdf))

plt.scatter(df["BOD"],df["NITRATE_N_NITRITE_N"],s=7, c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0],centroids[i][1],marker="o",c="red")
plt.title("gráfica 1 K-Means")


plt.xlabel("BOD")
plt.ylabel("NITRATE_N_NITRITE_N")

plt.show()



