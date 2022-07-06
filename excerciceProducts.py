'''
ejercicio: hacer un  programa  contable ,se  tiene una companñia con x productos x cantidades y x precios la unidad 
y tener  cantidad de stock , los productos  deben ir  cambiando ,  ejemplo fruteria  tiene 30 manazan  vendi 10 el stock va ser 20 unidades.

parametrizar  como se quiera
por pantalla  solicitar al usuario que  producto  quiere  y mostrar el  precio   con costo de  $500
luego  imprimir  la lista  de prouctos  ejemplo stock 2  se descuenta el  stock
'''
import pandas as pd
import numpy as np

p = pd.DataFrame({'producto': ['manzana', 'pera', 'banano'],
                  'precio': [2000, 3000, 1500],
                  'cantidad': [10, 20, 30]
                  })

# print(df.index.get_level_values('producto'))
# https://www.analyticslane.com/2021/05/10/pandas-comprobar-la-existencia-de-valores-en-los-dataframe/
