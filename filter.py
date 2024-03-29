import pandas as pd

# Load the Excel file into a DataFrame
file_path = 'C:/New folder (2)\Data NRICH Teachwork.xlsx'
sheet_name = 'FamilyMaster'  # Replace with the name of your sheet
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Define the filter criteria
first_name_filter = 'John'
last_name_filter = 'Doe'
email_filter = 'johndoe@example.com'

# Filter the DataFrame based on the criteria
filtered_df = df[
    (df['First Name'] == first_name_filter) &
    (df['Last Name'] == last_name_filter) &
    (df['Email'] == email_filter)
]

# Save the filtered DataFrame to a new Excel file
filtered_file_path = 'filtered_excel_file.xlsx'
filtered_df.to_excel(filtered_file_path, index=False)

print(f"Filtered data saved to {filtered_file_path}")
