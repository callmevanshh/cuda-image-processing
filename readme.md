Image Processing with OpenCV
This project performs image processing by converting images to grayscale and applying Canny edge detection. It is part of the CUDA at Scale assignment, demonstrating how a batch of TIFF images can be processed using OpenCV on CPU (with optional GPU acceleration if available).

Features
Batch processing of TIFF images

Grayscale conversion

Canny edge detection

Automatic output saving

CUDA device check using OpenCV

How to Run
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Place all .tif or .tiff images inside the input_images/ folder.

Run the processing script:

bash
Copy
Edit
python process_images.py
The processed grayscale and edge-detected images will be saved to the output_images/ folder.

Folder Structure
process_images.py: Main Python script that performs the processing

requirements.txt: Python package requirements

input_images/: Folder containing input TIFF images

output_images/: Folder where processed images are saved

README.md: Project documentation (this file)

CUDA Acceleration
The script checks if a CUDA-enabled GPU is available via OpenCV. If a GPU is found, it will print a message; otherwise, it defaults to CPU processing.

Example output:

csharp
Copy
Edit
CUDA device count: 0
Running on CPU using OpenCV.
Dataset Used
Images from the USC-SIPI Miscellaneous dataset (39 TIFF images)

