import pandas as pd
import numpy as np

def esNumero(num):
    try:
        if pd.isna(num):
            return False
        float(num)
        return True
    except Exception:
        return False

def leerDatos(ubi):
    terFila = False
    terColumna = False
    nFila = -1
    datos = list()
    x = pd.read_excel(ubi)
    maxFilas, maxColumnas = x.shape
    
    while not terFila:
        nFila += 1
        
        if nFila >= maxFilas:
            break
        
        nColumnas = -1
        terColumna = False
        
        while not terColumna:
            nColumnas += 1
            
            if nColumnas >= maxColumnas:
                break
            
            dato = x.iloc[nFila, nColumnas]

            if esNumero(dato):
                datos.append(float(dato))
            
            if nColumnas + 1 >= maxColumnas:
                terColumna = True
            else:
                datoSiguiente = x.iloc[nFila, nColumnas + 1]
                if not esNumero(datoSiguiente):
                    terColumna = True
        
        if nFila + 1 >= maxFilas:
            terFila = True
        else:
            datoSiguiente = x.iloc[nFila + 1, nColumnas]
            if not esNumero(datoSiguiente):
                terFila = True

    datos.sort()
    return datos

