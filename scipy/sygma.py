import numpy as np
import control as ctrl
from scipy.linalg import svd
import matplotlib.pyplot as plt

sys = ctrl.rss(3, 2, 2)
# 3 estados, 2 entradas, 2 salidas (sistema MIMO)

sys.A = np.array([[-0.5, -0.3, -0.2],
                  [0, -1.3, -1.7],
                  [0.4, 1.7, -1.3]]) 

U, S, Vt = svd(sys.A)
frecuencias = np.logspace(-2, 2, num=100)  
S_dB = 20 * np.log10(S)

# Trama de valores singulares en dB
plt.semilogx(frecuencias, S_dB)
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Valores Singulares (dB)')
plt.title('Valores singulares')
plt.grid(True)
plt.legend()
plt.show()