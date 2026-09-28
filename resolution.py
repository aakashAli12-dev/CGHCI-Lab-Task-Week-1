from PIL import Image

# Open the sample image and read its dimensions.
with Image.open("image.jpg") as image:
    width, height = image.size

# Display the width, height, and resolution in pixels.
print(f"Image width: {width} pixels")
print(f"Image height: {height} pixels")
print(f"Image resolution: {width} x {height} pixels")
