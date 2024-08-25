from collections import Counter
from readExcel import leerDatos

# reemplazar esto para que tome los datos de tu lista 
# estesolo es prueba
# datos = leerDatos()

datos = [ 11, 9,	8,	7,	11,	6,	11,
11,	11,	8,	6,	9,	7,	10,
11,	5,	9,	7,	8,	6,	5,
9,	7,	5,	5,	6,	8,	8,
8,	9,	11,	8,	8,	8,	10,
10,	8,	9,	7,	9,	6,	7,
9,	9,	11,	10,	7,	10,	8,
11,	10,	5,	5,	5,	6,	10,
6,	6,	10,	7,	9,	9,	10,
8,	7,	6,	10,	7,	9,	7]

frecuencias = Counter(datos)
n = len(datos)

valores = sorted(frecuencias.keys())

frecuencia_abs = []
frecuencia_rel = []
frecuencia_acum = []
frecuencia_acum_rel = []
frecuencia_desc = []
frecuencia_desc_rel = []
deltas = []
frecuencia_abs_delta = []
frecuencia_abs_delta_abs = []
frecuencia_abs_delta_cuadrado = []
frecuencia_abs_delta_cubo = []
frecuencia_abs_delta_cuarta = []

fa_acum = 0
fd_acum = n

media = sum([valor * frecuencias[valor] for valor in valores]) / n

for valor in valores:
    f = frecuencias[valor]
    fa_acum += f
    fr = (f / n) * 100
    fr_acum_rel = (fa_acum / n) * 100
    fd_acum -= f
    fd_rel = (fd_acum / n) * 100

    delta = valor - media
    abs_delta = abs(delta)
    delta_cuadrado = delta ** 2
    delta_cubo = delta ** 3
    delta_cuarta = delta ** 4
    


    frecuencia_abs.append(f)
    frecuencia_rel.append(fr)
    frecuencia_acum.append(fa_acum)
    frecuencia_acum_rel.append(fr_acum_rel)
    frecuencia_desc.append(fd_acum)
    frecuencia_desc_rel.append(fd_rel)
    deltas.append(delta)
    frecuencia_abs_delta.append(f * delta)
    frecuencia_abs_delta_abs.append(f * abs_delta)
    frecuencia_abs_delta_cuadrado.append(f * delta_cuadrado)
    frecuencia_abs_delta_cubo.append(f * delta_cubo)
    frecuencia_abs_delta_cuarta.append(f * delta_cuarta)

# Esto me inprimira el cuadro estadistico
print(f"{'x':<5}{'f':<5}{'f%':<7}{'Fa':<5}{'Fa%':<7}{'Fd':<5}{'Fd%':<7}{'d':<7}"
      f"{'f*|d|':<7}{'f*d':<7}{'f*d^2':<7}{'f*d^3':<7}{'f*d^4':<7}")
print("-" * 92)
for i, valor in enumerate(valores):
     print(f"{valor:<5}{frecuencia_abs[i]:<5}{frecuencia_rel[i]:<7.2f}"
        f"{frecuencia_acum[i]:<5}{frecuencia_acum_rel[i]:<7.2f}"
        f"{frecuencia_desc[i]:<5}{frecuencia_desc_rel[i]:<7.2f}"
        f"{deltas[i]:<7.2f}{frecuencia_abs_delta_abs[i]:<7.2f}"
        f"{frecuencia_abs_delta[i]:<7.2f}{frecuencia_abs_delta_cuadrado[i]:<7.2f}"
        f"{frecuencia_abs_delta_cubo[i]:<7.2f}{frecuencia_abs_delta_cuarta[i]:<7.2f}")
     
        # Calcular los totales
total_f = sum(frecuencia_abs)
total_f_rel = sum(frecuencia_rel)
total_abs_delta = sum(frecuencia_abs_delta_abs)
total_delta = sum(frecuencia_abs_delta)
total_delta_cuadrado = sum(frecuencia_abs_delta_cuadrado)
total_delta_cubo = sum(frecuencia_abs_delta_cubo)
total_delta_cuarta = sum(frecuencia_abs_delta_cuarta)

# Imprimir la fila de totales
print("-" * 92)
print(f"{'T':<5}{total_f:<5}{total_f_rel:<7.2f}{'':<19}"
      f"{total_abs_delta:<7.2f}{total_delta:<7.2f}"
      f"{total_delta_cuadrado:<7.2f}{total_delta_cubo:<7.2f}"
      f"{total_delta_cuarta:<7.2f}")

# Resumen estadístico
media = sum([x * f for x, f in frecuencias.items()]) / n
mediana = sorted(datos)[n // 2] if n % 2 != 0 else (sorted(datos)[n // 2 - 1] + sorted(datos)[n // 2]) / 2
moda = max(frecuencias, key=frecuencias.get)
varianza = total_delta_cuadrado / n
curtosis = (n * total_delta_cuarta) / (total_delta_cuadrado ** 2) - 3
coef_asimetria = (n * total_delta_cubo) / (total_delta_cuadrado ** (3/2))
rango = max(datos) - min(datos)
minimo = min(datos)
maximo = max(datos)

print("\nResumen Estadístico")
print(f"{'Media':<20}: {media:.2f}")
print(f"{'Mediana':<20}: {mediana:.2f}")
print(f"{'Moda':<20}: {moda}")
print(f"{'Varianza':<20}: {varianza:.2f}")
print(f"{'Curtosis':<20}: {curtosis:.2f}")
print(f"{'Coef. Asimetría':<20}: {coef_asimetria:.2f}")
print(f"{'Rango':<20}: {rango}")
print(f"{'Valor Mínimo':<20}: {minimo}")
print(f"{'Valor Máximo':<20}: {maximo}")