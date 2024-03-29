import os
import cv2

def cut_image_horizontally(input_path, output_folder):
    try:
        # Read the input image using OpenCV
        img = cv2.imread(input_path)
        
        # Get the height and width of the image
        height, width = img.shape[:2]
        
        # Calculate the mid-point to split the image horizontally
        mid_point = height // 2
        
        # Split the image into two halves horizontally
        top_half = img[:mid_point, :]
        bottom_half = img[mid_point:, :]
        
        # Save the two halves as separate images in the output folder
        base_filename = os.path.splitext(os.path.basename(input_path))[0]
        #cv2.imwrite(os.path.join(output_folder, f"{base_filename}_top.jpg"), top_half) # To get the top half
        cv2.imwrite(os.path.join(output_folder, f"{base_filename}_bottom.jpg")) # To get the bottom half
        
        print(f"Image '{input_path}' split into two halves and saved successfully.")
    except Exception as e:
        print(f"Error occurred while processing '{input_path}': {e}")

if __name__ == "__main__":
    # Define a list of image paths in the input folder
    image_folder = 'C:/New folder (3)/maharashtra img'  # Replace with the path to your input image folder
    image_paths = [os.path.join(image_folder, image_name) for image_name in os.listdir(image_folder)]

    output_folder = 'C:/New folder (3)/img croped'  # Replace with the path to the output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for input_image_path in image_paths: 
        cut_image_horizontally(input_image_path, output_folder)
