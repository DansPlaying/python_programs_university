import matplotlib.pyplot as plt
import control as ctrl

# Crear un sistema de espacio de estados aleatorio MIMO
sys = ctrl.rss(3, 2, 2)  
# 3 estados, 2 salidas, 2 entradas (sistema MIMO)
# DefinO la matriz de coeficientes 'A'
sys.A = [[-0.5, -0.3, -0.2],
         [0, -1.3, -1.7],
         [0.4, 1.7, -1.3]]

print(sys)
# ObtenGO la respuesta al escalón para cada 
# combinación de entrada-salida
time, response = ctrl.step_response(sys)

# Gráfico las respuestas al escalón para cada canal de entrada-salida
# fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# for i in range(2):  # Recorro las entradas
#     for j in range(2):  # Recorro las salidas
#         axs[i, j].plot(time, response[j, i, :])  
#         # Gráfico la respuesta correspondiente
#         axs[i, j].set_title(f'Respuesta al Escalón - Entrada {i+1}, Salida {j+1}')
#         axs[i, j].set_xlabel('Tiempo (segundos)')
#         axs[i, j].set_ylabel('Amplitud')
#         axs[i, j].grid(True)

# plt.tight_layout()
# plt.show()

plt.figure(figsize=(10, 8))

# Gráfico las respuestas al escalón para cada canal de entrada-salida
for i in range(2):  # Recorro las entradas
    for j in range(2):  # Recorro las salidas
        plt.plot(time, response[j, i, :], label=f'Entrada {i + 1}, Salida {j + 1}')

# Establezco etiquetas y título
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')
plt.title('Respuestas al Escalón')
plt.legend()  # Muestro leyenda

plt.grid(True)
plt.tight_layout()
plt.show()
