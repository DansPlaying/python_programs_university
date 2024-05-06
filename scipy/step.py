import matplotlib.pyplot as plt
import control as ctrl

# Defino la función de transferencia
G = ctrl.TransferFunction([2, 1], [1, 3, 2]) 
 # G = -(2*s + 1) / (s^2 + 3*s + 2)
k = 0.7
T = ctrl.feedback(-G * k, 1)

# Obtener la respuesta al escalón
time, response = ctrl.step_response(T)

# Gráfico la respuesta al escalón
plt.figure()
plt.plot(time, response)
plt.title('Respuesta al Escalón del Sistema')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()