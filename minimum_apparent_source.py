import matplotlib.pyplot as plt
import numpy as np


P = np.linspace(0, 100, 1000)
lim = 100
A_source = P/100

plt.plot(P, A_source, label='Minimum Apparent Source Area')

plt.xlabel('Power [W]')
plt.ylabel('Area [m^2]')
plt.grid()

plt.legend()
plt.show()

E = np.linspace(0, 100, 1000)
omega = E/(6*10**4)
sqrt_omega = np.sqrt(omega)


plt.subplot(2, 1, 1)
plt.plot(E, omega, label='$\Omega$')
plt.xlabel('Irradiance [W/m^2]')
plt.ylabel('Solid Angle [sr]')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(E, np.rad2deg(sqrt_omega), label='$\Omega^{0.5}$')
plt.xlabel('Irradiance [W/m^2]')
plt.ylabel('Angle [deg]')
plt.grid()
plt.legend()



plt.tight_layout()
plt.show()





