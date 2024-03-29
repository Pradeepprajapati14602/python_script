# from PIL import Image

# file = "C:/test/test2/test.jpeg"
# img = Image.open(file)

# filter = ImageEnhance.Color(img)
# filter.enhance(0)
# img.show()

# from PIL import Image, ImageEnhance

# img = Image.open("C:/test/test2/test.jpeg")
# img_data = img.getdata()

# lst=[]
# for i in img_data:

#     # lst.append(i[0]*0.299+i[1]*0.587+i[2]*0.114) ### Rec. 609-7 weights
#     lst.append(i[0]*0.2125+i[1]*0.7174+i[2]*0.0721) ### Rec. 709-6 weights

# new_img = Image.new("L", img.size)
# new_img.putdata(lst)



# new_img.show()


# from PIL import Image

# input_image = Image.open("C:/test/test2/test.jpeg")

# grayscale_data = []
# for pixel in input_image.getdata():
#     gray_value = pixel[0] * 0.2125 + pixel[1] * 0.7174 + pixel[2] * 0.0721
#     grayscale_data.append(int(gray_value))

# # Create a new grayscale image
# grayscale_image = Image.new("L", input_image.size)
# grayscale_image.putdata(grayscale_data)

# # Save the grayscale image
# grayscale_image.save("C:/test/test2/grayscale_output.jpeg")

# # Show the grayscale image (optional)
# grayscale_image.show()

# import cv2

# input_image_path = "C:/test/test2/test.jpeg"
# output_image_path = "C:/test/test2/black_and_white_output.jpg"

# image = cv2.imread(input_image_path)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold_value = 120  
# _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# cv2.imwrite(output_image_path, binary_image)
# cv2.imwrite(input_image_path, binary_image)

# cv2.imshow('Black and White Image', binary_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2

# # Load the image in color
# image = cv2.imread('C:/test/test2/test.jpeg', cv2.IMREAD_COLOR)

# # Convert the image to grayscale
# grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Binary Thresholding
# _, binary_thresholded = cv2.threshold(grayscale_image, 128, 255, cv2.THRESH_BINARY)

# # Adaptive Thresholding
# adaptive_thresholded = cv2.adaptiveThreshold(grayscale_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# # Otsu's Thresholding
# _, otsu_thresholded = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# # Display the original and thresholded images
# cv2.imshow('Original Image', image)
# cv2.imshow('Binary Thresholded Image', binary_thresholded)
# cv2.imshow('Adaptive Thresholded Image', adaptive_thresholded)
# cv2.imshow('Otsu Thresholded Image', otsu_thresholded)

# # Wait for a key press and then close the windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2

# Load the image
image = cv2.imread('C:/test/test2/OGR.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply binary thresholding
threshold_value = 120  # You can adjust this threshold value as needed
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the binary image
cv2.imwrite('C:/test/test2/binary_image.jpg', binary_image)

print("Binary image saved as 'binary_image.jpg'")




