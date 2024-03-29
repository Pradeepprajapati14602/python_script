# import cv2

# def get_channel_and_set_up_box(image_path):
#     # Read the image
#     image = cv2.imread(image_path)
    
#     # Get the number of channels in the image
#     num_channels = image.shape[2]
    
#     # Determine the channel based on the number of channels
#     if num_channels == 1:
#         channel = "Grayscale"
#     elif num_channels == 3:
#         channel = "RGB"
#     else:
#         channel = "Unknown"
    
#     # Determine the set up box based on the channel
#     if channel == "Grayscale":
#         set_up_box = "Standard"
#     elif channel == "RGB":
#         set_up_box = "HD"
#     else:
#         set_up_box = "Unknown"
    
#     return channel, set_up_box

# # Example usage
# image_path = "C:/Users/Dell/Downloads/00000108_20231111_081455/00000108_20231110_162900150_EPG.jpeg"
# channel, set_up_box = get_channel_and_set_up_box(image_path)
# print("Channel:", channel)
# print("Set up box:", set_up_box)




# import cv2
# import pytesseract

# def get_channel_and_set_top_box(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply OCR to the grayscale image
#     text = pytesseract.image_to_string(gray)

#     # Find the channel name and set top box name in the OCR text
#     channel_name = ""
#     set_top_box_name = ""

#     # Split the OCR text into lines
#     lines = text.split("\n")

#     # Iterate over each line
#     for line in lines:
#         # Check if the line contains the channel name
#         if "channel" in line.lower():
#             channel_name = line.split(":")[1].strip()
#         # Check if the line contains the set top box name
#         if "set top box" in line.lower():
#             set_top_box_name = line.split(":")[1].strip()

#     return channel_name, set_top_box_name

# # Example usage
# image_path = "C:/Users/Dell/Downloads/00000108_20231111_081455/00000108_20231110_162900150_EPG.jpeg"
# channel, set_top_box = get_channel_and_set_top_box(image_path)
# print("Channel Name:", channel)
# print("Set Top Box Name:", set_top_box)


import paddlehub as hub

def recognize_image(image_path):
    ocr = hub.Module(name="chinese_ocr_db_crnn_server")
    result = ocr.recognize_text(images=[image_path])
    return result[0]['data']

def get_channel_name(image_path):
    channel_name = ""
    text = recognize_image(image_path)
    # Extract channel name from the recognized text
    # You can use regular expressions or any other method to extract the channel name
    # and assign it to the channel_name variable
    return channel_name

def get_setup_box_name(image_path):
    setup_box_name = ""
    text = recognize_image(image_path)
    # Extract setup box name from the recognized text
    # You can use regular expressions or any other method to extract the setup box name
    # and assign it to the setup_box_name variable
    return setup_box_name

image_path = "C:/Users/Dell/Downloads/00000108_20231111_081455/00000108_20231110_162900150_EPG.jpeg"
channel_name = get_channel_name(image_path)
setup_box_name = get_setup_box_name(image_path)

print("Channel Name:", channel_name)
print("Setup Box Name:", setup_box_name)