import pandas as pd
import os
import requests

# Assuming you have a CSV file containing the data
data = pd.read_csv('C:/Users/Dell/Desktop/_SELECT_nnod_deviceId_nnod_fileName_nnod_capturedAtIST_nnod_chan_202310111636.csv')

# Create a directory to save the downloaded files
os.makedirs('C:/test', exist_ok=True)

# Iterate through each row
for index, row in data.iterrows():
    if index >= 332:
        break  # Stop after processing 600 rows
    
    file_path = row['filePath']
    file_name = row['fileName']
    
    # Download the file using requests
    response = requests.get(file_path)
    
    if response.status_code == 200:
        # Specify the directory where you want to save the files
        save_dir = 'C:/test'
        
        # Define the complete path for the downloaded file
        # save_path = os.path.join(save_dir, file_name)
        save_path = os.path.join(save_dir, os.path.basename(file_name))
        
        # Save the downloaded file with the specified name
        with open(save_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Downloaded and saved: {file_name}")
    else:
        print(f"Failed to download: {file_name}")
