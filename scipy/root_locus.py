import matplotlib.pyplot as plt
import control as ctrl

# Definir la función de transferencia
G = -ctrl.TransferFunction([2, 1], [1, 3, 2])  
# G = -(2*s + 1) / (s^2 + 3*s + 2)
k = 0.7
T = ctrl.feedback(G * k, 1)

# Gráfico el lugar de las raíces
plt.figure()
ctrl.root_locus(T)
plt.title('Lugar de las Raíces del Sistema')
plt.xlabel('Parte Real (1/segundos)')
plt.ylabel('Parte Imaginaria (1/segundos)')
plt.grid(True)
plt.show()