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
