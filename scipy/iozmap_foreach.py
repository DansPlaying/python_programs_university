import matplotlib.pyplot as plt
import numpy as np
import control as ctrl

# Creo un sistema de espacio de estados MIMO
sys = ctrl.rss(3, 2, 2)
# 3 estados, 2 entradas, 2 salidas (sistema MIMO)
# sys.A = [[-0.5, -0.3, -0.2],
#          [0, -1.3, -1.7],
#          [0.4, 1.7, -1.3]]
# Obtengo los polos y ceros del sistema MIMO
poles, zeros = ctrl.pole(sys), ctrl.zero(sys)

# Gráfico el mapa de polos y ceros para cada par de I/O
num_inputs, num_outputs = sys.inputs, sys.outputs
for inp in range(num_inputs):
    for out in range(num_outputs):
        plt.figure()
        plt.scatter(poles[out*num_inputs+inp].real, poles[out*num_inputs+inp].imag, marker='x', color='red', label='Polos')
        plt.scatter(zeros[out*num_inputs+inp].real, zeros[out*num_inputs+inp].imag, marker='o', color='blue', label='Ceros')
        plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
        plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
        plt.xlabel('Parte Real')
        plt.ylabel('Parte Imaginaria')
        plt.title(f'Mapa de Polos y Ceros (PZ map) para I/O par ({inp+1}, {out+1})')
        plt.legend()
        plt.grid(True)
        plt.show()