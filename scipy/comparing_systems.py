import matplotlib.pyplot as plt
import numpy as np
import control as ctrl

# Defino la función de transferencia G
numerator = [2, 1]
denominator = [1, 3, 2]
G = ctrl.TransferFunction(numerator, denominator)

# Defino los valores de ganancia k
k_values = [0.7, 0.4, 1]

# Creo una figura para la gráfica
plt.figure()

# Itero sobre los valores de ganancia
for k in k_values:
    r = ctrl.feedback(-G * k, 1)
    t, y = ctrl.step_response(r)
    plt.plot(t, y, label=f'k = {k}')

# Configuro la gráfica
plt.title('Respuesta al Escalón con Diferentes Valores de Ganancia')
plt.xlabel('Tiempo(segundos)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()