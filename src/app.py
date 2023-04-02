import os.path
import shutil
from shutil import make_archive
from uuid import uuid4

from PIL import Image
from fastapi import FastAPI, File, UploadFile

from .dto import ResizeParams
from .settings import settings, root_dir
from .utils import *

app = FastAPI(
    debug=settings.debug,
)
media_path = os.path.join(os.path.dirname(root_dir), 'media')


@app.post("/upload")
async def root(fileb: UploadFile = File()):
    id = str(uuid4())
    file_type = fileb.filename.split('.')[-1]
    out_file_path = os.path.join(media_path, f'{id}.{file_type}')
    with open(out_file_path, 'wb') as out_file:
        content = await fileb.read()
        out_file.write(content)
    return {"Result": "OK", 'id': id}


@app.post('/resize/{filename}')
def resize(filename: str, resize_params: ResizeParams):
    file_path = os.path.join(media_path, filename)
    filename, filetype = filename.split('.')  # TODO: fix for filename with .
    dirname = os.path.abspath(os.path.join(media_path, filename))

    try:
        os.mkdir(dirname)
    except FileExistsError:
        pass

    image = Image.open(file_path)
    for size in resize_params.sizes:
        if size.width == 0:
            size.width = get_with(image, size.height)
        if size.height == 0:
            size.height = get_height(image, size.width)
        resize_image_name = f'{filename}_{size.width}x{size.height}.{filetype}'
        resize_image = image.resize((size.width, size.height))
        resize_image.save(os.path.join(media_path, filename, resize_image_name))
    make_archive(dirname, 'zip', dirname)
    shutil.rmtree(dirname)
    return {"Result": "OK"}
