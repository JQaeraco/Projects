# Image Magic
# Load an image and manipulate the pixels

from PIL import Image


def to_grayscale(pixel: tuple, algo="average") -> tuple:
    """Convert a pixel to grayscale.
    can also specify the grayscale algorithim.
    Defaults to average.

    Args:
        pixel: a 3-tuple of ints from
            0 - 255, e.g. (140, 120, 255)
            represents (r, g, b)
        algo: the grayscale conversion algorithm
            specified by the user
            valid values are "average", "luma"
            defaults to "average"

    Returns:
        a 3-tuple pixel (r, g, b) in
        grayscale
    """
    # grab rgb
    red, green, blue = pixel

    # calculate the gray pixel
    if algo.lower() == "luma":
        gray = int(red * 0.3 + green * 0.59 + blue * 0.11)
    else:
        gray = int(sum(pixel) / len(pixel))

    return gray, gray, gray


# Load the image (pumpkin)
# Open an output image that's the same size
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# a_pixel = image.getpixel((0, 0))

# Grab pixel information


# Iterate over EVERY PIXEL
image_width = image.width
image_height = image.height

# Modify the image to convert it from colour to grayscale
# (r, g, b) --> (?, ?, ?)
# take the rgb, add them up and divide by three
# replace rgb with that average

# Top to Bottom
for y in range(image_height):
    # Left to right
    for x in range(image.width):
        # Grab pixel information for THIS pixel
        pixel = image.getpixel((x, y))


        # print(gray_pixel) # test

        # TODO: put that in the new image
        output_image.putpixel((x, y), to_grayscale(pixel, "wg"))

        # print(f"\nPixel Location: {x}, {y}")
        # # Print pixel values
        # print(f"red: {pixel[0]}")
        # print(f"blue: {pixel[1]}")
        # print(f"green: {pixel[2]}")

output_image.save('grayscale2.jpg')