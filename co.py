import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import cv2
import numpy as np

drawing = False  # Indicates whether the user is drawing a bounding box
start_x, start_y = None, None  # Initial coordinates of the bounding box

def draw_bbox(event):
    global img_cv, original_img_cv, drawing, start_x, start_y
    if not drawing:
        # Start drawing the bounding box
        start_x, start_y = event.x, event.y
        drawing = True
    else:
        # Finish drawing the bounding box
        end_x, end_y = event.x, event.y
        color = (0, 255, 0)  # Green color
        thickness = 2
        cv2.rectangle(img_cv, (start_x, start_y), (end_x, end_y), color, thickness)
        entry.delete(0, tk.END)
        entry.insert(0, f"{start_x},{start_y},{end_x-start_x},{end_y-start_y}")
        update_display()
        drawing = False

def erase_bbox():
    global img_cv, original_img_cv
    img_cv = np.copy(original_img_cv)
    update_display()

def update_display():
    global img_cv, img_tk
    img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    img_tk = ImageTk.PhotoImage(image=img_pil)
    canvas.config(width=img_tk.width(), height=img_tk.height())
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk

def open_image():
    global img_cv, original_img_cv
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")])
    if file_path:
        img_cv = cv2.imread(file_path)
        original_img_cv = np.copy(img_cv)
        update_display()

root = tk.Tk()
root.title("Image Editor")

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

entry_label = tk.Label(root, text="Enter Coordinates (X,Y,W,H):")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

draw_button = tk.Button(root, text="Draw Bounding Box", command=None)  # Button is not used
draw_button.pack()

erase_button = tk.Button(root, text="Erase Bounding Box", command=erase_bbox)
erase_button.pack()

canvas = tk.Canvas(root)
canvas.pack()

img_cv = np.zeros((500, 500, 3), dtype=np.uint8)
original_img_cv = np.copy(img_cv)
img_tk = None  # Initialize img_tk

canvas.bind("<Button-1>", draw_bbox)

root.mainloop()
