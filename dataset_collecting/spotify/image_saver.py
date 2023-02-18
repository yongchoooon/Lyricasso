import base64
from PIL import Image
from io import BytesIO


def image_saver(cover_base64):
    # Assume that `cover_base64` is a base64-encoded string representing an image
    # Decode the base64 string into a bytes object
    image_bytes = base64.b64decode(cover_base64)

    # Use the `PIL` module to open the image and save it to a file
    image = Image.open(BytesIO(image_bytes))
    image.save('cover.jpg')