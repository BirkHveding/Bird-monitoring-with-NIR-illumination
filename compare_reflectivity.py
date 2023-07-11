# This script was writen by ChatGPT and modified by the author of this repo.
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_average_pixel(image):
    # Calculate the average pixel value of the image
    average_pixel = np.mean(image)
    return average_pixel

def display_images(images, files):
    # Create a figure with subplots for displaying the images
    fig, axes = plt.subplots(1, len(images), figsize=(12, 5))
    # fig.suptitle('Images and Average Pixel Values')

    # Display the images and calculate the average pixel value for each image
    for i, (image, filename) in enumerate(zip(images, files)):
        if 'black' in filename:
            n = 2
            m = str(2) + '. Black'
        elif 'white' in filename:
            n = 0 # Want to place the bird in the middel, for better comparison
            m = str(3) + '. White'
        else:
            n = 1
            m = str(1) + '. Bird'


        axes[n].imshow(image)
        axes[n].set_title('Cropp {}'.format(m))
        axes[n].axis('off')

        # Calculate the average pixel value
        average_pixel = calculate_average_pixel(image)
        axes[n].text(0.5, -0.10, 'Avg Pixel: {:.2f}'.format(average_pixel), transform=axes[n].transAxes,
                     horizontalalignment='center', verticalalignment='center', fontsize=12)

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()

def get_images_from_directory(directory, var):
    # Get the list of image files in the directory
    image_files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png')) and var in f]

    # Read the images and store them in a list
    images = []
    files = []
    for file in image_files:
        image_path = os.path.join(directory, file)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        files.append(file)
        images.append(image)

    return images, files

# Specify the directory containing the images
directory = r'path'

# Get the images from the directory
images, files = get_images_from_directory(directory, 'cropped_fulmar')

# Display the images and their average pixel values
display_images(images, files)


