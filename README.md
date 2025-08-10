# Ayodhya Guide - Holy City Pilgrimage Guide

A comprehensive guide to the sacred city of Ayodhya, featuring interactive maps, detailed information about temples and holy sites, and a working contact form system.

## ✨ Features

- **Interactive Map** - Explore Ayodhya's sacred sites with Leaflet.js
- **Place Details** - Comprehensive information about temples, ghats, and historical sites
- **Search & Filter** - Find places by category or search terms
- **Contact Forms** - Working contact forms for inquiries and support
- **Responsive Design** - Mobile-friendly interface
- **Backend API** - FastAPI-powered backend for dynamic content

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd ayodhya-guide
```

### 2. Start the Backend Server
```bash
cd backend
python start_server.py
```
The API will be available at `http://localhost:8000`

### 3. Open the Website
Open `index.html` in your browser or serve the files using a local server.

## 📁 Project Structure

```
ayodhya-guide/
├── index.html              # Main homepage
├── contact.html            # Contact page with working form
├── about.html              # About page
├── place.html              # Individual place details page
├── css/                    # Stylesheets
├── js/                     # JavaScript files
├── images/                 # Temple and site images
├── backend/                # FastAPI backend
│   ├── app/
│   │   ├── main.py        # Main API server
│   │   └── data/          # Places data
│   ├── start_server.py    # Server startup script
│   └── requirements.txt   # Python dependencies
└── test-contact-local.html # Test page for contact form
```

## 🔧 Contact Form Setup

The contact forms have been fixed and now work with a local backend API. See `CONTACT_FORM_SETUP.md` for detailed information.

### Features:
- ✅ Form validation
- ✅ Loading states  
- ✅ Success/error messages
- ✅ Subject field support
- ✅ Backend logging

## 🌐 API Endpoints

- `GET /` - API information
- `GET /api/places` - All places
- `GET /api/places/{slug}` - Specific place
- `GET /api/categories` - All categories
- `POST /api/search` - Search places
- `POST /api/contact` - Submit contact form

## 🛠️ Development

### Backend Development
```bash
cd backend
pip install -r requirements.txt
python start_server.py
```

### Frontend Development
The frontend is pure HTML/CSS/JavaScript and can be opened directly in a browser.

## 📱 Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## 🚀 Deployment

### Local Development
1. Start the backend server
2. Open HTML files in your browser
3. Use `test-contact-local.html` to test the contact form

### Production Deployment
1. Deploy the backend to a hosting service (Heroku, Render, etc.)
2. Update the frontend fetch URLs to point to your production backend
3. Set up proper CORS and security measures

## 📞 Support

For questions or issues:
- Email: abcxyzsp9@gmail.com
- Phone: +91 9997457651

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Images courtesy of UP Tourism & District Ayodhya
- Built with FastAPI, Leaflet.js, and modern web technologies
