from readExcel import leerDatos
import math

def condicion(x, li, ls):
    return li <= x <= ls

def contar_decimales(numero):
    str_numero = str(numero)
    if '.' in str_numero:
        parte_decimal = str_numero.split('.')[1]
        if parte_decimal == '0' * len(parte_decimal):
            return 0
        else:
            return len(parte_decimal)
    else:
        return 0

def max_decimales(lista_numeros):
    max_decimales = 0
    for numero in lista_numeros:
        decimales = contar_decimales(numero)
        if decimales > max_decimales:
            max_decimales = decimales
    return max_decimales

def redondear(valor, decimales):
    return round(valor, decimales)

def tablaPorIntervalos(datos):
    decimales = max_decimales(datos)
    decimales2 = 2 if decimales == 0 else decimales
    min_val = datos[0]
    max_val = datos[-1]
    n = len(datos)
    rango = max_val - min_val

    ni = 1 + 3.322 * math.log(n, 10)
    ni = redondear(ni, decimales2)
    i = rango / ni
    i = redondear(i, decimales)

    li = []
    ls = []
    x = min_val
    xi = []
    frecuencia = []
    fr = []

    while x < max_val:
        li.append(redondear(x, decimales))
        ls.append(redondear(x + i -(1 * (10**-decimales)), decimales))
        x += i

    fa = []
    faDato = 0
    faPor = []
    canIntervalos = len(li)
    fd = []
    fdVar = n
    fdPor = []
    fPorXi = []
    d = []

    for indice in range(canIntervalos):
        promedio = (li[indice] + ls[indice]) / 2
        promedio = redondear(promedio, decimales2)
        xi.append(promedio)
        fre = [x for x in datos if condicion(x, li[indice], ls[indice])]
        freVar = len(fre)
        frecuencia.append(freVar)
        xFR = (freVar * 100) / n
        xFR = redondear(xFR, decimales)
        fr.append(xFR)
        faDato += len(fre)
        fa.append(faDato)
        faVar = (faDato * 100) / n
        faVar = redondear(faVar, decimales)
        faPor.append(faVar)
        fd.append(fdVar)
        fdPor.append(redondear((fdVar * 100) / n, decimales))
        fdVar -= freVar
        fPorXi.append(redondear(freVar * promedio, decimales2))

    mediaArit = sum(fPorXi) / n
    mediaArit = redondear(mediaArit, decimales2)
    fPorAbsD = []
    fPorDDD = []
    fPorDD = []
    fPorDDDD = []
    indMaxFre = 0
    maxFre = 0
    posicionMediana = n / 2
    serchMediana = True
    mediana = 0
    cuartiles = []
    deciles = []
    percentiles = []

    for j in range(4):
        posMedPos = n * ((j + 1) / 4)
        for y in range(canIntervalos):
            if posMedPos <= fa[y]:
                cuartil = li[y] + ((posMedPos - fa[y - 1]) / frecuencia[y]) * i
                cuartil = redondear(cuartil, decimales2)
                cuartiles.append(cuartil)
                break

    for j in range(10):
        posMedPos = n * ((j + 1) / 10)
        for y in range(canIntervalos):
            if posMedPos <= fa[y]:
                decil = li[y] + ((posMedPos - fa[y - 1]) / frecuencia[y]) * i
                decil = redondear(decil, decimales2)
                deciles.append(decil)
                break

    for j in range(100):
        posMedPos = n * ((j + 1) / 100)
        for y in range(canIntervalos):
            if posMedPos <= fa[y]:
                percentil = li[y] + ((posMedPos - fa[y - 1]) / frecuencia[y]) * i
                percentil = redondear(percentil, decimales2)
                percentiles.append(percentil)
                break

    for indice in range(canIntervalos):
        dVar = xi[indice] - mediaArit
        dVar = redondear(dVar, decimales2)
        d.append(dVar)
        fPorAbsD.append(redondear(frecuencia[indice] * abs(dVar), decimales2))
        fPorDD.append(redondear(frecuencia[indice] * dVar ** 2, decimales2))
        fPorDDD.append(redondear(frecuencia[indice] * dVar ** 3, decimales2))
        fPorDDDD.append(redondear(frecuencia[indice] * dVar ** 4, decimales2))

        if frecuencia[indice] > maxFre:
            indMaxFre = indice
            maxFre = frecuencia[indice]

        if posicionMediana <= fa[indice] and serchMediana:
            mediana = li[indice] + ((posicionMediana - fa[indice - 1]) / frecuencia[indice]) * i
            mediana = redondear(mediana, decimales2)
            serchMediana = False

    # Calcular moda
    if indMaxFre > 0 and indMaxFre < len(frecuencia) - 1:
        delta1Moda = frecuencia[indMaxFre] - frecuencia[indMaxFre - 1]
        delta2Moda = frecuencia[indMaxFre] - frecuencia[indMaxFre + 1]
    elif indMaxFre == 0:
        delta1Moda = frecuencia[indMaxFre] - frecuencia[indMaxFre + 1]
        delta2Moda = 0  # No hay valor a la derecha
    elif indMaxFre == len(frecuencia) - 1:
        delta1Moda = frecuencia[indMaxFre] - frecuencia[indMaxFre - 1]
        delta2Moda = 0  # No hay valor a la derecha
    else:
        delta1Moda = 0
        delta2Moda = 0

    if delta1Moda + delta2Moda != 0:
        moda = li[indMaxFre] + (delta1Moda / (delta1Moda + delta2Moda) * i)
    else:
        moda = None
        print("Advertencia: No se puede calcular la moda debido a una división por cero.")

    if moda is not None:
        moda = redondear(moda, decimales2)

    desviacionMed = sum(fPorAbsD) / n
    desviacionMed = redondear(desviacionMed, decimales2)
    desviacionEst = sum(fPorDD) / n
    desviacionEst = math.sqrt(desviacionEst)
    desviacionEst = redondear(desviacionEst, decimales2)

    if desviacionEst != 0:
        sk = sum(fPorDDD) / (n * (desviacionEst ** 3))
        sk = redondear(sk, decimales2)
        k = sum(fPorDDDD) / (n * (desviacionEst ** 4))
        k = redondear(k, decimales2)
    else:
        sk = None
        k = None
        print("Advertencia: La desviación estándar es cero, por lo que no se puede calcular el sesgo y la curtosis.")

    tabla = []
    for ji in range(canIntervalos):
        tabla.append([
            li[ji], ls[ji], xi[ji], frecuencia[ji], fr[ji], fa[ji], faPor[ji],
            fd[ji], fdPor[ji], fPorXi[ji], d[ji], fPorAbsD[ji], fPorDD[ji]
        ])

    for fila in tabla:
        print(fila)

# Llamada a la función con el argumento correcto
tablaPorIntervalos(leerDatos("prueba.xlsx"))
