from collections import Counter
from readExcel import leerDatos 
# reemplazar esto para que tome los datos de tu lista 
# estesolo es prueba
datos = leerDatos()

frecuencias = Counter(datos)
n = len(datos)

valores = sorted(frecuencias.keys())

frecuencia_abs = []
frecuencia_rel = []
frecuencia_acum = []
frecuencia_acum_rel = []
frecuencia_desc = []
frecuencia_desc_rel = []

fa_acum = 0
fd_acum = n

for valor in valores:
    f = frecuencias[valor]
    fa_acum += f
    fr = (f / n) * 100
    fr_acum_rel = (fa_acum / n) * 100
    fd_acum -= f
    fd_rel = (fd_acum / n) * 100

    frecuencia_abs.append(f)
    frecuencia_rel.append(fr)
    frecuencia_acum.append(fa_acum)
    frecuencia_acum_rel.append(fr_acum_rel)
    frecuencia_desc.append(fd_acum)
    frecuencia_desc_rel.append(fd_rel)

# Esto me inprimira el cuadro estadistico
print(f"{'x':<5}{'f':<5}{'f%':<7}{'Fa':<5}{'Fa%':<7}{'Fd':<5}{'Fd%':<7}")
print("-" * 37)
for i, valor in enumerate(valores):
    print(f"{valor:<5}{frecuencia_abs[i]:<5}{frecuencia_rel[i]:<7.2f}"
          f"{frecuencia_acum[i]:<5}{frecuencia_acum_rel[i]:<7.2f}"
          f"{frecuencia_desc[i]:<5}{frecuencia_desc_rel[i]:<7.2f}")