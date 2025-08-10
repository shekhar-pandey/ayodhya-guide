# Ayodhya Guide - Interactive Tourist Guide

A modern, interactive web application showcasing the sacred city of Ayodhya, featuring an interactive map powered by Leaflet.js, search functionality, and detailed information about temples, historical sites, and cultural attractions.

## 🌟 Features

- **Interactive Map**: Powered by Leaflet.js with OpenStreetMap tiles
- **Location Markers**: Color-coded markers for different categories (temples, historical, cultural)
- **Search & Filter**: Find attractions by name, description, or category
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Rich Content**: Detailed information about each location with images, ratings, and tips
- **Modern UI**: Beautiful, intuitive interface with smooth animations

## 🚀 Quick Start

### Option 1: Open Directly in Browser
1. Download or clone this repository
2. Open `index.html` in your web browser
3. The application will load with the interactive map

### Option 2: Local Server (Recommended)
1. Navigate to the project directory
2. Start a local server:

**Using Python 3:**
```bash
python -m http.server 8000
```

**Using Python 2:**
```bash
python -m SimpleHTTPServer 8000
```

**Using Node.js:**
```bash
npx http-server
```

3. Open your browser and go to `http://localhost:8000`

### Option 3: Test Leaflet.js Integration
1. Open `test.html` in your browser to test the map functionality
2. This file contains a simplified version to verify Leaflet.js is working

## 🗺️ Map Features

- **Interactive Markers**: Click on any marker to see location details
- **Category Colors**: 
  - 🟠 Orange: Temples
  - 🟢 Green: Historical sites
  - 🟣 Purple: Cultural attractions
- **Zoom Controls**: Standard map zoom in/out functionality
- **Responsive**: Automatically adjusts to show all visible markers
- **Search Integration**: Map updates based on search and filter results

## 🔧 Technical Details

### Dependencies
- **Leaflet.js 1.9.4**: Interactive mapping library
- **Leaflet.fullscreen**: Fullscreen map control
- **OpenStreetMap**: Free map tiles

### Browser Support
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

### File Structure
```
ayodhya-guide/
├── index.html          # Main application page
├── test.html          # Leaflet.js test page
├── css/
│   └── style.css      # Application styles
├── js/
│   └── main.js        # Main application logic
├── data/
│   └── places.json    # Location data
└── images/            # Location images
```

## 🐛 Troubleshooting

### Map Not Loading
1. **Check Console**: Open browser developer tools (F12) and check for JavaScript errors
2. **Internet Connection**: Ensure you have internet access for loading map tiles
3. **File Paths**: Make sure all files are in the correct directory structure
4. **Browser Compatibility**: Try a different browser or update your current browser

### Common Issues

**"L is not defined" Error:**
- This means Leaflet.js didn't load properly
- Check if the CDN links are accessible
- Verify the script tags are in the correct order

**Map Container Not Found:**
- Ensure the HTML has a `<div id="map">` element
- Check that the JavaScript runs after the DOM is loaded

**Markers Not Showing:**
- Verify the `places.json` file is accessible
- Check that coordinates are in the correct format `[latitude, longitude]`
- Ensure the JSON file has valid syntax

### Testing the Map
1. Open `test.html` first to verify Leaflet.js is working
2. Check browser console for any error messages
3. Verify that map tiles load (you should see a world map)
4. Test marker functionality by clicking on markers

## 📱 Mobile Optimization

The application is fully responsive and optimized for mobile devices:
- Touch-friendly map controls
- Responsive grid layouts
- Mobile-optimized navigation
- Fast loading on mobile networks

## 🔒 Security Notes

- The application uses CDN links for external libraries
- All map data is loaded from local JSON files
- No external API calls are made
- Consider hosting libraries locally for production use

## 🚀 Deployment

### GitHub Pages
1. Push your code to a GitHub repository
2. Enable GitHub Pages in repository settings
3. Select source branch (usually `main` or `master`)
4. Your site will be available at `https://username.github.io/repository-name`

### Netlify
1. Drag and drop the project folder to Netlify
2. Your site will be deployed automatically
3. Custom domain can be configured in settings

### Vercel
1. Connect your GitHub repository to Vercel
2. Deploy automatically on every push
3. Get a production URL instantly

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Review browser console for error messages
3. Ensure all files are in the correct locations
4. Test with the `test.html` file first

---

**Happy Exploring! 🗺️✨**

Discover the spiritual heritage of Ayodhya, the birthplace of Lord Rama, through this interactive guide.
