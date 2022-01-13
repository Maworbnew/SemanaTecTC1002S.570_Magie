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
import matplotlib.pyplot as plt

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