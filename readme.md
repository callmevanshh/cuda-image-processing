📸 Image Processing with OpenCV
This project performs image processing by converting TIFF images to grayscale and applying Canny edge detection. It is part of the CUDA at Scale assignment, demonstrating how a batch of images can be processed using OpenCV on the CPU, with optional GPU acceleration if available.

✅ Features
📁 Batch processing of .tif / .tiff images

🎨 Grayscale conversion

⚡ Canny edge detection

💾 Automatic output saving

🚀 CUDA device detection (via OpenCV)

🚀 How to Run
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Place images:
Copy your input TIFF images into the input_images/ folder.

Run the script:

bash
Copy
Edit
python process_images.py
Processed grayscale and edge-detected images will be saved to the output_images/ folder.

📁 Folder Structure
graphql
Copy
Edit
.
├── process_images.py       # Main Python script
├── requirements.txt        # Python dependencies
├── input_images/           # Input TIFF images (you add them)
├── output_images/          # Output results (auto-generated)
└── README.md               # This documentation
Note: input_images/ and output_images/ contain .keep files to preserve folder structure.

⚙️ Command-Line Support
You can optionally run with arguments:

bash
Copy
Edit
python process_images.py --input_dir input_images --output_dir output_images
💻 CUDA Acceleration
The script checks for a CUDA-enabled GPU via OpenCV.

Sample output:

csharp
Copy
Edit
CUDA device count: 0
Running on CPU using OpenCV.
If GPU is available, OpenCV’s CUDA backend may be used (if built with CUDA support).

🖼 Dataset Used
You can test with the USC-SIPI Miscellaneous Dataset which provides 39 .tiff images.

📌 Notes
This repo intentionally does not include actual TIFF files.

You must provide your own input images in input_images/.

Works on both CPU and GPU-enabled systems (if OpenCV is built with CUDA).

