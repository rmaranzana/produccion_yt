# Función de cálculo del Makespan:
def calcular_makespan(calendario):
    ultima_subtarea = calendario[-1]
    primera_subtarea = calendario[0]

    return ultima_subtarea['t0'] + ultima_subtarea['d'] - primera_subtarea['t0']

# Datos del problema:
nombre_maq = ["M0", "M1", "M2", "M3"]
nombre_tar = ["T0", "T1", "T2"]

d_tareas = [
    (5, 10, 6, 8),
    (8, 15, 5, 7),
    (8, 5, 7, 9)
]

# Armamos una secuencia ejemplo:
secuencia1 = [2, 1, 0]

# Importamos nuestro programador de Flow Shop y programamos la producción en un calendario:
from makespan.programador_flow_shop import programar_fs

calendario1 = programar_fs(d_tareas, nombre_maq, nombre_tar, secuencia1)

print(calendario1)

# calculamos el makespan y lo imprimimos:
makespan1 = calcular_makespan(calendario1)

print(makespan1)

# Importamos el diagrama de Gantt y lo armamos:
# from flow_shop_intro.gantt_fs import crear_y_mostrar_gantt_fs

# crear_y_mostrar_gantt_fs(calendario1, nombre_maq, nombre_tar)
from flow_shop_intro.gantt_fs import crear_gantt_fs

diagrama = crear_gantt_fs(calendario1, nombre_maq, nombre_tar)
diagrama['fig'].savefig('filename.png', dpi=225)


# Vamos a calcular distintas combinaciones de secuencias:
from itertools import permutations

combinaciones = list(permutations(range(0,3)))

# Imprimimos las combinaciones:
for comb_i in combinaciones:
    print(comb_i)

# Armamos el calendario para cada una y su makespan:
makespans = [0] * len(combinaciones)
calendarios = [0] * len(combinaciones)

for i, comb_i in enumerate(combinaciones):

    # Armamos el calendario de la combinación i y lo guardamos:
    calendarios[i] = programar_fs(d_tareas, nombre_maq, nombre_tar, comb_i)

    # Calculamos el makespan y lo guardamos:
    makespans[i] = calcular_makespan(calendarios[i])

# Imprimimos los Makespans:
print(makespans)

# Mínimo makespan de las combinaciones:
min_ms = min(makespans)

print(min_ms)

import numpy as np

i_min_ms = np.argmin(makespans)

print(i_min_ms)

min_calendario = calendarios[i_min_ms]

print(min_calendario)
