import numpy as np
import matplotlib.pyplot as plt

# In[1]: Define the function of the area of the projected square

def projected_area(th1, th2, dist):
    # Calculates the area of the projected square at a certain distance
    # th1 and th2 are orthogonal, total angles of the FOV
    th1 = np.radians(th1)
    th2 = np.radians(th2)
    
    width_dist1 = 2*dist*np.tan(th1/2)
    width_dist2 = 2*dist*np.tan(th2/2) 
    area = width_dist1 * width_dist2
    return area


# In[2]: plot the energy projected area for different angles at 200m


# define the angles
th1 = 40
th2 = 40

th7 = 20
th8 = 20

th9 = 10
th10 = 10

# define the distance
dist = np.linspace(0, 200, 1000) 

# calculate the projected area
projectedArea = projected_area(th1, th2, dist)

# plot the projected area
plt.plot(dist, 20/projectedArea, label='P:20W, FOV: ' + str(th1) + 'deg')
plt.plot(dist, 80/projectedArea, label='P:80W, FOV: ' + str(th1) + 'deg')
plt.plot(dist, 20/projected_area(th7, th8, dist), label='P:20W, FOV: ' + str(th7) + 'deg')
plt.plot(dist, 20/projected_area(th9, th10, dist), label='P:20W, FOV: ' + str(th9) + 'deg')


plt.xlabel('Distance from point source [m]')
plt.ylabel('Irradiance E [W/m^2]')
plt.yscale('log')
plt.legend()
plt.grid()
plt.show()
