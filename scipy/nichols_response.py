import matplotlib.pyplot as plt
import control as ctrl

# Defino la función de transferencia
numerator = [8, 18, 32]
denominator = [1, 6, 14, 24]
sys = ctrl.TransferFunction(numerator, denominator)

# Creo el diagrama de Nichols
plt.figure()
ctrl.nichols_plot(sys)
plt.title('Diagrama de Nichols')
plt.xlabel('Fase (grados)')
plt.ylabel('Magnitud (dB)')
plt.grid(True)
plt.show()