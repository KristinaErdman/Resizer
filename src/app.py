import os.path
from uuid import uuid4

from PIL import Image
from fastapi import FastAPI, File, UploadFile

from .settings import settings, root_dir

app = FastAPI(
    debug=settings.debug,
)
media_path = os.path.join(os.path.dirname(root_dir), 'media')


@app.post("/upload")
async def root(fileb: UploadFile = File()):
    file_type = fileb.filename.split('.')[-1]
    out_file_path = os.path.join(media_path, f'{str(uuid4())}.{file_type}')
    with open(out_file_path, 'wb') as out_file:
        content = await fileb.read()
        out_file.write(content)
    return {"Result": "OK"}


@app.get('/resize/{filename}')
def resize(filename: str):
    file_path = os.path.join(media_path, filename)
    image = Image.open(file_path)
    image = image.resize((500, 100))
    # (left, upper, right, lower) = (20, 20, 400, 400)
    # image.thumbnail((400, 400))
    # image = image.crop((left, upper, right, lower))
    # image = image.filter(ImageFilter.DETAIL)
    image.save(os.path.join(media_path, 'myimage_500.jpg'))
    return {"Result": "OK"}
