# Obtención de estadísticas descriptivas
#Alison Magie Yáñez Dávila 

#   -INSTRUCCIONES
#   -Cargar los datos.
#   -Selecciones dos columnas que al momento parezcan interesantes. Para éstas:
#   -Desplegar su histograma. 
#   -Desplegar el diagrama de cajas y bigotes.
#   -Si hay outliers, quítalos y vuelve a desplegar el diagrama con los nuevos datos.
#   -Despliega el mapa de calor de las correlaciones entre todas las variables numéricas. 
#    Escoge la visualización más adecuada y que aporte la mayor información posible para el análisis.

#Importando pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#Lectura de archivo csv haciendo uso de pandas
file='waterquality.csv'
df= pd.read_csv(file,encoding='latin1')


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


