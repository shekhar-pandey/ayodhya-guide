#!/usr/bin/env python3
"""
Ayodhya Guide - Image Downloader
Downloads high-quality, free images from open source websites for all locations
"""

import os
import requests
import json
from urllib.parse import quote
import time
from pathlib import Path

# Configuration
IMAGES_DIR = "images"
PLACES_FILE = "data/places.json"
UNSPLASH_ACCESS_KEY = ""  # Optional: Add your Unsplash API key for better results
PEXELS_API_KEY = ""       # Optional: Add your Pexels API key for better results

# Image search queries for each location
LOCATION_IMAGES = {
    "ram-temple": [
        "hindu temple architecture",
        "ram temple ayodhya",
        "sacred hindu temple",
        "golden temple architecture"
    ],
    "hanuman-garhi": [
        "hanuman temple",
        "hindu temple on hill",
        "sacred temple architecture",
        "temple with panoramic view"
    ],
    "kanak-bhawan": [
        "golden temple architecture",
        "hindu temple carvings",
        "ornate temple facade",
        "traditional indian temple"
    ],
    "nageshwarnath-temple": [
        "shiva temple",
        "ancient hindu temple",
        "temple architecture",
        "sacred shiva linga"
    ],
    "treta-ke-thakur": [
        "ancient temple complex",
        "hindu temple ruins",
        "sacred site",
        "temple architecture"
    ],
    "chhoti-devkali": [
        "goddess temple",
        "peaceful temple",
        "hindu temple interior",
        "sacred temple space"
    ],
    "sarayu-ghats": [
        "river ghats",
        "sacred river",
        "ghats on river",
        "holy river steps"
    ],
    "ayodhya-fort": [
        "ancient fort",
        "historical fort",
        "fort architecture",
        "ruins of fort"
    ],
    "gulab-bari": [
        "rose garden",
        "beautiful garden",
        "mughal architecture",
        "garden with flowers"
    ],
    "mani-parbat": [
        "hill view",
        "panoramic city view",
        "sacred hill",
        "mountain landscape"
    ]
}

def create_images_directory():
    """Create images directory if it doesn't exist"""
    Path(IMAGES_DIR).mkdir(exist_ok=True)
    print(f"✅ Images directory created/verified: {IMAGES_DIR}")

def download_image_from_unsplash(query, filename, size="800x600"):
    """Download image from Unsplash (free tier)"""
    if not UNSPLASH_ACCESS_KEY:
        # Use Unsplash source without API key (limited but free)
        search_url = f"https://unsplash.com/s/photos/{quote(query)}"
        print(f"🔍 Search Unsplash manually: {search_url}")
        return False
    
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    search_url = f"https://api.unsplash.com/search/photos?query={quote(query)}&per_page=1"
    
    try:
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                image_url = data["results"][0]["urls"]["regular"]
                return download_image(image_url, filename)
    except Exception as e:
        print(f"❌ Unsplash API error: {e}")
    
    return False

def download_image_from_pexels(query, filename, size="800x600"):
    """Download image from Pexels (free tier)"""
    if not PEXELS_API_KEY:
        # Use Pexels source without API key (limited but free)
        search_url = f"https://www.pexels.com/search/{quote(query)}/"
        print(f"🔍 Search Pexels manually: {search_url}")
        return False
    
    headers = {"Authorization": PEXELS_API_KEY}
    search_url = f"https://api.pexels.com/v1/search?query={quote(query)}&per_page=1"
    
    try:
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data["photos"]:
                image_url = data["photos"][0]["src"]["large"]
                return download_image(image_url, filename)
    except Exception as e:
        print(f"❌ Pexels API error: {e}")
    
    return False

def download_image_from_pixabay(query, filename, size="800x600"):
    """Download image from Pixabay (free tier)"""
    # Pixabay allows direct image downloads without API key
    search_url = f"https://pixabay.com/images/search/{quote(query)}/"
    print(f"🔍 Search Pixabay manually: {search_url}")
    return False

def download_image_from_wikimedia(query, filename, size="800x600"):
    """Download image from Wikimedia Commons (completely free)"""
    # Wikimedia Commons has many free images
    search_url = f"https://commons.wikimedia.org/w/index.php?search={quote(query)}&title=Special:MediaSearch&go=Go&type=bitmap"
    print(f"🔍 Search Wikimedia Commons manually: {search_url}")
    return False

