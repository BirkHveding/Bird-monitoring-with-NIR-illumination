import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def cone_path(folder_path):
    # Plots the path of the light cone over 4 seconds for 30 FPS

    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    image_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
    # Sort the image files alphabetically
    # image_files.sort()

    # Empty list to store the x-axis indices
    indices = []

    # Iterate through the image files
    for image_file in image_files:
        # Load the image
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Apply Otsu's thresholding
        _, thresh = cv2.threshold(image, 20, 255, cv2.THRESH_BINARY)

        # Find contours of the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour area
        max_area = 0
        largest_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                largest_contour = contour

        # Find the centroid of the largest contour
        M = cv2.moments(largest_contour)
        cX = int(M["m10"] / M["m00"])

        # Append the x-axis index to the list
        indices.append(cX)

    # Convert the indices to time values
    time_values = np.arange(0, 4, 1/30)

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the x-axis indices against every second time value
    ax.plot(indices, time_values)
    

    # plot red dots at each point
    ax.plot(indices, time_values, 'ro')
    # add number to each point
    for i, txt in enumerate(indices):
        ax.annotate(str(i+1), (indices[i], time_values[i]))


    # Set plot labels and title
    ax.set_ylabel('Time (seconds)')
    ax.set_ylim(0, 1)
    ax.set_xlabel('Image X-axis Index')
    # ax.set_title('X-axis Index Variation Over Time')

    # Display the plot
    plt.show()

def fourier_images(folder_path):
    # Generates a fourier fransform from the light-cone cycles.

    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    image_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
    # Sort the image files alphabetically
    # image_files.sort()

    # Empty list to store the x-axis indices
    indices = []

    # Iterate through the image files
    for image_file in image_files:
        # Load the image
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Apply Otsu's thresholding
        _, thresh = cv2.threshold(image, 20, 255, cv2.THRESH_BINARY)

        # Find contours of the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour area
        max_area = 0
        largest_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                largest_contour = contour

        # Find the centroid of the largest contour
        M = cv2.moments(largest_contour)
        cX = int(M["m10"] / M["m00"])

        # Append the x-axis index to the list
        indices.append(cX)

    # Convert the indices to time values
    time_values = np.arange(0, 4, 1/30)

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the values
    ax.plot(indices, time_values, 'r.')
    
    # Perform Fourier transform
    frequencies = np.fft.fft(indices)
    frequencies = np.fft.fftshift(frequencies)
    freq_values = np.fft.fftfreq(len(indices), 1/30)
    freq_values = np.fft.fftshift(freq_values)

    # Create the Fourier transform plot
    fig, ax2 = plt.subplots(figsize=(8, 3))
    ax2.plot(freq_values, np.abs(frequencies))
    fig.subplots_adjust(bottom=0.2)
    ax2.set_xlim(0, 15)
    ax2.set_ylim(0, 40000)
    ax2.grid()
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Amplitude')
    

    max_freq = 0
    max_amp = 0
    for i, freq in enumerate(freq_values):
        if freq > 2:
            if np.abs(frequencies[i]) > max_amp:
                max_freq = freq
                max_amp = np.abs(frequencies[i])
    
    ax2.plot(max_freq, max_amp, 'ro')
    ax2.annotate(str(max_freq), (max_freq, max_amp))

    # Set plot labels and title
    ax.set_ylabel('Time (seconds)')
    
    ax.set_xlabel('X-axis Index')
    ax.set_title('X-axis Index Variation Over Time')

    # Display the plots
    plt.show()

# Specify the folder containing the images
folder_path = r'path'

cone_path(folder_path)
fourier_images(folder_path)













