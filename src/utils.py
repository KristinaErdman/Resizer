from PIL import Image


def get_with(image: Image, new_height: int):
    return int((new_height / image.height) * image.width)


def get_height(image: Image, new_with: int):
    return int((new_with / image.width) * image.height)
