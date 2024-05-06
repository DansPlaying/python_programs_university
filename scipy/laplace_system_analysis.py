import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Defino el rango de tiempo hasta 20 segundos
t = np.linspace(0, 20, 1000)

# Defino la función de transferencia
system1 = ctrl.TransferFunction(1, [1, 3, 2, 1])
system2 = ctrl.TransferFunction(2, [1, 3, 2, 2])
system3 = ctrl.TransferFunction(3, [1, 3, 2, 3])

time, response1 = ctrl.step_response(system1, T = t)
time2, response2 = ctrl.step_response(system2, T = t)
time3, response3 = ctrl.step_response(system3, T = t)

# Gráfico la respuesta al escalón
plt.figure()
plt.plot(time, response1, label='k1')
plt.plot(time2, response2, label='k2')
plt.plot(time3, response3, label='k3')
plt.title('Respuesta al Escalón del Sistema variando k')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

