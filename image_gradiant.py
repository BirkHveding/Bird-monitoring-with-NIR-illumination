# This script was writen by ChatGPT and modified by the author of this repo.

import numpy as np
import matplotlib.pyplot as plt
import os

# In[1]:
def plot_pixel_gradients(image_path):
    # Plots the pixel gradient along two columns and one row of an image

    # Load the image
    image = plt.imread(image_path)

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Ask the user to select two columns and one row
    column1 = int(input("Enter the index of the first column (0 to {}): ".format(width - 1)))
    column2 = int(input("Enter the index of the second column (0 to {}): ".format(width - 1)))
    row = int(input("Enter the index of the row (0 to {}): ".format(height - 1)))

    # Extract the selected columns and row from the image
    selected_columns = image[:, [column1, column2], :]
    selected_row = image[row, :, :]

    # Calculate the gradients of pixel values along the selected columns and row
    gradients_columns = np.gradient(selected_columns.mean(axis=2), axis=0)
    gradient_row = np.gradient(selected_row.mean(axis=1))

    # Create a plot to display the pixel value gradients
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the image with lines
    ax1.imshow(image)
    ax1.plot([column1, column1], [0, height - 1], color='orange', linewidth=1) 
    ax1.plot([column2, column2], [0, height - 1], color='red', linewidth=1)
    ax1.plot([0, width - 1], [row, row], color='green', linewidth=1)
    # ax1.set_title('Image with Selected Lines')

    # Plot the pixel value gradients
    ax2.plot(gradients_columns[:, 0], label='Column {}'.format(column1), color='orange')
    ax2.plot(gradients_columns[:, 1], label='Column {}'.format(column2), color='red')
    ax2.plot(gradient_row, label='Row {}'.format(row), color='green')
    ax2.set_xlabel('Pixel Index')
    ax2.set_ylabel('Pixel Gradient')
    # ax2.set_title('Pixel Value Gradients')
    ax2.legend()
    ax2.grid(True)

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()


def plot_pixel_gradients_rows(image_path):
    # Plots the pixel gradient along 3 rows of an image

    # Load the image
    image = plt.imread(image_path)

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Ask the user to select three rows
    rows = []
    for i in range(3):
        row = int(input("Enter the index of row {} (0 to {}): ".format(i+1, height - 1)))
        rows.append(row)

    # Calculate the desired figure height and width to match the image
    dpi = 80  # Adjust the dpi value if needed
    figsize = width * 2, height 

    # Create a plot to display the image and pixel value gradients
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the image with the selected rows
    axs[0].imshow(image)
    for row in rows:
        axs[0].plot([0, width - 1], [row, row], color='green', linewidth=1)
    axs[0].set_title('Image with Selected Rows')

    # Plot the pixel value gradients for the selected rows
    for row in rows:
        # Extract the selected row from the image
        selected_row = image[row, :, :]

        # Calculate the gradients of pixel values along the selected row
        print(selected_row.shape)
        gradient_row = np.gradient(selected_row.mean(axis=1))

        # Plot the pixel value gradient along the row
        axs[1].plot(gradient_row, label='Row {}'.format(row))
    axs[1].set_xlabel('Pixel Index')
    axs[1].set_ylabel('Pixel Gradient')
    axs[1].set_title('Pixel Value Gradients Along Rows')
    axs[1].legend()
    axs[1].grid(True)

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()


def iterate_through_folder(path):
    # Iterates though the images in the folder given by "path" and plots their pixel gradients
    n = 0
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        print(file_path)
        plot_pixel_gradients_rows(file_path)
        n += 1
    if n == 0:
        print('No files found in folder')

# In[2]: 


image_path = r'path'

# iterate_through_folder(image_path)
plot_pixel_gradients_rows(image_path)