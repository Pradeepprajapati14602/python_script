import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import cv2
import numpy as np
import paddle
from paddleocr import PaddleOCR

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

        # Extract text using PaddleOCR
        bbox = [start_x, start_y, end_x, end_y]
        cropped_image = original_img_cv[bbox[1]:bbox[3], bbox[0]:bbox[2]]
        result = ocr.ocr(cropped_image)
        text = ' '.join([line[1][0] for line in result[0]])

        # Print the extracted text
        print("Extracted Text:", text)

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

# Initialize PaddleOCR model
ocr = PaddleOCR()

root = tk.Tk()
root.title("TEXT Image Editor")

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


# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk, ImageDraw
# import cv2
# import numpy as np
# import paddle
# from paddleocr import PaddleOCR

# drawing = False  # Indicates whether the user is drawing a bounding box
# editing = False  # Indicates whether the user is editing an existing bounding box
# start_x, start_y = None, None  # Initial coordinates of the bounding box
# edit_bbox = None  # Stores the bounding box being edited

# def draw_bbox(event):
#     global img_cv, original_img_cv, drawing, start_x, start_y, edit_bbox, editing
#     if editing:
#         return

#     if not drawing:
#         # Start drawing the bounding box
#         start_x, start_y = event.x, event.y
#         drawing = True
#     else:
#         # Finish drawing the bounding box
#         end_x, end_y = event.x, event.y
#         color = (0, 255, 0)  # Green color
#         thickness = 2
#         cv2.rectangle(img_cv, (start_x, start_y), (end_x, end_y), color, thickness)
#         entry.delete(0, tk.END)
#         entry.insert(0, f"{start_x},{start_y},{end_x-start_x},{end_y-start_y}")
#         update_display()
#         drawing = False

# def erase_bbox():
#     global img_cv, original_img_cv, editing, edit_bbox
#     if editing:
#         img_cv = np.copy(original_img_cv)
#         editing = False
#         edit_bbox = None
#     else:
#         img_cv = np.copy(original_img_cv)
#     update_display()

# def edit_coordinates():
#     global editing, edit_bbox
#     coordinates = entry.get().split(',')
#     if len(coordinates) == 4:
#         edit_bbox = [int(coord) for coord in coordinates]
#         editing = True

# def update_display():
#     global img_cv, img_tk
#     img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
#     img_tk = ImageTk.PhotoImage(image=img_pil)
#     canvas.config(width=img_tk.width(), height=img_tk.height())
#     canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
#     canvas.image = img_tk

# def open_image():
#     global img_cv, original_img_cv
#     file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")])
#     if file_path:
#         img_cv = cv2.imread(file_path)
#         original_img_cv = np.copy(img_cv)
#         update_display()

# # Initialize PaddleOCR model
# ocr = PaddleOCR()

# root = tk.Tk()
# root.title("Image Editor")

# open_button = tk.Button(root, text="Open Image", command=open_image)
# open_button.pack()

# entry_label = tk.Label(root, text="Enter Coordinates (X,Y,W,H):")
# entry_label.pack()
# entry = tk.Entry(root)
# entry.pack()

# draw_button = tk.Button(root, text="Draw Bounding Box", command=None)  # Button is not used
# draw_button.pack()

# edit_button = tk.Button(root, text="Edit Coordinates", command=edit_coordinates)
# edit_button.pack()

# erase_button = tk.Button(root, text="Erase Bounding Box", command=erase_bbox)
# erase_button.pack()

# canvas = tk.Canvas(root)
# canvas.pack()

# img_cv = np.zeros((500, 500, 3), dtype=np.uint8)
# original_img_cv = np.copy(img_cv)
# img_tk = None  # Initialize img_tk

# canvas.bind("<Button-1>", draw_bbox)

# root.mainloop()




# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk, ImageDraw
# import cv2
# import numpy as np
# import paddle
# from paddleocr import PaddleOCR

# drawing = False  # Indicates whether the user is drawing a bounding box
# editing = False  # Indicates whether the user is editing an existing bounding box
# start_x, start_y = None, None  # Initial coordinates of the bounding box
# edit_bbox = None  # Stores the bounding box being edited

# def draw_bbox(event):
#     global img_cv, original_img_cv, drawing, start_x, start_y, edit_bbox, editing
#     if not drawing and not editing:
#         # Start drawing a new bounding box
#         start_x, start_y = event.x, event.y
#         drawing = True
#     elif editing:
#         # Update the edited bounding box
#         end_x, end_y = event.x, event.y
#         edit_bbox = [start_x, start_y, end_x, end_y]
#         entry.delete(0, tk.END)
#         entry.insert(0, f"{edit_bbox[0]},{edit_bbox[1]},{edit_bbox[2]-edit_bbox[0]},{edit_bbox[3]-edit_bbox[1]}")
#         update_display()
#         editing = False
#     else:
#         # Finish drawing a new bounding box
#         end_x, end_y = event.x, event.y
#         color = (0, 255, 0)  # Green color
#         thickness = 2
#         cv2.rectangle(img_cv, (start_x, start_y), (end_x, end_y), color, thickness)
#         entry.delete(0, tk.END)
#         entry.insert(0, f"{start_x},{start_y},{end_x-start_x},{end_y-start_y}")
#         update_display()
#         drawing = False

# def erase_bbox():
#     global img_cv, original_img_cv, editing, edit_bbox
#     if editing:
#         edit_bbox = None
#         editing = False
#     else:
#         img_cv = np.copy(original_img_cv)
#     update_display()

# def edit_coordinates():
#     global editing, edit_bbox
#     coordinates = entry.get().split(',')
#     if len(coordinates) == 4:
#         edit_bbox = [int(coord) for coord in coordinates]
#         editing = True

# def update_display():
#     global img_cv, img_tk, edit_bbox
#     img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
#     if edit_bbox:
#         draw = ImageDraw.Draw(img_pil)
#         draw.rectangle(edit_bbox, outline="red")
#     img_tk = ImageTk.PhotoImage(image=img_pil)
#     canvas.config(width=img_tk.width(), height=img_tk.height())
#     canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
#     canvas.image = img_tk

# def open_image():
#     global img_cv, original_img_cv
#     file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")])
#     if file_path:
#         img_cv = cv2.imread(file_path)
#         original_img_cv = np.copy(img_cv)
#         update_display()

# # Initialize PaddleOCR model
# ocr = PaddleOCR()

# root = tk.Tk()
# root.title("Image Editor")

# open_button = tk.Button(root, text="Open Image", command=open_image)
# open_button.pack()

# entry_label = tk.Label(root, text="Enter Coordinates (X,Y,W,H):")
# entry_label.pack()
# entry = tk.Entry(root)
# entry.pack()

# draw_button = tk.Button(root, text="Draw Bounding Box", command=None)  # Button is not used
# draw_button.pack()

# edit_button = tk.Button(root, text="Edit Coordinates", command=edit_coordinates)
# edit_button.pack()

# erase_button = tk.Button(root, text="Erase Bounding Box", command=erase_bbox)
# erase_button.pack()

# canvas = tk.Canvas(root)
# canvas.pack()

# img_cv = np.zeros((500, 500, 3), dtype=np.uint8)
# original_img_cv = np.copy(img_cv)
# img_tk = None  # Initialize img_tk

# canvas.bind("<Button-1>", draw_bbox)

# root.mainloop()
