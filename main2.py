# import pytesseract
# from PIL import Image
# import os

# # Image ka path
# image_path = 'path_to_your_image.jpg'

# # Desired text
# desired_text = '21/07/23'

# # Text ko image se extract karna
# try:
#     extracted_text = pytesseract.image_to_string(Image.open(image_path))
# except Exception as e:
#     print("Error while extracting text:", str(e))
#     extracted_text = ""

# # Check karein ki desired text image mein hai ya nahi
# if desired_text in extracted_text:
#     # Agar desired text image mein hai, to usko udhar he rahne dein
#     print("Text found, image will remain in the same location.")
# else:
#     # Agar desired text image mein nahi hai, to use dusri file mein move kar dein
#     new_path = 'path_to_xyz_folder/image.jpg'
#     os.rename(image_path, new_path)
#     print("Text not found, image moved to XYZ folder.")

import os
import pytesseract
from PIL import Image

# Source folder (images will be checked here)
source_folder = 'images/'

# Destination folder for moving images
destination_folder = 'seperate/'

# Desired text to check
desired_text = '21/07/23'

# Loop through each file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(source_folder, filename)
        
        # Extract text from image
        try:
            extracted_text = pytesseract.image_to_string(Image.open(image_path))
        except Exception as e:
            print("Error while extracting text from", filename, ":", str(e))
            extracted_text = ""
        
        # Check if desired text is present in extracted text
        if desired_text in extracted_text:
            # If desired text is found, image will remain in the same location
            print("Text found in", filename, "- Image will remain in the same location.")
        else:
            # If desired text is not found, move image to destination folder
            new_path = os.path.join(destination_folder, filename)
            os.rename(image_path, new_path)
            print("Text not found in", filename, "- Image moved to destination folder.")

print("Process completed.")

# import os
# import pytesseract
# from PIL import Image
# import xml.etree.ElementTree as ET

# # Source folder (images and XML files will be checked here)
# source_folder = 'images/'

# # Destination folder for moving images
# destination_folder = 'seperate/'

# # Desired text to check
# desired_text = '21/07/23'

# # Loop through each XML file in the source folder
# for filename in os.listdir(source_folder):
#     if filename == 'frames.xml':
#         xml_path = os.path.join(source_folder, filename)
#         tree = ET.parse(xml_path)
#         root = tree.getroot()

#         for frame in root.findall('frame'):
#             x_coordinate = int(frame.find('x').text)
#             y_coordinate = int(frame.find('y').text)
#             image_filename = frame.find('image_filename').text
#             image_path = os.path.join(source_folder, image_filename)

#             try:
#                 img = Image.open(image_path)
#                 cropped_img = img.crop((x_coordinate, y_coordinate, x_coordinate + 100, y_coordinate + 30))
#                 extracted_text = pytesseract.image_to_string(cropped_img)
#             except Exception as e:
#                 print("Error while extracting text from", image_filename, ":", str(e))
#                 extracted_text = ""

#             if desired_text in extracted_text:
#                 print("Text found in", image_filename, "- Image will remain in the same location.")
#             else:
#                 new_path = os.path.join(destination_folder, image_filename)
#                 os.rename(image_path, new_path)
#                 print("Text not found in", image_filename, "- Image moved to destination folder.")

# print("Process completed.")

