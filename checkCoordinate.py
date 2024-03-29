# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# import cv2
# import numpy as np

# # Function to draw bounding box on the image
# def draw_bbox():
#     global img_cv
#     x, y, w, h = map(int, entry.get().split(","))
#     color = (0, 255, 0)  # Green color
#     thickness = 2
#     cv2.rectangle(img_cv, (x, y), (x + w, y + h), color, thickness)
#     update_display()

# # Function to update the displayed image
# def update_display():
#     global img_cv
#     img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
#     img_tk = ImageTk.PhotoImage(image=img_pil)
#     label.config(image=img_tk)
#     label.image = img_tk

# # Function to open an image file
# def open_image():
#     global img_cv
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         img_cv = cv2.imread(file_path)
#         update_display()

# # Create the main window
# root = tk.Tk()
# root.title("Image Editor")

# # Create a button to open an image
# open_button = tk.Button(root, text="Open Image", command=open_image)
# open_button.pack()

# # Create an entry for entering coordinates
# entry_label = tk.Label(root, text="Enter Coordinates (X,Y,W,H):")
# entry_label.pack()
# entry = tk.Entry(root)
# entry.pack()

# # Create a button to draw the bounding box
# draw_button = tk.Button(root, text="Draw Bounding Box", command=draw_bbox)
# draw_button.pack()

# # Create a label to display the image
# label = tk.Label(root)
# label.pack()

# # Initialize the image variable
# img_cv = np.zeros((500, 500, 3), dtype=np.uint8)

# # Start the Tkinter main loop
# root.mainloop()


# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# import cv2
# import numpy as np

# # Function to draw bounding box on the image
# def draw_bbox():
#     global img_cv
#     x, y, w, h = map(int, entry.get().split(","))
#     color = (0, 255, 0)  # Green color
#     thickness = 2
#     cv2.rectangle(img_cv, (x, y), (x + w, y + h), color, thickness)
#     update_display()

# # Function to erase the bounding box
# def erase_bbox():
#     global img_cv
#     img_cv = np.copy(original_img_cv)
#     update_display()

# # Function to update the displayed image
# def update_display():
#     global img_cv
#     img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
#     img_tk = ImageTk.PhotoImage(image=img_pil)
#     label.config(image=img_tk)
#     label.image = img_tk

# # Function to open an image file
# def open_image():
#     global img_cv, original_img_cv
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         img_cv = cv2.imread(file_path)
#         original_img_cv = np.copy(img_cv)
#         update_display()

# # Create the main window
# root = tk.Tk()
# root.title("Image Editor")

# # Create a button to open an image
# open_button = tk.Button(root, text="Open Image", command=open_image)
# open_button.pack()

# # Create an entry for entering coordinates
# entry_label = tk.Label(root, text="Enter Coordinates (X,Y,W,H):")
# entry_label.pack()
# entry = tk.Entry(root)
# entry.pack()

# # Create a button to draw the bounding box
# draw_button = tk.Button(root, text="Draw Bounding Box", command=draw_bbox)
# draw_button.pack()

# # Create a button to erase the bounding box
# erase_button = tk.Button(root, text="Erase Bounding Box", command=erase_bbox)
# erase_button.pack()

# # Create a label to display the image
# label = tk.Label(root)
# label.pack()

# # Initialize the image variable
# img_cv = np.zeros((500, 500, 3), dtype=np.uint8)
# original_img_cv = np.copy(img_cv)

# # Start the Tkinter main loop
# root.mainloop()



# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# import cv2
# import numpy as np

# # Function to draw bounding box on the image
# def draw_bbox():
#     global img_cv
#     x, y, w, h = map(int, entry.get().split(","))
#     color = (0, 255, 0)  # Green color
#     thickness = 2
#     cv2.rectangle(img_cv, (x, y), (x + w, y + h), color, thickness)
#     update_display()

# # Function to erase the bounding box
# def erase_bbox():
#     global img_cv
#     img_cv = np.copy(original_img_cv)
#     update_display()

# # Function to update the displayed image
# def update_display():
#     global img_cv
#     img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
#     img_tk = ImageTk.PhotoImage(image=img_pil)
#     label.config(image=img_tk)
#     label.image = img_tk

# # Function to open an image file
# def open_image():
#     global img_cv, original_img_cv
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         img_cv = cv2.imread(file_path)
#         original_img_cv = np.copy(img_cv)
#         update_display()

# # Create the main window
# root = tk.Tk()
# root.title("Image Editor")

# # Create a button to open an image
# open_button = tk.Button(root, text="Open Image", command=open_image)
# open_button.pack()

# # Create an entry for entering coordinates
# entry_label = tk.Label(root, text="Enter Coordinates (X,Y,W,H):")
# entry_label.pack()
# entry = tk.Entry(root)
# entry.pack()

# # Create a button to draw the bounding box
# draw_button = tk.Button(root, text="Draw Bounding Box", command=draw_bbox)
# draw_button.pack()

