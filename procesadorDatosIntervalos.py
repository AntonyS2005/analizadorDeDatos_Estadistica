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
    
    ni= 1+3.322*math.log(n,10)
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

    for indice in range(canIntervalos):
        dVar = xi[indice] - mediaArit
        dVar = round(dVar,2)
        d.append(dVar)
        fPorAbsD.append(round(frecuencia[indice]*abs(dVar),2))
        fPorDD.append(round(frecuencia[indice]*dVar**2,2))
        fPorDDD.append(round(frecuencia[indice]*dVar**3,2))
        fPorDDDD.append(round(frecuencia[indice]*dVar**4,2))
        
        
    print(f"li {li}")
    print(f"ls{ls}")
    print(f"xi{xi}")
    print(f"f{frecuencia}")
    print(f"fr {fr}")
    print(f"fa{fa}")
    print(f"fa%{faPor}")
    print(f"fd{fd}")
    print(f"fd%{fdPor}")
    print(f"F*xi{fPorXi}")
    print(f"d {d}")
    print()
    print(f"f*|d|{fPorAbsD}")
    print(sum( fPorAbsD))
    print()
    print(f"f*d^2{fPorDD}")
    print(sum(fPorDD))
    print()
    print(f"f*d^3{fPorDDD}")
    print(sum(fPorDDD))
    print()
    print(f"f*d^4{fPorDDDD}")
    print(sum(fPorDDDD))
    print()
    print(f"media aritmetica {mediaArit}")
    
                
                
tablaPorIntervalos()
