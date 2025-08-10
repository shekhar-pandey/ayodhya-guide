from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import json
import os
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel

# Data models
class Place(BaseModel):
    id: int
    name: str
    slug: str
    category: str
    description: str
    image: str
    rating: float
    location: str
    coordinates: List[float]
    timings: str
    entryFee: str
    bestTime: str
    history: Optional[str] = None
    tips: Optional[List[str]] = None
    gallery: Optional[List[str]] = None

class SearchQuery(BaseModel):
    query: str
    category: Optional[str] = None

class ContactMessage(BaseModel):
    name: str
    email: str
    subject: Optional[str] = None
    message: str

# Initialize FastAPI app
app = FastAPI(
    title="Ayodhya Guide API",
    description="API for the Ayodhya Guide application - exploring the holy city of Ayodhya",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load places data
def load_places_data():
    """Load places data from JSON file"""
    try:
        data_file = Path(__file__).parent / "data" / "places.json"
        if not data_file.exists():
            # Fallback to parent directory
            data_file = Path(__file__).parent.parent.parent / "data" / "places.json"
        
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading places data: {e}")
        return []

# Routes
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Ayodhya Guide API",
        "version": "1.0.0",
        "endpoints": {
            "places": "/api/places",
            "search": "/api/search",
            "categories": "/api/categories",
            "contact": "/api/contact"
        }
    }

@app.get("/api/places", response_model=List[Place])
async def get_places():
    """Get all places"""
    places = load_places_data()
    return places

@app.get("/api/places/{slug}", response_model=Place)
async def get_place_by_slug(slug: str):
    """Get a specific place by slug"""
    places = load_places_data()
    place = next((p for p in places if p["slug"] == slug), None)
    
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    
    return place

@app.get("/api/categories")
async def get_categories():
    """Get all available categories"""
    places = load_places_data()
    categories = list(set(place["category"] for place in places))
    return {"categories": categories}

@app.post("/api/search")
async def search_places(search_query: SearchQuery):
    """Search places by query and optional category filter"""
    places = load_places_data()
    
    query = search_query.query.lower()
    category = search_query.category.lower() if search_query.category else None
    
    filtered_places = []
    
    for place in places:
        # Check if place matches search query
        matches_query = (
            query in place["name"].lower() or
            query in place["description"].lower() or
            query in place["location"].lower() or
            query in place["category"].lower()
        )
        
        # Check if place matches category filter
        matches_category = not category or place["category"].lower() == category
        
        if matches_query and matches_category:
            filtered_places.append(place)
    
    return {
        "query": search_query.query,
        "category": search_query.category,
        "results": filtered_places,
        "total": len(filtered_places)
    }

@app.post("/api/contact")
async def submit_contact(contact: ContactMessage):
    """Submit a contact form message"""
    # In a real application, you would save this to a database
    # For now, we'll just log it and return a success message
    
    print(f"Contact form submitted:")
    print(f"Name: {contact.name}")
    print(f"Email: {contact.email}")
    if contact.subject:
        print(f"Subject: {contact.subject}")
    print(f"Message: {contact.message}")
    
    return {
        "message": "Thank you for your message! We'll get back to you soon.",
        "status": "success",
        "data": {
            "name": contact.name,
            "email": contact.email,
            "subject": contact.subject,
            "message": contact.message
        }
    }

@app.get("/api/places/category/{category}")
async def get_places_by_category(category: str):
    """Get all places in a specific category"""
    places = load_places_data()
    filtered_places = [p for p in places if p["category"].lower() == category.lower()]
    
    if not filtered_places:
        raise HTTPException(status_code=404, detail=f"No places found in category '{category}'")
    
    return {
        "category": category,
        "places": filtered_places,
        "total": len(filtered_places)
    }

@app.get("/api/places/featured")
async def get_featured_places():
    """Get featured places (top rated)"""
    places = load_places_data()
    
    # Sort by rating and return top 5
    featured_places = sorted(places, key=lambda x: x["rating"], reverse=True)[:5]
    
    return {
        "featured_places": featured_places,
        "total": len(featured_places)
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Ayodhya Guide API"}

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Resource not found"}
    )

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
