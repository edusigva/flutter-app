#!/usr/bin/env python3
"""
EDUSİGVA - A - Immediate Completion
Minimal API for GitHub Actions deployment test
"""

from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="EDUSİGVA API", version="1.0.0")

@app.get("/")
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "EDUSİGVA API", 
        "timestamp": datetime.now().isoformat(),
        "message": "🚀 A - Immediate Completion Ready!"
    }

@app.get("/api/v1/reference-data/tr")
def get_reference_data():
    """Flutter app için temel referans data"""
    return {
        "cities": [
            {"id": 1, "name": "İstanbul", "code": "34"},
            {"id": 2, "name": "Ankara", "code": "06"},
            {"id": 3, "name": "İzmir", "code": "35"},
            {"id": 4, "name": "Mardin", "code": "47"},
            {"id": 5, "name": "Antalya", "code": "07"}
        ],
        "districts": [
            {"id": 1, "city_id": 1, "name": "Kadıköy"},
            {"id": 2, "city_id": 1, "name": "Beşiktaş"},
            {"id": 3, "city_id": 4, "name": "Nusaybin"},
            {"id": 4, "city_id": 2, "name": "Çankaya"},
            {"id": 5, "city_id": 3, "name": "Konak"}
        ],
        "subjects": [
            {"id": 1, "name": "Matematik", "grade_min": 1, "grade_max": 12},
            {"id": 2, "name": "Türkçe", "grade_min": 1, "grade_max": 12},
            {"id": 3, "name": "Sosyal Bilgiler", "grade_min": 4, "grade_max": 7}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
