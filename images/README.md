# Images for Ayodhya Guide

This directory contains images for the Ayodhya Guide tourist application. Currently, the application uses placeholder images, but you can replace them with real images from the Uttar Pradesh Tourism website.

## 🖼️ Required Images

### Main Location Images (Required)
- `ram-temple.jpg` - Ram Janmabhoomi Temple
- `hanuman-garhi.jpg` - Hanuman Garhi Temple
- `kanak-bhawan.jpg` - Kanak Bhawan Temple
- `nageshwarnath-temple.jpg` - Nageshwarnath Temple
- `treta-ke-thakur.jpg` - Treta Ke Thakur
- `chhoti-devkali.jpg` - Chhoti Devkali Temple
- `sarayu-ghats.jpg` - Sarayu River Ghats
- `ayodhya-fort.jpg` - Ayodhya Fort
- `gulab-bari.jpg` - Gulab Bari
- `mani-parbat.jpg` - Mani Parbat

### Gallery Images (Optional)
- `ram-temple-1.jpg`, `ram-temple-2.jpg`, `ram-temple-3.jpg`
- `hanuman-garhi-1.jpg`, `hanuman-garhi-2.jpg`, `hanuman-garhi-3.jpg`
- `kanak-bhawan-1.jpg`, `kanak-bhawan-2.jpg`, `kanak-bhawan-3.jpg`
- And more gallery images for each location

## 📥 How to Get Real Images

### Option 1: UP Tourism Website
1. Visit: https://uptourism.gov.in/en/dynamic/photogallery?slug=en-ayodhya
2. Browse through the photo gallery
3. Right-click on images and "Save Image As..."
4. Rename them according to the required filenames above
5. Place them in this `images/` directory

### Option 2: Download from UP Tourism API
The website may have an API endpoint for images. Check the network tab in browser developer tools for image URLs.

### Option 3: Use Placeholder Images (Current Setup)
The application currently uses placeholder images from placeholder.com, which will work for testing and development.

## 🎯 Image Specifications

### Recommended Image Sizes
- **Main Images**: 800x600 pixels (16:9 ratio)
- **Gallery Images**: 600x400 pixels (3:2 ratio)
- **Thumbnails**: 300x200 pixels (3:2 ratio)

### File Formats
- **Primary**: JPG/JPEG (good compression, web-friendly)
- **Alternative**: PNG (if transparency is needed)
- **WebP**: Modern format with better compression (optional)

### File Size
- Keep images under 500KB for main images
- Keep gallery images under 300KB
- Optimize for web use

## 🔧 Image Optimization

### Before Uploading
1. **Resize**: Use appropriate dimensions
2. **Compress**: Reduce file size while maintaining quality
3. **Format**: Convert to JPG for photos, PNG for graphics
4. **Metadata**: Remove unnecessary EXIF data

### Tools for Optimization
- **Online**: TinyPNG, Compressor.io, Squoosh.app
- **Desktop**: GIMP, Photoshop, ImageOptim (Mac)
- **Command Line**: ImageMagick, jpegoptim

## 📱 Responsive Images

The application automatically handles responsive images:
- Images scale appropriately on different screen sizes
- Placeholder images are used as fallbacks
- CSS ensures proper aspect ratios

## 🚨 Troubleshooting

### Images Not Loading
1. Check file paths in `places.json`
2. Verify image files exist in the `images/` directory
3. Check file permissions
4. Ensure correct file extensions

### Broken Image Links
1. Verify image URLs in the JSON data
2. Check for typos in filenames
3. Ensure images are in the correct directory

### Performance Issues
1. Optimize image sizes
2. Use appropriate compression
3. Consider lazy loading for gallery images

## 📋 Quick Setup Commands

```bash
# Create images directory if it doesn't exist
mkdir -p images

# Download a sample image (replace URL with actual image)
curl -o images/ram-temple.jpg "https://example.com/ram-temple.jpg"

# Optimize images using ImageMagick (if installed)
mogrify -resize 800x600 -quality 85 images/*.jpg
```

## 🌟 Current Status

- ✅ Application works with placeholder images
- ✅ All image references are properly configured
- ✅ Fallback images are implemented
- ⏳ Real images need to be downloaded and added

## 📞 Support

If you need help with images:
1. Check the main README.md for troubleshooting
2. Verify image file paths and names
3. Test with placeholder images first
4. Ensure proper file permissions

---

**Note**: The application will work perfectly with placeholder images for development and testing. Real images will enhance the user experience but are not required for functionality.
