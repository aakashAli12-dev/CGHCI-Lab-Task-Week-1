import os
from PIL import Image

input_file = "image.jpg"
output_file = "compressed.jpg"

# Record the original file size before creating the compressed copy.
original_size = os.path.getsize(input_file)

# Save a new JPEG at lower quality. The original image is not changed.
with Image.open(input_file) as image:
    image.save(output_file, "JPEG", quality=30)

# Read the new file size and display both sizes in bytes.
compressed_size = os.path.getsize(output_file)
print(f"Original file size: {original_size} bytes")
print(f"Compressed file size: {compressed_size} bytes")
print(f"Saved compressed image as: {output_file}")
