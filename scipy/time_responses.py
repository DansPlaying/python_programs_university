import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Defino la función de transferencia
numerator = [8, 18, 32]
denominator = [1, 6, 14, 24]
sys = ctrl.TransferFunction(numerator, denominator)

# Creo la figura y los subplots
fig, axs = plt.subplots(2)

# Gráfico la respuesta al escalón en el primer subplot
axs[0].set_title('Respuesta al escalón')
time, response = ctrl.step_response(sys)
axs[0].plot(time, response)
axs[0].set_xlabel('Tiempo (segundos)')
axs[0].set_ylabel('Amplitud')

# Gráfico la respuesta al impulso en el segundo subplot
axs[1].set_title('Respuesta al impulso')
time, response = ctrl.impulse_response(sys)
axs[1].plot(time, response)
axs[1].set_xlabel('Tiempo (segundos)')
axs[1].set_ylabel('Amplitud')

# Muestro la gráfica
plt.tight_layout()
plt.show()