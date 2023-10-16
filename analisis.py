# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats

ruta = r'C:\Users\lucas\OneDrive\Escritorio\companyofone\Red farma Rio Bueno\Datos\16-09-2023\junio_julio_Ventas_x_Producto.xlsx'
data = pd.read_excel( ruta ,engine='openpyxl', header= 1)

#ANALISIS DEPARTAMENTO FARMACIA 
nombre_columna = "DEPARTAMENTO"
categoria_deseada = "FARMACIA"

# Filtrar el DataFrame basado en la categoría deseada
data_filtrada = data[data[nombre_columna] == categoria_deseada]

# Mostrar el resultado
print(data_filtrada)



#ANALISIS CANTIDAD DE UNIDADES
columna = "UNIDADES"
datos_columna = data_filtrada[columna]

#MEDIA 

# Histograma
plt.figure(figsize=(20, 5))
plt.hist(datos_columna, bins=10, density=True, alpha=0.6, color='b')
plt.title(f"Histograma de {columna}")
plt.show()

# Gráfico QQ
plt.figure(figsize=(10, 5))
stats.probplot(datos_columna, dist="norm", plot=plt)
plt.title(f"Gráfico QQ de {columna}")
plt.show()


#DATOS COSTO NO AGREGADO
filtered_data = data_filtrada[data_filtrada["PROM. CPP"] < 300]

