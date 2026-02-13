from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os

# Use package-relative imports to work when this is a package
from .extractor import process_file_extraction
from .processor import rewrite_text_for_audio
from .convertor import generate_audio_from_text

app = FastAPI(title="AudioBook Generator API")

# Provide an alias named `backend` so existing uvicorn command works
backend = app


@app.get("/")
def read_root():
    return {"message": "AudioBook Backend is running!"}


@app.post("/generate-audio/")
async def generate_audio(file: UploadFile = File(...)):
    try:
        # 1. Read the uploaded file
        file_bytes = await file.read()
        
        # 2. Text Extraction
        raw_text = process_file_extraction(file_bytes, file.filename)
        if not raw_text:
            raise HTTPException(status_code=400, detail="Could not extract text from the file.")
            
        # 3. LLM Enrichment (Rewrite for narration)
        enriched_text = rewrite_text_for_audio(raw_text)
        
        # 4. Text-to-Speech Generation
        audio_file_path = generate_audio_from_text(enriched_text)
        
        if not audio_file_path or not os.path.exists(audio_file_path):
            raise HTTPException(status_code=500, detail="Audio generation failed.")
            
        # 5. Return the audio file to the frontend
        return FileResponse(path=audio_file_path, media_type="audio/mpeg", filename=os.path.basename(audio_file_path))
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
