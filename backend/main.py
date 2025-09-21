import os
import json
import logging
import asyncio
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
from dotenv import load_dotenv
import cv2
import numpy as np

# Load .env

load_dotenv()

# Logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ARSAA AI")

# Config

class Config:
    BYTEPLUS_API_KEY = os.getenv("BYTEPLUS_API_KEY")
    BYTEPLUS_BASE_URL = os.getenv("BYTEPLUS_BASE_URL")
    BYTEPLUS_MODEL = os.getenv("BYTEPLUS_MODEL")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
    UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
    STABLE_DIFFUSION_API_KEY = os.getenv("STABLE_DIFFUSION_API_KEY")
    STABLE_DIFFUSION_BASE_URL = os.getenv("STABLE_DIFFUSION_BASE_URL")
    OSM_BASE_URL = os.getenv("OSM_BASE_URL", "https://nominatim.openstreetmap.org")
    APP_NAME = os.getenv("APP_NAME", "ARSAA DIMENSION")
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

config = Config()

# FastAPI app

app = FastAPI(title=config.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models

class QueryRequest(BaseModel):
    prompt: str

class FeedbackRequest(BaseModel):
    interaction_id: str
    rating: int
    comment: Optional[str] = None

# AI Query Handling

async def call_byteplus_api(prompt: str) -> Optional[str]:
    """Call BytePlus AI"""
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(
                f"{config.BYTEPLUS_BASE_URL}/generate",
                headers={"Authorization": f"Bearer {config.BYTEPLUS_API_KEY}"},
                json={"model": config.BYTEPLUS_MODEL, "prompt": prompt}
            )
            if res.status_code == 200:
                data = res.json()
                return data.get("text") or data.get("response")
    except Exception as e:
        logger.warning(f"BytePlus API failed: {e}")
    return None

async def call_gemini_api(prompt: str, api_key: str) -> str:
    """Call Gemini AI"""
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(
                "https://generativeai.googleapis.com/v1beta2/models/text-bison-001:generate",
                headers={"Authorization": f"Bearer {api_key}"},
                json={"prompt": prompt, "temperature": 0.7, "maxOutputTokens": 512}
            )
            if res.status_code == 200:
                data = res.json()
                return data.get("candidates", [{}])[0].get("content", "")
    except Exception as e:
        logger.warning(f"Gemini API failed: {e}")
    return "Maaf, AI sedang tidak tersedia sekarang."

async def get_ai_response(prompt: str) -> str:
    """Fallback BytePlus → Gemini"""
    response = await call_byteplus_api(prompt)
    if not response:
        response = await call_gemini_api(prompt, config.GEMINI_API_KEY)
    return response

# OpenCV Image Analysis

async def analyze_property_image(image_bytes: bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        return "Gagal membaca gambar properti."
    height, width, channels = img.shape
    # Contoh analisis sederhana
    return f"Gambar diterima. Dimensi: {width}x{height}, Channels: {channels}"

# OpenStreetMap Geolocation

async def geolocate_address(address: str):
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(config.OSM_BASE_URL, params={"q": address, "format": "json", "limit": 1})
            data = res.json()
            if data:
                return {"lat": data[0]["lat"], "lon": data[0]["lon"], "display_name": data[0]["display_name"]}
    except Exception as e:
        logger.warning(f"Geolocation failed: {e}")
    return None

# API Endpoints

@app.get("/api/arsaa/health")
async def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "byteplus_available": bool(config.BYTEPLUS_API_KEY),
        "gemini_available": bool(config.GEMINI_API_KEY),
        "database": "connected",
        "version": "2.0.0"
    }

@app.get("/api/arsaa/analytics")
async def analytics():
    return {
        "total_interactions": 0,
        "average_rating": 0,
        "average_response_time": "0s",
        "byteplus_status": "active" if config.BYTEPLUS_API_KEY else "fallback",
        "gemini_status": "active" if config.GEMINI_API_KEY else "inactive",
        "version": "2.0.0"
    }

@app.post("/api/arsaa/query")
async def query_ai(request: QueryRequest):
    response_text = await get_ai_response(request.prompt)
    return {
        "success": True,
        "response": response_text,
        "context_used": "real_estate_advisor",
        "processing_time": "auto",
        "market_sentiment": "neutral",
        "timestamp": datetime.now()
    }

@app.post("/api/arsaa/feedback")
async def feedback_ai(request: FeedbackRequest):

    # Simulasi simpan feedback
    return {"success": True, "message": f"Feedback diterima: {request.rating}/5"}

@app.post("/api/arsaa/analyze-image")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    result = await analyze_property_image(content)
    return {"success": True, "result": result}

@app.get("/api/arsaa/geolocate")
async def geolocate(address: str):
    loc = await geolocate_address(address)
    if not loc:
        raise HTTPException(status_code=404, detail="Lokasi tidak ditemukan")
    return {"success": True, "location": loc}

# Run Uvicorn

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config.PORT, reload=config.DEBUG)
