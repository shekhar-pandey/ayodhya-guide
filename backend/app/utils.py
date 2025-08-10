import json
import os
from typing import Dict, List, Optional
from pathlib import Path

def load_places_data() -> List[Dict]:
    """Load places data from JSON file"""
    try:
        # Try to load from backend data first
        backend_data_path = Path(__file__).parent / "data" / "places.json"
        if backend_data_path.exists():
            with open(backend_data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Fallback to main data directory
        main_data_path = Path(__file__).parent.parent.parent / "data" / "places.json"
        if main_data_path.exists():
            with open(main_data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return []
    except Exception as e:
        print(f"Error loading places data: {e}")
        return []

def get_place_by_slug(slug: str) -> Optional[Dict]:
    """Get a specific place by its slug"""
    places = load_places_data()
    for place in places:
        if place.get('slug') == slug:
            return place
    return None

def search_places(query: str) -> List[Dict]:
    """Search places by name, description, or category"""
    if not query:
        return []
    
    query = query.lower()
    places = load_places_data()
    results = []
    
    for place in places:
        # Search in name
        if query in place.get('name', '').lower():
            results.append(place)
            continue
        
        # Search in description
        if query in place.get('description', '').lower():
            results.append(place)
            continue
        
        # Search in category
        if query in place.get('category', '').lower():
            results.append(place)
            continue
        
        # Search in tags
        tags = place.get('tags', [])
        if any(query in tag.lower() for tag in tags):
            results.append(place)
            continue
    
    return results

def get_places_by_category(category: str) -> List[Dict]:
    """Get all places in a specific category"""
    places = load_places_data()
    return [place for place in places if place.get('category', '').lower() == category.lower()]

def get_categories() -> List[str]:
    """Get all available categories"""
    places = load_places_data()
    categories = set()
    for place in places:
        if 'category' in place:
            categories.add(place['category'])
    return sorted(list(categories))

def validate_place_data(place_data: Dict) -> bool:
    """Validate place data structure"""
    required_fields = ['name', 'slug', 'description', 'category']
    for field in required_fields:
        if field not in place_data or not place_data[field]:
            return False
    return True

def format_place_response(place: Dict) -> Dict:
    """Format place data for API response"""
    return {
        'id': place.get('id'),
        'name': place.get('name'),
        'slug': place.get('slug'),
        'description': place.get('description'),
        'category': place.get('category'),
        'image': place.get('image'),
        'location': place.get('location'),
        'timings': place.get('timings'),
        'entry_fee': place.get('entry_fee'),
        'tags': place.get('tags', []),
        'coordinates': place.get('coordinates'),
        'best_time': place.get('best_time'),
        'how_to_reach': place.get('how_to_reach')
    }
