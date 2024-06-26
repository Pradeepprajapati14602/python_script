# from paddleocr import PaddleOCR
# from PIL import Image
# import os
# import numpy as np
# import pandas as pd
# import uuid
# import xml.etree.ElementTree as ET

# def generate_unique_filename():
#     unique_id = str(uuid.uuid4())
#     return f"image_{unique_id}.jpg"

# def ImgtoOcr(folder_path):
#     ocr = PaddleOCR(lang='en')

#     data = []

#     for filename in os.listdir(folder_path):
#         image_path = os.path.join(folder_path, filename)
#         image = Image.open(image_path).convert("RGB")
#         image_name = os.path.basename(image_path)

#         # Read XML file and get bounding box coordinates
#         xml_file_path = os.path.join(folder_path, filename.replace(".png", ".xml"))
#         tree = ET.parse('frame.xml')
#         root = tree.getroot()
#         xmin = int(root.find(".//xmin").text)
#         ymin = int(root.find(".//ymin").text)
#         xmax = int(root.find(".//xmax").text)
#         ymax = int(root.find(".//ymax").text)

#         # Crop the image based on bounding box coordinates
#         cropped_image = image.crop((xmin, ymin, xmax, ymax))

#         result = ocr.ocr(np.array(cropped_image))

#         text_data = ""
#         for line in result[0]:
#             text = line[1][0]
#             coordinates = line[0]
#             text_data += f"{text} (Coordinates: {coordinates}), "

#         data.append({'Image Name': image_name, 'Extracted Text': text_data})

#     df = pd.DataFrame(data)
#     excel_file_path = 'DEN - Delhi.xlsx'
#     df.to_excel(excel_file_path, index=False)

#     print(f"OCR results with coordinates saved to Excel file: {excel_file_path}")

# folder_path ='images'
# ImgtoOcr(folder_path)


import os
import shutil
from paddleocr import PaddleOCR

# Source folder (contains all images)
source_folder = 'images/'

# Destination folder for moving images
destination_folder = 'img/'

# Desired text to check
desired_text = '7/12/2002'

# Coordinates
x_coordinate = 990
y_coordinate = 790

# Initialize PaddleOCR
ocr = PaddleOCR()

# Function to extract text using PaddleOCR
def extract_text(image_path, x, y):
    image = ocr.ocr(image_path)
    extracted_text = []
    for result in image:
        for line in result:
            text = line[-2][0]
            if isinstance(text, list):  # Handle the case where text is a list
                text = ' '.join(text)
            text_x = line[0][0][0]  # Extract the x-coordinate value from the list
            text_y = line[0][0][1]  # Extract the y-coordinate value from the list
            if x <= text_x <= x + 100 and y <= text_y <= y + 30:
                extracted_text.append(text)
    return ' '.join(extracted_text)

# Loop through each image in the source folder
for filename in os.listdir(source_folder):
    if filename.startswith('frame') and (filename.endswith('.jpg') or filename.endswith('.png')):
        image_path = os.path.join(source_folder, filename)

        # Extract text using PaddleOCR
        extracted_text = extract_text(image_path, x_coordinate, y_coordinate)

        # Check if desired text is present
        if desired_text in extracted_text:
            print("Text found in", filename, "- Image will remain in the same location.")
        else:
            new_path = os.path.join(destination_folder, filename)
            shutil.move(image_path, new_path)
            print("Text not found in", filename, "- Image moved to destination folder.")

print("Process completed.")
