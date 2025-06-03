import numpy as np
import matplotlib.pyplot as plt

class simulacion:
    def __init__(self, t0, tf, x0, v0, n, fuerza = lambda x, v, i: 0, inicializado = False):
        self.t0 = t0
        self.tf = tf
        self.x0 = x0
        self.v0 = v0
        self.n = n
        self.fuerza = fuerza
        self.inicializado = inicializado

        self.desplazamiento = np.zeros(self.n + 1)
        self.velocidad = np.zeros(self.n + 1)

        self.tiempo, self.paso_tiempo = np.linspace(self.t0, self.tf, self.n + 1, retstep = True)

    def inicializacion(self):
        if self.inicializado:
            print("La simulación ya está inicializada")
        else:
            self.inicializado = True
            self.desplazamiento[0] = self.x0
            self.velocidad[0] = self.v0
            print(f"Se inicializó la simulación con los valores x0 = {self.x0} y v0 = {self.v0}")

    def euler(self):
        if self.inicializado:
            for i in range(1, self.n + 1):
                self.velocidad[i] = self.velocidad[i - 1] + self.paso_tiempo * self.fuerza(self.desplazamiento, self.velocidad, i)
                self.desplazamiento[i] = self.desplazamiento[i - 1] + self.paso_tiempo * self.velocidad[i]

        else:
            print("Primero inicializa la simulación")

    def graficar_desplazamiento(self):
        plt.figure(figsize = (8, 5))
        plt.plot(self.tiempo, self.desplazamiento)
        plt.xlabel("Tiempo")
        plt.ylabel("Desplazamiento")
        plt.show()

    def graficar_velocidad(self):
        plt.figure(figsize = (8, 5))
        plt.plot(self.tiempo, self.velocidad)
        plt.xlabel("Tiempo")
        plt.ylabel("Velocidad")
        plt.show()

    def proceso(self):
        print("Se va a realizar el proceso de simulación")
        print()

        self.inicializacion()
        self.euler()
        self.graficar_desplazamiento()
        self.graficar_velocidad()

        print()
        print("Se terminó el proceso de simulación")