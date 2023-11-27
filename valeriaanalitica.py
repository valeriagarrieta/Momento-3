# -*- coding: utf-8 -*-
"""ValeriaAnalitica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hlc9sghP3qWcucqSWIcetdM2Q0-MP42V

#Analisis de dataframe para nuevas tecnologías.
"""

import pandas as pd

info_alquiler = pd.read_csv('/content/drive/MyDrive/CSV/alquiler.csv', sep = ';')

from google.colab import drive
drive.mount('/content/drive')

info_alquiler.shape

"""Head para imprimir los primeros datos del dataframe tabla:head(numero)"""

info_alquiler.head(10)

"""Tail para imprimir los ultimos datos del dataframe tabla:head(numero)"""

info_alquiler.tail(10)

"""Filtrar la información por categoria de una columna."""

list(info_alquiler['Tipo'].drop_duplicates().tail(10))

list(info_alquiler['Distrito'].drop_duplicates())

list(info_alquiler['Tipo'].drop_duplicates().tail(10))

viviendas = ['Habitación',
 'Casa',
 'Departamento',
 'Casa en condominio',
 'Flat',
 'Casa de villa',
 'Cochera',
 'Loft',
 'Chalet'
 ]

viviendas

"""Validar si viviendas esta en info_alquiler"""

info_viviendas = info_alquiler['Tipo'].isin(viviendas)

info_viviendas

"""construir el data frame con los datos de solo viviendas"""

datos_viviendas = info_alquiler[info_viviendas]

datos_viviendas

datos_viviendas.shape

datos_viviendas.index = range(datos_viviendas.shape[0])

datos_viviendas

datos_viviendas.to_csv('alquileres_viviendas.csv', sep = ';')