# # Create a button to erase the bounding box
# erase_button = tk.Button(root, text="Erase Bounding Box", command=erase_bbox)
# erase_button.pack()

# # Create a label to display the image
# label = tk.Label(root)
# label.pack()

# # Initialize the image variable
# img_cv = np.zeros((500, 500, 3), dtype=np.uint8)
# original_img_cv = np.copy(img_cv)

# # Start the Tkinter main loop
# root.mainloop()





# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# import cv2
# import numpy as np

# # Function to draw bounding box on the image
# def draw_bbox():
#     global img_cv
#     x, y, w, h = map(int, entry.get().split(","))
#     color = (0, 255, 0)  # Green color
#     thickness = 2
#     cv2.rectangle(img_cv, (x, y), (x + w, y + h), color, thickness)
#     update_display()

# # Function to erase the bounding box
# def erase_bbox():
#     global img_cv
#     img_cv = np.copy(original_img_cv)
#     update_display()

# # Function to add a new bounding box
# def add_bbox():
#     global img_cv
#     x, y, w, h = map(int, add_entry.get().split(","))
#     color = (0, 255, 0)  # Green color
#     thickness = 2
#     cv2.rectangle(img_cv, (x, y), (x + w, y + h), color, thickness)
#     update_display()

# # Function to update the displayed image
# def update_display():
#     global img_cv
#     img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
#     img_tk = ImageTk.PhotoImage(image=img_pil)
#     label.config(image=img_tk)
#     label.image = img_tk

# # Function to open an image file
# def open_image():
#     global img_cv, original_img_cv
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         img_cv = cv2.imread(file_path)
#         original_img_cv = np.copy(img_cv)
#         update_display()

# # Create the main window
# root = tk.Tk()
# root.title("Image Editor")

# # Create a button to open an image
# open_button = tk.Button(root, text="Open Image", command=open_image)
# open_button.pack()

# # Create an entry for entering coordinates to draw a bounding box
# entry_label = tk.Label(root, text="Enter Coordinates (X,Y,W,H):")
# entry_label.pack()
# entry = tk.Entry(root)
# entry.pack()

# # Create a button to draw the bounding box
# draw_button = tk.Button(root, text="Draw Bounding Box", command=draw_bbox)
# draw_button.pack()

# # Create a button to erase the bounding box
# erase_button = tk.Button(root, text="Erase Bounding Box", command=erase_bbox)
# erase_button.pack()

# # Create an entry for entering coordinates to add a bounding box
# add_entry_label = tk.Label(root, text="Add Coordinates (X,Y,W,H):")
# add_entry_label.pack()
# add_entry = tk.Entry(root)
# add_entry.pack()

# # Create a button to add a bounding box
# add_button = tk.Button(root, text="Add Bounding Box", command=add_bbox)
# add_button.pack()

# # Create a label to display the image
# label = tk.Label(root)
# label.pack()

# # Initialize the image variable
# img_cv = np.zeros((500, 500, 3), dtype=np.uint8)
# original_img_cv = np.copy(img_cv)

# # Start the Tkinter main loop
# root.mainloop()



import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import cv2
import numpy as np

def draw_bbox():
    global img_cv, original_img_cv
    x, y, w, h = map(int, entry.get().split(","))
    color = (0, 255, 0)  # Green color
    thickness = 2
    cv2.rectangle(img_cv, (x, y), (x + w, y + h), color, thickness)
    update_display()

def erase_bbox():
    global img_cv, original_img_cv
    img_cv = np.copy(original_img_cv)
    update_display()

def update_display():
    global img_cv
    img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    img_tk = ImageTk.PhotoImage(image=img_pil)
    label.config(image=img_tk)
    label.image = img_tk

def open_image():
    global img_cv, original_img_cv
    file_path = filedialog.askopenfilename()
    if file_path:
        img_cv = cv2.imread(file_path)
        original_img_cv = np.copy(img_cv)
        update_display()

def on_image_click(event):
    global img_cv, original_img_cv
    x, y = event.x, event.y
    x1 = max(x - 50, 0)
    y1 = max(y - 50, 0)
    x2 = min(x + 50, img_cv.shape[1])
    y2 = min(y + 50, img_cv.shape[0])
    
    cv2.rectangle(img_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)
    entry.delete(0, tk.END)
    entry.insert(0, f"{x1},{y1},{x2-x1},{y2-y1}")
    update_display()

root = tk.Tk()
root.title("Check co-ordinate Image Editor")

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

entry_label = tk.Label(root, text="Enter Coordinates (X,Y,W,H):")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

draw_button = tk.Button(root, text="Draw Bounding Box", command=draw_bbox)
draw_button.pack()

erase_button = tk.Button(root, text="Erase Bounding Box", command=erase_bbox)
erase_button.pack()
label = tk.Label(root)
label.pack()

img_cv = np.zeros((500, 500, 3), dtype=np.uint8)
original_img_cv = np.copy(img_cv)

label.bind("<Button-1>", on_image_click)
label.bind("<Button-2>", on_image_click)

root.mainloop()
