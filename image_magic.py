# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')

# a_pixel = image.getpixel((0, 0))

# Grab pixel information
print(a_pixel)

# Iterate over EVERY PIXEL
image_width = image.width
image_height = image.height

# Top to Bottom
for y in range(image_height):
    # Left to right
    for x in range(image.width):
        # Grab pixel information for THIS pixel
        pixel = image.getpixel((x, y))

        # print(f"\nPixel Location: {x}, {y}")
        # # Print pixel values
        # print(f"red: {pixel[0]}")
        # print(f"blue: {pixel[1]}")
        # print(f"green: {pixel[2]}")