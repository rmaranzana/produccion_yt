#################################################################
# Diagrama de Gantt Básico para Programación de la Producción   #
# Autor: Rodrigo Maranzana                                      #
# Contacto: https://www.linkedin.com/in/rodrigo-maranzana       #
# Fecha: Octubre 2020                                           #
#################################################################

nombre_maq = ["M0", "M1", "M2", "M3"]
nombre_tar = ["T0", "T1", "T2", "T3", "T4"]

d_tareas = [
    (5, 10, 6, 8),
    (8, 15, 5, 7),
    (8, 5, 7, 9),
    (10, 7, 11, 5),
    (5, 10, 6, 6)
]

secuencia = [0, 1, 3, 2, 4]

def agregar_subtarea(calendario, t0, d, i_maq, i_tarea):
    # Diccionario de subtarea:
    subtarea = {'t0': t0, 'd': d, 'i_maq': i_maq, 'i_tarea': i_tarea}

    # Agregar al calendario
    calendario.append(subtarea)

def programar_fs(d_tareas, nombre_maq, nombre_tar, secuencia):
    # Creamos el calendario:
    calendario = []

    # Último t0 para cada etapa:
    tn_etapa = [0]*len(nombre_maq)

    # Para cada tarea en la secuencia:
    for i_tarea in secuencia:
        # Para cada subtarea en la tarea:
        for i_maquina, d_subtarea in enumerate(d_tareas[i_tarea]):
            tn_maq_anterior = tn_etapa[i_maquina-1]
            tn_maq_presente = tn_etapa[i_maquina]

            # Obtenemos el t0:
            if (i_maquina > 0) & (tn_maq_anterior > tn_maq_presente):
                t0 = tn_maq_anterior
            else:
                t0 = tn_maq_presente

            # Agregamos subtarea programada:
            agregar_subtarea(calendario, t0, d_subtarea, i_maquina, i_tarea)

            # Nuevo tn:
            tn_etapa[i_maquina] = t0 + d_subtarea

    return calendario
