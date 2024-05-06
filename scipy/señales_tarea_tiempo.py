import numpy as np
import matplotlib.pyplot as plt

# Defino el rango de tiempo
t = np.linspace(0, 20, 1000)

# Defino las señales
signal1 = -0.75 + 0.5 * t + np.exp(-t) - 0.25 * np.exp(-2 * t)
signal2 = -1.5 + t + 2*np.exp(-t) - 0.5 * np.exp(-2 * t)
signal3 = -2.25 + 1.5 * t + 3 * np.exp(-t) - 0.75 * np.exp(-2 * t)

# Gráfico las señales
plt.figure()
plt.plot(t, signal1, label='k1')
plt.plot(t, signal2, label='k2')
plt.plot(t, signal3, label='k3')

# Agrego etiquetas, leyenda y muestro
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Salida variando con la K')
plt.legend()
plt.show()

