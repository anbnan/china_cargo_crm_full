from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
from uuid import uuid4

router = APIRouter()

UPLOAD_DIR = "app/static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload/")
async def upload_image(order_id: int = Form(...), image: UploadFile = File(...)):
    ext = image.filename.split(".")[-1]
    filename = f"{order_id}_{uuid4().hex}.{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as f:
        f.write(await image.read())
    
    return JSONResponse(content={"detail": "Файл загружен", "file": filename})
