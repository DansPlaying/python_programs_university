import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Defino la función de transferencia
numerator = [8, 18, 32]
denominator = [1, 6, 14, 24]
sys = ctrl.TransferFunction(numerator, denominator)

# Genero el vector de tiempo y la señal de entrada
t = np.arange(0, 4, 0.01)
u = np.sin(10 * t)
# Calculo la respuesta forzada del sistema
time, response = ctrl.forced_response(sys, T=t, U=u)
# Creo una figura y un eje
fig, ax1 = plt.subplots()
# Gráfico la respuesta del sistema en el primer eje y
ax1.plot(time, response, label='Respuesta', color='blue')
ax1.set_ylabel('Amplitud', color='blue')
ax1.set_xlabel('Tiempo (segundos)', color='blue')
ax1.set_title('Simulación del resultado lineal')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)

# Creo un segundo eje y para la señal de entrada
ax2 = ax1.twinx()
ax2.plot(t, u, label='Entrada', color='gray')
ax2.tick_params(axis='y', labelcolor='gray')

# Ajusto los límites del eje y para que coincidan
min_val = min(min(response), min(u))
max_val = max(max(response), max(u))
ax1.set_ylim(min_val, max_val)
ax2.set_ylim(min_val, max_val)

# Muestro leyendas
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper right')

# Muestro la gráfica
plt.show()