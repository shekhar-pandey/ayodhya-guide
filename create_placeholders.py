#!/usr/bin/env python3
"""
Create simple placeholder images for Ayodhya Guide
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(filename, text, size=(800, 600), bg_color=(74, 144, 226), text_color=(255, 255, 255)):
    """Create a simple placeholder image"""
    try:
        # Create image
        img = Image.new('RGB', size, bg_color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a default font, fallback to basic if not available
        try:
            # Try to use a larger font
            font_size = min(size) // 10
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
            except:
                font = ImageFont.load_default()
        
        # Calculate text position (center)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (size[0] - text_width) // 2
        y = (size[1] - text_height) // 2
        
        # Draw text
        draw.text((x, y), text, fill=text_color, font=font)
        
        # Save image
        filepath = os.path.join("images", filename)
        img.save(filepath, "JPEG", quality=85)
        print(f"✅ Created: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create {filename}: {e}")
        return False

def create_all_placeholders():
    """Create placeholder images for all locations"""
    print("🎨 Creating placeholder images for Ayodhya Guide...")
    
    # Ensure images directory exists
    os.makedirs("images", exist_ok=True)
    
    # Main location images
    locations = {
        "ram-temple.jpg": "Ram Janmabhoomi Temple",
        "hanuman-garhi.jpg": "Hanuman Garhi",
        "kanak-bhawan.jpg": "Kanak Bhawan",
        "nageshwarnath-temple.jpg": "Nageshwarnath Temple",
        "treta-ke-thakur.jpg": "Treta Ke Thakur",
        "chhoti-devkali.jpg": "Chhoti Devkali",
        "sarayu-ghats.jpg": "Sarayu River Ghats",
        "ayodhya-fort.jpg": "Ayodhya Fort",
        "gulab-bari.jpg": "Gulab Bari",
        "mani-parbat.jpg": "Mani Parbat"
    }
    
    # Gallery images
    gallery_images = {}
    for location in locations.keys():
        base_name = location.replace('.jpg', '')
        for i in range(1, 4):  # Create 3 gallery images per location
            gallery_images[f"{base_name}-{i}.jpg"] = f"{locations[location]} - View {i}"
    
    # Create all images
    all_images = {**locations, **gallery_images}
    
    success_count = 0
    for filename, text in all_images.items():
        if create_placeholder_image(filename, text):
            success_count += 1
    
    print(f"\n🎉 Created {success_count}/{len(all_images)} placeholder images!")
    print("📁 Images saved in: images/")
    
    return success_count

if __name__ == "__main__":
    create_all_placeholders()
