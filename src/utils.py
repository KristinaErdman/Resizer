from PIL import Image, ExifTags


def get_with(image: Image, new_height: int):
    return int((new_height / image.height) * image.width)


def get_height(image: Image, new_with: int):
    return int((new_with / image.width) * image.height)


def save_source_orientation(image: Image):
    orientation = image.getexif().get(ExifTags.Base.Orientation, None)

    transform_methods = {
        2: (Image.Transpose.FLIP_LEFT_RIGHT,),
        3: (Image.Transpose.ROTATE_180,),
        4: (Image.Transpose.FLIP_TOP_BOTTOM,),
        5: (Image.Transpose.ROTATE_270, Image.Transpose.FLIP_LEFT_RIGHT,),
        6: (Image.Transpose.ROTATE_270,),
        7: (Image.Transpose.ROTATE_90, Image.Transpose.FLIP_LEFT_RIGHT,),
        8: (Image.Transpose.ROTATE_90,)
    }
    for method in transform_methods.get(orientation, tuple()):
        image = image.transpose(method)

    return image
