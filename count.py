# To check whether an image exists or not, you can use the `os.path` module in Python. Here's an example code:

# ```python
import os

def check_image_exists(image_path):
    if os.path.exists(image_path):
        print("Image exists")
    else:
        print("Image does not exist")

# Example usage
image_path = "C:/Users/Dell/Downloads/00000108_20231111_081505/00000108_20231111_081459721_GPT.jpeg"
check_image_exists(image_path)
# ```

# In this code, we define a function `check_image_exists` that takes an `image_path` as input. We then use the `os.path.exists` function to check if the image file exists at the given path. If it exists, we print "Image exists", otherwise we print "Image does not exist".

# You can replace `"path/to/image.jpg"` with the actual path to the image you want to check.