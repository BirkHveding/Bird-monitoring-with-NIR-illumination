import os
import cv2

def convert_to_grayscale(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get the list of files in the source directory
    file_list = os.listdir(source_dir)

    # Iterate over each file in the source directory
    for file_name in file_list:
        # Construct the full path of the source file
        source_path = os.path.join(source_dir, file_name)

        # Check if the current file is a regular file
        if os.path.isfile(source_path):
            # Read the image
            image = cv2.imread(source_path)

            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Construct the new filename with "_gray" suffix
            new_file_name = os.path.splitext(file_name)[0] + "_gray.jpg"

            # Construct the full path of the destination file
            destination_path = os.path.join(destination_dir, new_file_name)

            # Save the grayscale image to the destination directory
            cv2.imwrite(destination_path, gray_image)

            print(f"Converted {file_name} to grayscale and saved as {new_file_name} in {destination_dir}")



path = r'path'

destination_directory = os.path.join(path, 'gray')

convert_to_grayscale(path, destination_directory)
