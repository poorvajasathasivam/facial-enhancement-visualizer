from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import io
from PIL import Image
import os
import uuid
import logging
from datetime import datetime
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Facial Enhancement API",
    description="API for enhancing facial images using Stable Diffusion.",
    version="0.1.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Welcome to the Facial Enhancement API!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Validate file is an image
        content_type = file.content_type
        if not content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Read image data
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        
        # Generate a unique filename
        file_id = str(uuid.uuid4())
        file_extension = os.path.splitext(file.filename)[1]
        filename = f"{file_id}{file_extension}"
        
        # Save the image
        file_path = os.path.join("uploads", filename)
        image.save(file_path)
        
        logger.info(f"Image uploaded successfully: {filename}")
        
        return {
            "file_id": file_id,
            "filename": filename,
            "message": "Image uploaded successfully"
        }
    
    except Exception as e:
        logger.error(f"Error uploading image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

@app.post("/enhance/{file_id}")
async def enhance_image(
    file_id: str,
    enhancement_type: str,
    intensity: float = 0.5
):
    try:
        # In a real implementation, we would call the StyleGAN model here
        # For now, we'll just return a mock response
        
        # Validate enhancement type
        valid_enhancements = ["smooth_skin", "reduce_wrinkles", "enhance_jawline", 
                              "brighten_eyes", "fuller_lips", "defined_cheekbones"]
        
        if enhancement_type not in valid_enhancements:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid enhancement type. Valid options: {valid_enhancements}"
            )
        
        # Validate intensity (0-1 range)
        if not (0 <= intensity <= 1):
            raise HTTPException(
                status_code=400,
                detail="Intensity must be between 0 and 1"
            )
        
        # Here we would process the image with StyleGAN
        # For now, we'll return a dummy response
        
        logger.info(f"Enhancement applied: {enhancement_type} with intensity {intensity}")
        
        return {
            "file_id": file_id,
            "enhancement_type": enhancement_type,
            "intensity": intensity,
            "result_id": str(uuid.uuid4()),
            "message": "Enhancement applied successfully"
        }
    
    except Exception as e:
        logger.error(f"Error enhancing image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error enhancing image: {str(e)}")

@app.get("/results/{result_id}")
async def get_result(result_id: str):
    return {
        "result_id": result_id,
        "status": "completed",
        "original_image_url": f"/images/original/{result_id}.jpg",
        "enhanced_image_url": f"/images/enhanced/{result_id}.jpg",
        "created_at": datetime.now().isoformat()
    }
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)