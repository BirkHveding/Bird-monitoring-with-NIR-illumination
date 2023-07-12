import cv2
import numpy as np
import matplotlib.pyplot as plt
import os



path = r'path/to/images'

def find_files(path, fps):
    matching_files = []  # List to store matching file names
    file_name = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(fps):
                file_path = os.path.join(root, file)
                matching_files.append(file_path)  # Add matching file to the list
                file_name.append(file) 
    
    return matching_files, file_name


def plot_histograms(image_paths, image_names, ylim):
    plt.figure()
    # plt.title('Histogram of Pixel Values')
    plt.xlabel('Pixel Value')
    plt.ylabel('Occurrences')

    for i in range(len(image_paths)):
        image_path = image_paths[i]
        image_name = image_names[i]
        image_name = image_name.replace('_frame5.jpg','')
        
        # Read the image using OpenCV
        image = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculate the histogram using NumPy
        histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

        # Plot the histogram
        # plt.legend(image_name[i])
        plt.plot(histogram)


    # Add a legend with the file names
    plt.legend([name.replace('_frame5.jpg','') for name in image_names])

    # Show the plot
    # plt.ylim([0, ylim])
    plt.show()

# Specify the paths to your image files
image_paths, image_names = find_files(path, 'sky_frame5.jpg')


# Call the function to plot the histograms
plot_histograms(image_paths, image_names, 50)
