# import torch
# import torch.nn as nn
# import torch.optim as optim
# from torchvision import datasets, transforms
# from torch.utils.data import DataLoader

# # Define a simple CNN model for gender classification.
# class GenderClassifier(nn.Module):
#     def __init__(self):
#         super(GenderClassifier, self).__init__()
#         self.conv1 = nn.Conv2d(3, 32, 3)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.fc1 = nn.Linear(32 * 15 * 15, 128)
#         self.fc2 = nn.Linear(128, 2)

#     def forward(self, x):
#         x = self.pool(torch.relu(self.conv1(x)))
#         x = x.view(-1, 32 * 15 * 15)
#         x = torch.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x

# # Load and preprocess your dataset using torchvision transforms.

# # Split the dataset into training, validation, and test sets.

# # # Create data loaders for each split.
# # train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
# # validation_loader = DataLoader(validation_dataset, batch_size=32)
# # test_loader = DataLoader(test_dataset, batch_size=32)

# # Replace these lines with your actual dataset loading and preprocessing
# train_dataset = ...
# validation_dataset = ...
# test_dataset = ...

# # Create data loaders for each split.
# train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
# validation_loader = DataLoader(validation_dataset, batch_size=32)
# test_loader = DataLoader(test_dataset, batch_size=32)

# # Initialize the model, loss function, and optimizer.
# model = GenderClassifier()
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# # Train the model.
# num_epochs = 10
# for epoch in range(num_epochs):
#     model.train()
#     for inputs, labels in train_loader:
#         optimizer.zero_grad()
#         outputs = model(inputs)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()

# # Use the trained model for classification and counting.
# model.eval()
# male_count = 0
# female_count = 0

# for inputs, labels in test_loader:
#     outputs = model(inputs)
#     _, predicted = torch.max(outputs, 1)
#     male_count += (predicted == 0).sum().item()
#     female_count += (predicted == 1).sum().item()

# print(f'Male count: {male_count}')
# print(f'Female count: {female_count}')









import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained gender classification model (you'll need to obtain or train this).
gender_model = tf.keras.models.load_model("gender_model.h5")

# Initialize counters
male_count = 0
female_count = 0
total_count = 0

# Open a connection to the webcam (0 indicates the default webcam).
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Preprocess the image for the gender model (resize, normalize, etc.).
    resized_frame = cv2.resize(frame, (64, 64))
    input_frame = np.expand_dims(resized_frame, axis=0) / 255.0

    # Perform gender classification using the model.
    gender_predictions = gender_model.predict(input_frame)
    gender = "Male" if gender_predictions[0] > 0.5 else "Female"

    # Update counters
    if gender == "Male":
        male_count += 1
    else:
        female_count += 1

    total_count += 1

    # Display the gender on the frame.
    cv2.putText(frame, gender, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Display the frame.
    cv2.imshow("Gender Classification", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window.
cap.release()
cv2.destroyAllWindows()

print("Total people detected:", total_count)
print("Male count:", male_count)
print("Female count:", female_count)
