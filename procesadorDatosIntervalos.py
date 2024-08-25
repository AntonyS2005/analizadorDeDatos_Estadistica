from readExcel import leerDatos
from  collections import Counter
import math 

def condicion(x,li,ls):
    if x >= li and x <= ls :
        return True
    return False  
    
def tablaPorIntervalos():
    datos = leerDatos()
    cEnDatos = Counter(datos)
    min = datos[0]
    max = datos[-1]
    n = len(datos)
    rango = max - min
    
    ni = 1+3.322*math.log(n,10)
    ni = round(ni,2)
    i = rango / ni
    i = round(i,0)#rawr
    li = list()
    ls= list()
    x = min
    xi = list()
    frecuencia = list()
    fr= list()
    while x < max:
        li.append(x)
        ls.append(x + i - 1)
        x += i 
    
    fa = list()
    fa
    faDato = 0
    faPor = list()
    canIntervalos= len(li)
    fd= list()
    fdVar = n
    fdPor = list()
    fPorXi = list()
    d = list()
    for indice in range (canIntervalos):
        promedio = (li[indice]+ls[indice])/2 
        xi.append(promedio)
        fre=[x for x in datos if condicion(x,li[indice],ls[indice])]
        freVar= len(fre)
        frecuencia.append(freVar)
        xFR=  (freVar * 100 ) / n
        xFR = round(xFR,2)
        fr.append(xFR)
        faDato += len(fre)
        fa.append(faDato)
        faVar=(faDato*100)/n
        faVar= round(faVar,2)
        faPor.append(faVar)
        fd.append(fdVar)
        fdPor.append(round(((fdVar*100)/n),2))

        fdVar-=freVar
        fPorXi.append(round((freVar  * promedio),2))
    mediaArit = sum(fPorXi)/n
    mediaArit = round(mediaArit,2)
    fPorAbsD = list()
    fPorDDD = list()
    fPorDD = list()
    fPorDDDD = list()
    indMaxFre = 0
    maxFre=0
    posicionMediana = n / 2
    serchMediana = True
    mediana = 0
    for indice in range(canIntervalos):
        #en esta parte se calcula de d a f*d4
        dVar = xi[indice] - mediaArit
        dVar = round(dVar,2)
        d.append(dVar)
        fPorAbsD.append(round(frecuencia[indice]*abs(dVar),2))
        fPorDD.append(round(frecuencia[indice]*dVar**2,2))
        fPorDDD.append(round(frecuencia[indice]*dVar**3,2))
        fPorDDDD.append(round(frecuencia[indice]*dVar**4,2))
        #en esta parte se calcula la moda
        if frecuencia[indice] > maxFre:
            indMaxFre= indice
            maxFre = frecuencia[indice]
            #en esta parte se calcula la mediana
        if posicionMediana <= fa[indice] and  serchMediana :
            print(fa[indice])
            mediana = li[indice] + ( ( posicionMediana - fa[indice-1] ) / frecuencia[indice] ) * i
            mediana = round(mediana , 2)
            serchMediana = False

    delta1Moda=frecuencia[indMaxFre] - frecuencia[indMaxFre-1]
    delta2Moda=frecuencia[indMaxFre] - frecuencia[indMaxFre+1]
    moda = li[indMaxFre]+(delta1Moda/(delta1Moda+delta2Moda)* i)
    moda = round(moda,2)
    desviacionMed = sum(fPorAbsD)/n
    desviacionMed = round(desviacionMed,2)
    desviacionEst = sum(fPorDD)/n 
    desviacionEst = math.sqrt(desviacionEst)
    desviacionEst = round(desviacionEst,2)
    sk = sum(fPorDDD) / ( n * ( desviacionEst ** 3 ) )
    sk = round(sk,2)
    k = sum(fPorDDDD) / ( n * ( desviacionEst ** 4 ) )
    k = round( k , 2 )
    print(sk)
    print(k)
tablaPorIntervalos()
