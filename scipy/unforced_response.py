import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Defino la matriz A, vectores B y C, y escalar D
A = np.array([[-0.8, 3.6, -2.1], [-3, -1.2, 4.8], [3, -4.3, -1.1]])
B = np.array([[0], [-1.1], [-0.2]])
C = np.array([[1.2, 0, 0.6]])
D = -0.6

# Creo el sistema de espacio de estado
G = ctrl.ss(A, B, C, D)

# Defino el estado inicial x0
x0 = np.array([-1, 0, 2])

# Simulo y gráfico la respuesta inicial
time, response = ctrl.initial_response(G, T=np.linspace(0, 10, 100), X0=x0)

# Gráfico la respuesta inicial
plt.plot(time, response)
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')
plt.title('Respuesta a condiciones iniciales')
plt.grid(True)
plt.show()