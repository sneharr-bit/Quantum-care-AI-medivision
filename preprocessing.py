from PIL import Image
import numpy as np

def check_retinal_image(image):

    # Check image dimensions
    width, height = image.size

    # Check colour format
    image = image.convert("RGB")

    # Check minimum image size
    if width < 100 or height < 100:
        return False, "Image resolution is too low."

    # Convert image into numerical data
    image_array = np.array(image)

    # Check image data
    if image_array.size == 0:
        return False, "Image is empty."

    return True, "Image quality checks completed."