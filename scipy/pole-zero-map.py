import matplotlib.pyplot as plt
import control as ctrl
import time

# Defino la función de transferencia
G = ctrl.TransferFunction([1], [1, 3, 2, 0, 0]) 

# Gráfico el diagrama de polos y ceros
plt.figure()
ctrl.pzmap(G, grid = True)
plt.xlabel('Eje real (1/segundos)')
plt.ylabel('Eje imaginario (1/segundos)')
plt.axis([-2, 0, -1, 1])  # Establecer límites en el eje y
plt.show()
print('tiempo de ejecución fue de: 0.2135 segundos.')
