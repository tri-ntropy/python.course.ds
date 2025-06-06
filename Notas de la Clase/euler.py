import numpy as np

def creacion_parametros(t0, tf, x0, v0, n):
    tiempo, paso_tiempo = np.linspace(t0, tf, n + 1, retstep = True)
    desplazamiento = np.zeros(n + 1)
    velocidad = np.zeros(n + 1)
    
    desplazamiento[0] = x0
    velocidad[0] = v0

    return {"tiempo" : tiempo,
            "desplazamiento" : desplazamiento,
            "velocidad" : velocidad,
            "paso_tiempo" : paso_tiempo}

def solver(t0, tf, x0, v0, n, fuerza):
    parametros = creacion_parametros(t0, tf, x0, v0, n)
    tiempo = parametros["tiempo"]
    desplazamiento = parametros["desplazamiento"]
    velocidad = parametros["velocidad"]
    paso_tiempo = parametros["paso_tiempo"] 

    for i in range(1, n + 1):
        velocidad[i] = velocidad[i - 1] + paso_tiempo * fuerza(desplazamiento, velocidad, i)
        desplazamiento[i] = desplazamiento[i - 1] + paso_tiempo * velocidad[i]
    
    return tiempo, velocidad, desplazamiento