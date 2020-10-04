#################################################################
# Diagrama de Gantt Básico para Programación de la Producción   #
# Autor: Rodrigo Maranzana                                      #
# Contacto: https://www.linkedin.com/in/rodrigo-maranzana       #
# Fecha: Octubre 2020                                           #
#################################################################

import matplotlib.pyplot as plt
import numpy as np

# Datos
ht = 50
nmaq = 3
hbar = 10
tticks = 10
maquinas = ["M1", "M2", "M3"]

# Creación de los objetos del plot:
fig, gantt = plt.subplots()

# Etiquetas de los ejes:
gantt.set_xlabel("Tiempo")
gantt.set_ylabel("Máquinas")

# Límites de los ejes:
gantt.set_xlim(0, ht)
gantt.set_ylim(0, nmaq*hbar)

# Divisiones del eje de tiempo:
gantt.set_xticks(range(0, ht, 1), minor=True)
gantt.grid(True, axis='x', which='both')

# Divisiones del eje de máquinas:
gantt.set_yticks(range(hbar, nmaq*hbar, hbar), minor=True)
gantt.grid(True, axis='y', which='minor')

# Etiquetas de máquinas:
gantt.set_yticks(np.arange(hbar/2, hbar*nmaq - hbar/2 + hbar,
                           hbar))
gantt.set_yticklabels(maquinas)

# Función para armar tareas:
def agregar_tarea(t0, d, maq, nombre, color):
    # Índice de la máquina:
    imaq = maquinas.index(maq)
    # Posición de la barra:
    gantt.broken_barh([(t0, d)], (hbar*imaq, hbar),
                      facecolors=(color))
    # Posición del texto:
    gantt.text(x=(t0 + d/2), y=(hbar*imaq + hbar/2),
                  s=f"{nombre} ({d})", va='center', color='white')

# Agregamos dos tareas de ejemplo:
agregar_tarea(35, 15, "M1", "T1", "r")
agregar_tarea(10, 20, "M3", "T1", "g")

# Ploteamos
plt.show()
