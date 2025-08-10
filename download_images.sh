#!/bin/bash

# Ayodhya Guide - Image Downloader Shell Script
# This script downloads high-quality, free images for the Ayodhya Guide website

echo "🏛️  Ayodhya Guide - Image Downloader"
echo "======================================"

# Check if we're in the right directory
if [ ! -f "data/places.json" ]; then
    echo "❌ Error: data/places.json not found!"
    echo "Please run this script from the ayodhya-guide directory"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed!"
    echo "Please install Python 3 and try again"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 is not installed!"
    echo "Please install pip3 and try again"
    exit 1
fi

# Install required packages
echo "📦 Installing required Python packages..."
pip3 install requests pathlib

# Run the Python script
echo "🚀 Starting image download..."
python3 download_images.py

# Check if images were downloaded successfully
if [ -d "images" ] && [ "$(ls -A images)" ]; then
    echo ""
    echo "🎉 Success! Images have been downloaded to the 'images/' directory"
    echo ""
    echo "📁 Available images:"
    ls -la images/
    echo ""
    echo "🌐 Your Ayodhya Guide website is now ready with images!"
else
    echo ""
    echo "⚠️  No images were downloaded. Check the error messages above."
    echo "The script will create placeholder images as fallbacks."
fi
