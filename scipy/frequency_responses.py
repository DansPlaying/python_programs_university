import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Definir la función de transferencia para el primer sistema (filtro pasa-alto)
numerator_1 = [1,2,1]
denominator_1 = [1]
sys_1 = ctrl.TransferFunction(numerator_1, denominator_1)

# Definir la función de transferencia para el segundo sistema (filtro pasa-alto)
numerator_2 = [1, 1]
denominator_2 = [1, 0]
sys_2 = ctrl.TransferFunction(numerator_2, denominator_2)

# Crear el diagrama de Bode para ambos sistemas
mag_1, phase_1, omega_1 = ctrl.bode_plot(sys_1, Plot=False)
mag_2, phase_2, omega_2 = ctrl.bode_plot(sys_2, Plot=False)

# Convertir la fase a dB para ambos sistemas
phase_dB_1 = 20 * np.log10(np.abs(phase_1))
phase_dB_2 = 20 * np.log10(np.abs(phase_2))

# Gráfico el diagrama de Bode para la fase en dB de ambos sistemas
plt.semilogx(omega_1, phase_dB_1,)
plt.semilogx(omega_2, phase_dB_2,)
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Valores singulares (dB)')
plt.title('Valores singulares')
plt.grid(True)
plt.legend()
plt.show()
