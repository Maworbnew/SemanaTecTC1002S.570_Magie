# Obtención de estadísticas descriptivas
#Alison Magie Yáñez Dávila 

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

#Importando pandas
import pandas as pd

#Lectura de archivo csv haciendo uso de pandas
file='data.csv'
df= pd.read_csv(file)

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
print ("\n#########################\n  D A N C E A B I L T Y  \n#########################")
columna1= df["danceability"]
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

#Valor máximo y mínimo
print("\nValor maximo")
print(columna1.max())
print("\nValor minimo")
print(columna1.min())

#########################
#       Columna 2
#########################
print ("\n#########################\n      E N E R G Y  \n######################### ")
columna2= df["energy"]
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