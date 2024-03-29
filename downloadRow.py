import pandas as pd
import os
import requests

# Assuming you have a CSV file containing the data
data = pd.read_csv('C:/Users/Dell/Desktop/_Zip__202310082009.csv')

# Select the first 200 rows
data = data.head(200)

# Create a function to download and rename the files
def download_and_rename(row):
    file_path = row['filePath']
    file_name = row['fileName']
    
    # Download the file using requests
    response = requests.get(file_path)
    
    if response.status_code == 2:
        # Specify the directory where you want to save the files
        save_dir = 'C:/test'
        os.makedirs(save_dir, exist_ok=True)
        
        # Define the complete path for the downloaded file
        save_path = os.path.join(save_dir, file_name)
        
        # Save the downloaded file with the specified name
        with open(save_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Downloaded and saved: {file_name}")
    else:
        print(f"Failed to download: {file_name}")

# Apply the function to each row in the DataFrame
data.apply(download_and_rename, axis=1)