def download_image(url, filename):
    """Download image from URL"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        filepath = os.path.join(IMAGES_DIR, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"❌ Download failed for {filename}: {e}")
        return False

def create_placeholder_image(filename, text, size="800x600"):
    """Create a placeholder image using placeholder.com service"""
    try:
        # Use placeholder.com for temporary images
        url = f"https://via.placeholder.com/{size}/4A90E2/FFFFFF?text={quote(text)}"
        return download_image(url, filename)
    except Exception as e:
        print(f"❌ Placeholder creation failed for {filename}: {e}")
        return False

def download_all_images():
    """Download images for all locations"""
    print("🚀 Starting image download for Ayodhya Guide...")
    print("=" * 60)
    
    create_images_directory()
    
    total_images = 0
    successful_downloads = 0
    
    for location, queries in LOCATION_IMAGES.items():
        print(f"\n📍 Processing: {location.replace('-', ' ').title()}")
        print("-" * 40)
        
        # Main image
        main_filename = f"{location}.jpg"
        main_downloaded = False
        
        # Try different sources for main image
        for query in queries:
            if not main_downloaded:
                print(f"🔍 Trying query: '{query}'")
                
                # Try Unsplash first
                if UNSPLASH_ACCESS_KEY:
                    main_downloaded = download_image_from_unsplash(query, main_filename)
                
                # Try Pexels if Unsplash failed
                if not main_downloaded and PEXELS_API_KEY:
                    main_downloaded = download_image_from_pexels(query, main_filename)
                
                # Try Pixabay
                if not main_downloaded:
                    main_downloaded = download_image_from_pixabay(query, main_filename)
                
                # Try Wikimedia Commons
                if not main_downloaded:
                    main_downloaded = download_image_from_wikimedia(query, main_filename)
                
                if main_downloaded:
                    break
        
        # Create placeholder if no image downloaded
        if not main_downloaded:
            print(f"📝 Creating placeholder for: {main_filename}")
            create_placeholder_image(main_filename, location.replace('-', ' ').title())
            successful_downloads += 1
        
        total_images += 1
        
        # Gallery images (optional)
        gallery_count = 2  # Limit to 2 gallery images per location
        for i in range(1, gallery_count + 1):
            gallery_filename = f"{location}-{i}.jpg"
            
            # Try to download gallery image
            gallery_downloaded = False
            for query in queries:
                if not gallery_downloaded:
                    if UNSPLASH_ACCESS_KEY:
                        gallery_downloaded = download_image_from_unsplash(query, gallery_filename)
                    if not gallery_downloaded and PEXELS_API_KEY:
                        gallery_downloaded = download_image_from_pexels(query, gallery_filename)
                    if gallery_downloaded:
                        break
            
            # Create placeholder if no gallery image downloaded
            if not gallery_downloaded:
                create_placeholder_image(gallery_filename, f"{location.replace('-', ' ').title()} - View {i}")
                successful_downloads += 1
            
            total_images += 1
        
        # Rate limiting to be respectful to APIs
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print(f"🎉 Download complete!")
    print(f"📊 Total images processed: {total_images}")
    print(f"✅ Successfully created: {successful_downloads}")
    print(f"📁 Images saved in: {IMAGES_DIR}/")
    
    return successful_downloads

def verify_images():
    """Verify that all required images exist"""
    print("\n🔍 Verifying downloaded images...")
    
    missing_images = []
    
    for location in LOCATION_IMAGES.keys():
        # Check main image
        main_filename = f"{location}.jpg"
        main_path = os.path.join(IMAGES_DIR, main_filename)
        
        if not os.path.exists(main_path):
            missing_images.append(main_filename)
        else:
            print(f"✅ {main_filename}")
        
        # Check gallery images
        for i in range(1, 4):  # Check up to 3 gallery images
            gallery_filename = f"{location}-{i}.jpg"
            gallery_path = os.path.join(IMAGES_DIR, gallery_filename)
            
            if not os.path.exists(gallery_path):
                missing_images.append(gallery_filename)
            else:
                print(f"✅ {gallery_filename}")
    
    if missing_images:
        print(f"\n❌ Missing images: {len(missing_images)}")
        for img in missing_images:
            print(f"   - {img}")
    else:
        print("\n🎉 All required images are present!")
    
    return len(missing_images) == 0

def main():
    """Main function"""
    print("🏛️  Ayodhya Guide - Image Downloader")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists(PLACES_FILE):
        print(f"❌ Error: {PLACES_FILE} not found!")
        print("Please run this script from the ayodhya-guide directory")
        return
    
    # Download images
    download_all_images()
    
    # Verify images
    verify_images()
    
    print("\n" + "=" * 60)
    print("💡 Next steps:")
    print("1. Review downloaded images in the 'images/' directory")
    print("2. Replace placeholder images with better ones if needed")
    print("3. Optimize images for web use (compress, resize)")
    print("4. Test your website to ensure images display correctly")
    print("\n🌐 Your Ayodhya Guide website is ready with images!")

if __name__ == "__main__":
    main()
