# Computer Vision Lab Task - Week 1

## Introduction

This assignment looks at three basic ideas behind digital images: pixels, resolution, and image compression. The programs use Python and Pillow to inspect or save the sample image `image.jpg`.

Install Pillow from the VS Code terminal:

```bash
pip install pillow
```

Keep `image.jpg` in the same folder as the Python programs. Each program can be run separately, for example with `python pixel.py`.

## 1. Pixel

```python
from PIL import Image

# Open the sample image and convert it to RGB so every pixel has red, green,
# and blue values.
with Image.open("image.jpg") as source:
    image = source.convert("RGB")

# Choose one pixel near the upper-left area of the sample image.
x = 60
y = 60

# Read and display the pixel's RGB color value.
rgb_value = image.getpixel((x, y))
print(f"Pixel at ({x}, {y}) has RGB value: {rgb_value}")
```

**What it does:** Reads the RGB color of one pixel at coordinate `(60, 60)`.

**How it works:** Pillow opens the image, converts it to the RGB color format, and `getpixel()` returns the red, green, and blue values at the selected coordinate.

**Expected output:** For the included sample image, the output is `Pixel at (60, 60) has RGB value: (254, 99, 71)`. JPEG encoding can cause small color changes.

**Why it matters:** A pixel is the smallest addressable part of a digital image. Computer Vision programs use pixel values to detect colors, edges, shapes, and other visual information.

## 2. Resolution

```python
from PIL import Image

# Open the sample image and read its dimensions.
with Image.open("image.jpg") as image:
    width, height = image.size

# Display the width, height, and resolution in pixels.
print(f"Image width: {width} pixels")
print(f"Image height: {height} pixels")
print(f"Image resolution: {width} x {height} pixels")
```

**What it does:** Displays the image width, height, and total resolution in pixels.

**How it works:** The `size` property gives the image dimensions as `(width, height)`, which the program prints in a readable form.

**Expected output:** For the included sample image: `Image width: 320 pixels`, `Image height: 240 pixels`, and `Image resolution: 320 x 240 pixels`.

**Why it matters:** Resolution tells us how many pixels are available to represent an image. It affects the amount of detail a computer can analyze and the memory needed to store or process the image.

## 3. Image Compression

```python
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
```

**What it does:** Saves a lower-quality JPEG copy as `compressed.jpg` and reports both file sizes.

**How it works:** Pillow saves the image with JPEG quality set to `30`. The original file remains unchanged, and `os.path.getsize()` measures each file in bytes.

**Expected output:** The original and compressed sizes in bytes, followed by `Saved compressed image as: compressed.jpg`. The compressed file is usually smaller, though the exact sizes depend on the image.

**Why it matters:** Compression reduces storage use and transfer time. Lower-quality JPEG compression can discard image detail, so Computer Vision results may change if important visual information is lost.

## Conclusion

Pixels store the color information in a digital image, and resolution describes how many pixels form its width and height. Compression changes how much space the image uses and may also reduce detail. These three properties affect the quality, storage, and processing of images in Computer Vision.
