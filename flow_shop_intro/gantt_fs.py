#################################################################
# Diagrama de Gantt Básico para Programación de la Producción   #
# Autor: Rodrigo Maranzana                                      #
# Contacto: https://www.linkedin.com/in/rodrigo-maranzana       #
# Fecha: Octubre 2020                                           #
#################################################################

import matplotlib.pyplot as plt
import numpy as np
import random

def inicializar_gantt(maquinas, ht):
    # Parámetros:
    hbar = 10
    tticks = 10
    nmaq = len(maquinas)

    # Creación de los objetos del plot:
    fig, gantt = plt.subplots()

    # Diccionario con parámetros:
    diagrama = {
        "fig": fig,
        "ax": gantt,
        "hbar": hbar,
        "tticks": tticks,
        "maquinas": maquinas,
        "ht": ht,
        "colores": {}
    }

    # Etiquetas de los ejes:
    gantt.set_xlabel("Tiempo")
    gantt.set_ylabel("Máquinas")

    # Límites de los ejes:
    gantt.set_xlim(0, ht)
    gantt.set_ylim(nmaq*hbar, 0)

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

    return diagrama

# Función para armar tareas:
def agregar_subtarea(diagrama, t0, d, maq, nombre_tarea, color=None):
    maquinas = diagrama["maquinas"]
    hbar = diagrama["hbar"]
    gantt = diagrama["ax"]
    ht = diagrama["ht"]

    # Color:
    if diagrama["colores"].get(nombre_tarea) == None:
        if color == None:
            r = random.random()
            g = random.random()
            b = random.random()
            color = (r, g, b)

            diagrama["colores"].update({nombre_tarea: color})
    else:
        color = diagrama["colores"].get(nombre_tarea)

    # Índice de la máquina:
    imaq = maquinas.index(maq)
    # Posición de la barra:
    gantt.broken_barh([(t0, d)], (hbar*imaq, hbar),
                      facecolors=(color))
    # Posición del texto:
    gantt.text(x=(t0 + d/2), y=(hbar*imaq + hbar/2),
                  s=f"{nombre_tarea} ({d})", va='center', ha='center', color='white')

def completar_gantt(diagrama, calendario, n_maqs, n_tareas):
    # Agregamos las subtareas:
    for subtarea in calendario:

        agregar_subtarea(
            diagrama,
            subtarea["t0"],
            subtarea["d"],
            n_maqs[subtarea["i_maq"]],
            n_tareas[subtarea["i_tarea"]]
        )

def crear_gantt_fs(calendario, n_maqs, n_tareas):
    # Horizonte temporal:
    ultima_subtarea = calendario[-1]
    ht = ultima_subtarea["t0"] + ultima_subtarea["d"]

    # Creamos el diagrama de gantt:
    diagrama = inicializar_gantt(n_maqs, ht)

    # Completamos el gantt:
    completar_gantt(diagrama, calendario, n_maqs, n_tareas)

    # Retornamos el diagrama:
    return diagrama

def crear_y_mostrar_gantt_fs(calendario, n_maqs, n_tareas):
    # Creamos el gantt:
    crear_gantt_fs(calendario, n_maqs, n_tareas)

    # Plotteamos:
    mostrar()

def mostrar():
    plt.show()
