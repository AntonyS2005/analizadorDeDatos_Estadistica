import pandas as pd
def leerDatos():
    terFila = False
    terColumna = False
    nFila = -1
    nColumnas = -1
    datos = list()
    x = pd.read_excel("ej.xlsx")
    while  terFila == False:
        nFila += 1
        nColumnas = -1
        terColumna = False
        while terColumna == False :
            nColumnas += 1
            dato = x.iloc[nColumnas,nFila]
            if str(dato).isnumeric() :
                datos.append(dato);
            datoSiguiente = x.iloc[nColumnas+1,nFila]
            if not str(datoSiguiente).isnumeric():
                terColumna = True
        datoSiguiente = x.iloc[nColumnas,nFila+1]
        if not str(datoSiguiente).isnumeric():
            terFila=True
    datos.sort()
    return datos
            
def calcularF():
    datos = leerDatos()
    
print(leerDatos().item())    