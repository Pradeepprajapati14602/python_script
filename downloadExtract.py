# import zipfile
# import os

# # Specify the path to the zip file and the destination folder
# zip_file_path = 'path/to/yourfile.zip'
# destination_folder = 'path/to/destination_folder'

# # Create the destination folder if it doesn't exist
# os.makedirs(destination_folder, exist_ok=True)

# # Open and extract the zip file
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(destination_folder)

# print(f"Extracted {zip_file_path} to {destination_folder}")

# import zipfile
# import os

# # Specify the source folder containing the zip files and the destination folder
# source_folder = 'C:/test'
# destination_folder = 'C:/test2'

# # Create the destination folder if it doesn't exist
# os.makedirs(destination_folder, exist_ok=True)

# # Iterate over the files in the source folder
# for filename in os.listdir(source_folder):
#     if filename.endswith('.zip'):
#         # Construct the full path to the zip file
#         zip_file_path = os.path.join(source_folder, filename)

#         # Open and extract the zip file into the destination folder
#         with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#             zip_ref.extractall(destination_folder)

#         print(f"Extracted {zip_file_path} to {destination_folder}")

# print("Extraction complete.")

import py7zr
import os

# Specify the source folder containing the .7z files and the destination folder
source_folder = 'C:/test'
destination_folder = 'C:/test2'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Iterate over the files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.7z'):
        # Construct the full path to the .7z file
        seven_zip_file_path = os.path.join(source_folder, filename)

        # Open and extract the .7z file into the destination folder
        with py7zr.SevenZipFile(seven_zip_file_path, mode='r') as zip_ref:
            zip_ref.extractall(destination_folder)

        print(f"Extracted {seven_zip_file_path} to {destination_folder}")

print("Extraction complete.")
