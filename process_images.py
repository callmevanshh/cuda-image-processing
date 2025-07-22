import cv2
print("CUDA device count:", cv2.cuda.getCudaEnabledDeviceCount())

import os
from tqdm import tqdm

input_dir = "input_images"
output_dir = "output_images"
os.makedirs(output_dir, exist_ok=True)

for filename in tqdm(os.listdir(input_dir), desc="Processing images"):
    if not filename.lower().endswith((".tif", ".tiff")):
        continue

    input_path = os.path.join(input_dir, filename)
    img = cv2.imread(input_path)

    if img is None:
        print(f"❌ Couldn't read {filename}, skipping.")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    output_name = filename.replace(".tiff", ".png").replace(".tif", ".png")
    output_path = os.path.join(output_dir, output_name)
    cv2.imwrite(output_path, edges)

print("✅ Done processing all images!")
