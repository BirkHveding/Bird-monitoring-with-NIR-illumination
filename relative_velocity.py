# This script was writen by ChatGPT and modified by the author of this repo.

import numpy as np
import matplotlib.pyplot as plt

# Define the distance range from 0.5m to 200m
distances = np.linspace(0.5, 200, 100)

# Calculate the perceived velocity at each distance
perceived_velocity = 0.31

# Calculate the actual velocity based on perceived velocity and distance
actual_velocity = perceived_velocity * distances/0.5

# Convert actual velocity to km/h
actual_velocity_kmh = actual_velocity * 3.6

# Create the figure and axes
fig, ax1 = plt.subplots()

# Plot the velocity-distance relationship on the left y-axis
ax1.plot(distances, actual_velocity, color='black')
ax1.set_xlabel('Distance (m)')
ax1.set_ylabel('Actual Velocity (m/s)', color='black')
ax1.tick_params('y', colors='black')
ax1.grid(True)

# Create a twin axis on the right for km/h
ax2 = ax1.twinx()

# Plot the velocity-distance relationship on the right y-axis in km/h
ax2.plot(distances, actual_velocity_kmh, color='#21618C')
ax2.set_ylabel('Actual Velocity (km/h)', color='black')
ax2.tick_params('y', colors='black')

# Add a legend
lines = [ax1.lines[0], ax2.lines[0]]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper left')

# Show the plot
plt.grid(True)
plt.show()