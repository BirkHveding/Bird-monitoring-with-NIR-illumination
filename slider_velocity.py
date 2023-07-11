import numpy as np
import matplotlib.pyplot as plt

def plot_slider_velocity():
    # Constants
    e = 0.057
    r = 0.023
    l = 0.142
    w = 4 * 2 *np.pi

    crank_radius = 0.023  # meters
    connecting_rod_length = 0.142  # meters
    angular_velocity = 2*np.pi  # radians per second

    # Time range
    t = np.linspace(0, 1, 1200)  # 120 points for 2 seconds at 60 FPS

    # Calculate slider velocity as a function of time
    slider_velocity =  - angular_velocity * (crank_radius * np.sin(0 + angular_velocity*t) + (crank_radius**2 * np.sin(0 + angular_velocity*t)*np.cos(0 + angular_velocity*t))/(connecting_rod_length**2 + crank_radius**2*np.sin(0 + angular_velocity*t)**2)**(1/2))
    th = w*t
    pos = -((r+l)**2 - e**2)**0.5 + r*(np.cos(w*t) + (l/r)*(1-((e/l) - np.sin(th)*r/l)**2)**0.5)

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the slider velocity and position
    # ax.plot(slider_velocity, t, color='blue', label='Slider Velocity')
    ax.plot(pos, t, color='blue', label='Slider position')

    # # Add dots every 1/30 second
    dots_t = np.arange(0, 2 + 1/20, 1/30)
    dots_velocity = np.interp(dots_t, t, pos)
    ax.scatter(dots_velocity, dots_t, color='red', label='60 FPS')

    # Set plot labels and title
    ax.set_ylabel('Time (seconds)')
    ax.set_xlabel('Slider position (m)')
    # ax.set_title('Slider Velocity in a Slider-Crank Mechanism')

    # Set plot limits and legend
    ax.set_ylim(0, 1)
    ax.set_xlim(np.min(pos), np.max(pos))
    ax.legend(loc='upper right')

    # Display the plot
    plt.show()

# Call the function to generate the plot
plot_slider_velocity()
