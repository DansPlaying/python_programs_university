import numpy as np
import matplotlib.pyplot as plt

# Defino el rango de tiempo
t = np.linspace(0, 20, 1000)

# Defino las señales
signal1 = 1 - 0.91 * np.exp(-0.34*t)*np.cos(0.56*t) -\
0.96 * np.exp(-0.34*t)*np.sin(0.56*t)-0.10*np.exp(-2.32*t)
signal2 = 1 - 0.86 * np.exp(-0.24*t)*np.cos(0.86*t) -\
0.63 * np.exp(-0.24*t)*np.sin(0.86*t)-0.13*np.exp(-2.52*t)
signal3 = 1 - 0.84 * np.exp(-0.16*t)*np.cos(1.05*t) -\
0.52 * np.exp(-0.16*t)*np.sin(1.05*t)-0.15*np.exp(-2.67*t)
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

