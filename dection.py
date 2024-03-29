# import cv2
# import numpy as np

# # Load YOLO model for person detection
# yolo_net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# yolo_classes = []
# with open("coco.names", "r") as f:
#     yolo_classes = f.read().strip().split("\n")

# # Load gender classification model (replace with your model)
# # gender_model = cv2.dnn.readNet("gender_model_weights.prototxt", "gender_model.caffemodel")
# gender_model = cv2.dnn.readNet("gender_model_weights.h5", "gender_model.caffemodel")

# # gender_model_weights.h5

# gender_labels = ["Male", "Female"]

# cap = cv2.VideoCapture(0)
# person_count = 0

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Person detection
#     blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     yolo_net.setInput(blob)
#     yolo_outs = yolo_net.forward()

#     # Gender classification and counting
#     for detection in yolo_outs:
#         for obj in detection:
#             scores = obj[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5 and yolo_classes[class_id] == "person":
#                 person_count += 1

#                 # Crop the person's region and classify gender here
#                 x, y, w, h = (obj[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])).astype(int)
#                 person_img = frame[y:y+h, x:x+w]

#                 gender_blob = cv2.dnn.blobFromImage(person_img, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
#                 gender_model.setInput(gender_blob)
#                 gender_out = gender_model.forward()

#                 gender = gender_labels[gender_out[0].argmax()]
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 cv2.putText(frame, f"Gender: {gender}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

#     # Display results
#     cv2.putText(frame, f"Persons: {person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.imshow("Webcam Feed", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model

# # Load YOLO model for person detection
# yolo_net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# yolo_classes = []
# with open("coco.names", "r") as f:
#     yolo_classes = f.read().strip().split("\n")

# # Load the gender classification model in HDF5 format
# gender_model = load_model("gender_model_weights.h5")

# cap = cv2.VideoCapture(0)
# person_count = 0

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Person detection
#     blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     yolo_net.setInput(blob)
#     yolo_outs = yolo_net.forward()

#     # Gender classification and counting
#     for detection in yolo_outs:
#         for obj in detection:
#             scores = obj[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5 and yolo_classes[class_id] == "person":
#                 person_count += 1

#                 # Crop the person's region and classify gender
#                 x, y, w, h = (obj[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]).astype(int))
#                 person_img = frame[y:y+h, x:x+w]

#                 # Preprocess the image for gender classification
#                 person_img = cv2.resize(person_img, (100, 100))
#                 person_img = person_img / 255.0
#                 person_img = np.expand_dims(person_img, axis=0)

#                 # Classify gender
#                 gender = gender_model.predict(person_img)
#                 gender = "Male" if gender[0][0] > 0.5 else "Female"

#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 cv2.putText(frame, f"Gender: {gender}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

#     # Display results
#     cv2.putText(frame, f"Persons: {person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.imshow("Webcam Feed", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained model
model = tf.saved_model.load("ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.config/saved_model")
# path_to_ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/saved_model

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform object detection
    detections = model(frame_rgb)

    # Count persons
    num_persons = 0
    for detection in detections['detection_boxes'][0]:
        if detection[2] > 0.5 and detection[2] < 1.0 and int(detection[0]) == 1:
            num_persons += 1

    # Draw bounding boxes and display count
    cv2.putText(frame, f'Persons: {num_persons}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
