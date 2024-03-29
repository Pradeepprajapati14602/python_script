import cv2
import re  # Import the regex module
from paddleocr import PaddleOCR

# Load the PaddleOCR model
ocr_model = PaddleOCR(use_gpu=True, lang="en", show_log=False, use_angle_cls=False)

image_paths = [...]  # Replace with your list of image file paths
output_file = "filtered_ocr_results.txt"  # Output file for filtered results

# Define your regex pattern for filtering
regex_pattern = r"\d{4}-\d{2}-\d{2}"  # Example: YYYY-MM-DD

def save_filtered_ocr_results_to_text(filtered_results, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for line in filtered_results:
            file.write(line + "\n")

keys = []
values = []
filtered_results = []  # List to store filtered text results

for k, path in enumerate(image_paths[0:100]):
    image = cv2.imread(path)

    results = ocr_model.ocr(image, cls=False)

    values.append(results)
    keys.append(k)

    res_list = results[0][1]  # Extract text from the OCR results

    # Apply the regex filter to the extracted text
    filtered_text = "\n".join(re.findall(regex_pattern, " ".join(res_list)))

    print("Filtered OCR Results for image", k)
    print(filtered_text)

    filtered_results.append(filtered_text)  # Add filtered text to the list

    k += 1

# Save the filtered OCR results to a text file
save_filtered_ocr_results_to_text(filtered_results, output_file)

print("Filtered OCR results saved to", output_file)
