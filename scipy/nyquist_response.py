import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Defino la función de transferencia
numerator = [8, 18, 32]
denominator = [1, 6, 14, 24]
sys = ctrl.TransferFunction(numerator, denominator)

# Creo el diagrama de Nyquist
plt.figure()
ctrl.nyquist_plot(sys)
plt.title('Diagrama de Nyquist')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.grid(True)
plt.show()