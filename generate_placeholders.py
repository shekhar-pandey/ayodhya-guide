#!/usr/bin/env python3
"""
Simple Placeholder Image Generator for Ayodhya Guide
Creates basic colored rectangles as placeholder images
"""

import os
from PIL import Image, ImageDraw, ImageFont
import json

def create_placeholder_image(filename, name, color, category, size=(800, 600)):
    """Create a simple placeholder image"""
    # Create image with background color
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        # Try to use a system font
        font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
        font_small = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
    except:
        try:
            # Try alternative font paths
            font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
            font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        except:
            # Use default font
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
    
    # Calculate text positions
    text_bbox = draw.textbbox((0, 0), name, font=font_large)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2 - 30
    
    # Draw main text
    draw.text((x, y), name, fill='white', font=font_large)
    
    # Draw category text
    category_bbox = draw.textbbox((0, 0), category, font=font_small)
    category_width = category_bbox[2] - category_bbox[0]
    category_x = (size[0] - category_width) // 2
    category_y = y + text_height + 20
    
    draw.text((category_x, category_y), category, fill='white', font=font_small)
    
    # Draw border
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline='white', width=3)
    
    return img

def main():
    print("🖼️  Generating placeholder images for Ayodhya Guide...")
    
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # Define required images
    required_images = [
        {'filename': 'ram-temple.jpg', 'name': 'Ram Temple', 'color': (255, 107, 53), 'category': 'Temple'},
        {'filename': 'hanuman-garhi.jpg', 'name': 'Hanuman Garhi', 'color': (76, 175, 80), 'category': 'Temple'},
        {'filename': 'kanak-bhawan.jpg', 'name': 'Kanak Bhawan', 'color': (156, 39, 176), 'category': 'Temple'},
        {'filename': 'nageshwarnath-temple.jpg', 'name': 'Nageshwarnath Temple', 'color': (33, 150, 243), 'category': 'Temple'},
        {'filename': 'treta-ke-thakur.jpg', 'name': 'Treta Ke Thakur', 'color': (255, 152, 0), 'category': 'Historical'},
        {'filename': 'chhoti-devkali.jpg', 'name': 'Chhoti Devkali', 'color': (121, 85, 72), 'category': 'Temple'},
        {'filename': 'sarayu-ghats.jpg', 'name': 'Sarayu Ghats', 'color': (96, 125, 139), 'category': 'Cultural'},
        {'filename': 'ayodhya-fort.jpg', 'name': 'Ayodhya Fort', 'color': (233, 30, 99), 'category': 'Historical'},
        {'filename': 'gulab-bari.jpg', 'name': 'Gulab Bari', 'color': (103, 58, 183), 'category': 'Cultural'},
        {'filename': 'mani-parbat.jpg', 'name': 'Mani Parbat', 'color': (63, 81, 181), 'category': 'Historical'}
    ]
    
    # Generate images
    generated_count = 0
    for img_data in required_images:
        try:
            img = create_placeholder_image(
                img_data['filename'],
                img_data['name'],
                img_data['color'],
                img_data['category']
            )
            
            # Save image
            filepath = os.path.join('images', img_data['filename'])
            img.save(filepath, 'JPEG', quality=85)
            print(f"✅ Generated: {img_data['filename']}")
            generated_count += 1
            
        except Exception as e:
            print(f"❌ Error generating {img_data['filename']}: {e}")
    
    print(f"\n🎉 Generated {generated_count}/{len(required_images)} placeholder images")
    print(f"📁 Images saved to: {os.path.abspath('images')}")
    
    # Create a simple status file
    status = {
        'generated_images': [img['filename'] for img in required_images[:generated_count]],
        'total_required': len(required_images),
        'total_generated': generated_count,
        'status': 'ready' if generated_count == len(required_images) else 'partial'
    }
    
    with open('image_status.json', 'w') as f:
        json.dump(status, f, indent=2)
    
    print(f"\n📄 Status saved to: image_status.json")
    print("\n🎯 Next Steps:")
    print("1. Check the 'images/' directory for generated placeholder images")
    print("2. Test your application - images should now load properly")
    print("3. To get real images, visit: https://uptourism.gov.in/en/dynamic/photogallery?slug=en-ayodhya")
    print("4. Replace placeholder images with real ones when available")

if __name__ == "__main__":
    main()
