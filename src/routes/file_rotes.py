from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import shutil

router = APIRouter(
    prefix='/file',
    tags=['file']
)


@router.post('/file')
def get_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}


@router.post('/uploadfile')
def get_upload_file(upload_file: UploadFile = File(...)):
    path = f'uploaded_files/{upload_file.filename}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return {
        'filename': path,
        'type': upload_file.content_type
    }


@router.get('/download/{name}', response_class=FileResponse)
def download_file(name: str):
    path = f'uploaded_files/{name}'
    return path
