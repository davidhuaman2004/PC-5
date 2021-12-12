import pandas as pd
import matplotlib.pyplot as plt
import os
import xlwt
# Parte 1
print("============================================")
df_airbnb = pd.read_csv("C:/Users/DAVID\PythonFundamentos-master/Modulo5/Ejercicios/src/pandas/airbnb.csv")
print(df_airbnb.head())
# Parte 2
print("============================================")
print(df_airbnb.dtypes)
# U S A N D O   P A N D A S
# CASO 1
# Alicia va a ir a Lisboa durante una semana con su marido y sus 2 hijos. 
# Están buscando un apartamento con habitaciones separadas para los padres y los hijos. 
# No les importa donde alojarse o el precio, simplemente quieren tener una experiencia agradable. 
# Esto significa que solo aceptan lugares con más de 10 críticas con una puntuación mayor de 4. 
# Cuando seleccionemos habitaciones para Alicia, tenemos que asegurarnos de ordenar las habitaciones 
# de mejor a peor puntuación. Para aquellas habitaciones que tienen la misma puntuación, debemos mostrar 
# antes aquellas con más críticas. Debemos darle 3 alternativas.
print("================CASO 1================")
filtro_Alicia = (df_airbnb['reviews'] > 10)  &  (df_airbnb['overall_satisfaction'] > 4)  &  (df_airbnb['bedrooms'] == 2)
df_Alicia = df_airbnb[filtro_Alicia].sort_values(by=['reviews', 'overall_satisfaction',], ascending=[False, False])
print(df_Alicia.head(3))


# CASO 2
# Roberto es un casero que tiene una casa en Airbnb.
# De vez en cuando nos llama preguntando sobre cuales son las críticas de su alojamiento. 
# Hoy está particularmente enfadado, ya que su hermana Clara ha puesto una casa en Airbnb y 
# Roberto quiere asegurarse de que su casa tiene más críticas que las de Clara. 
# Tenemos que crear un dataframe con las propiedades de ambos. 
# Las id de las casas de Roberto y Clara son 97503 y 90387 respectivamente. 
# Finalmente guardamos este dataframe como excel llamado "roberto.xls
print("================CASO 2================")
condition = (df_airbnb["room_id"] == 97503) | (df_airbnb["room_id"] == 90387)
print(df_airbnb[condition])
if not os.path.isdir('C:/Users/DAVID/PythonFundamentos-master/Modulo5/Ejercicios/src/pandas'):
    os.mkdir('C:/Users/DAVID/PythonFundamentos-master/Modulo5/Ejercicios/src/pandas')
df_airbnb[condition].to_excel('C:/Users/DAVID/PythonFundamentos-master/Modulo5/Ejercicios/src/pandas/roberto.xls',
                   sheet_name='roberto',encoding='utf-8',index=False)

# CASO 3
# Diana va a Lisboa a pasar 3 noches y quiere conocer a gente nueva. Tiene un presupuesto de 50€ para su alojamiento. 
# Debemos buscarle las 10 propiedades más baratas, 
# dandole preferencia a aquellas que sean habitaciones compartidas *(room_type == Shared room)*, 
# y para aquellas viviendas compartidas debemos elegir aquellas con mejor puntuación.
print("================CASO 3================")
filtrar = (df_airbnb["room_type"] == 'Shared room') & (df_airbnb["price"] <= 50) & (df_airbnb["overall_satisfaction"] > 4)
df_new = df_airbnb[filtrar].sort_values(by=['price'], ascending=[True])
print(df_new.head(10))


# U S A N D O   M A T P L O T
# Realizar un gráfico circular, de la cantidad de tipo de habitaciones `room_type`
print("================MATPLOT================")
tipoCuarto = df_airbnb['room_type']
tipoCuarto.value_counts().plot.pie()
print(plt.show())

