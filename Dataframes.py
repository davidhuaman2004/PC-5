# I M P O R T A   P A N D A S  Y  N U M P Y
import pandas as pd
import numpy as pd
# C R E A R   U N A  S E R I E
print("================ C R E A R   U N A  S E R I E ================")
# Crea una serie de los números 10, 20 and 10.
serienum = pd.Series([10, 20, 10])
print(serienum)
# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'.
colores = pd.Series(['rojo', 'verde', 'azul'])
print(colores)

# C R E A R   U N    D A T A F R A M E
print("================ C R E A R   U N    D A T A F R A M E ================")
# Crea un dataframe vacío llamado 'df'.
df = pd.DataFrame()
# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado.
df['Serie de números'] = serienum
print(df)
# Crea una nueva columna en el dataframe, y asignale la 2da serie que has creado.
df['Colores'] = colores
print(df)

# L E E R   U N   D A T A F R A M E
print("================ L E E R   U N   D A T A F R A M E ================")
# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" 
# y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"
avengers = pd.read_csv('C:/Users/DAVID/PythonFundamentos-master/Modulo5/Ejercicios/src/pandas/avengers.csv')

# I N S P E C C I O N A R    U N   D A T A F R A M E 
print("================ I N S P E C C I O N A R    U N   D A T A F R A M E ================")
# Muestra las primeras 5 filas del DataFrame.
print(avengers.head(5))
# Muestra las primeras 10 filas del DataFrame. 
print(avengers.head(10))
# Muestra las últimas 5 filas del DataFrame.
print(avengers.tail(5))


# T A M A Ñ O   D E L   D A T A F R A M E
print("================ T A M A Ñ O   D E L   D A T A F R A M E ================")
# Muestra los data types del dataframe
print(avengers.dtypes)
# Cambia el indice a la columna "fecha_inicio".
avengers = avengers.set_index("fecha_inicio").copy()
print(avengers)
# Ordena el índice de forma descendiente
avengers = avengers.sort_values(by=['fecha_inicio'], ascending=[False])
print(avengers)
# Resetea el índice
avengers.reset_index(drop=True, inplace=True)
print(avengers)