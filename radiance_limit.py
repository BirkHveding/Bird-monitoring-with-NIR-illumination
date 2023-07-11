import matplotlib.pyplot as plt
import numpy as np

alpha = np.linspace(0, 0.1020, 2000)
L = 6000/alpha
L_min = 6000/0.1   
L_max = 6000/0.0017


L_full = L_max*(alpha < 0.0017) + L*(alpha >= 0.0017)*(0.1> alpha) + L_min*(alpha >= 0.1)


plt.plot(alpha, L_full, label='L$_{IR}$', color='blue')
plt.axvline(x=0.0017, color='gray', linestyle='--')
plt.axvline(x=0.1, color='gray', linestyle='--')
plt.text(0.0022, 100000, '$\\alpha$ = 0.0017', rotation=90, color='gray')
plt.text(0.1005, 100000, '$\\alpha$ = 0.1', rotation=90, color='gray')
plt.xlabel('$\\alpha$ [rad]')
plt.ylabel('L [W/m^2sr]')
plt.grid()
plt.legend()
plt.show()
