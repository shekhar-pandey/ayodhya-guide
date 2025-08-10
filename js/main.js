// Main JavaScript file for Ayodhya Guide
// Handles search, card rendering, and main functionality

class AyodhyaGuide {
    constructor() {
        this.places = [];
        this.filteredPlaces = [];
        this.currentFilter = 'all';
        this.map = null;
        this.markers = [];
        this.init();
    }

    async init() {
        try {
            await this.loadPlaces();
            this.setupEventListeners();
            this.renderAttractions();
            this.initMap();
        } catch (error) {
            console.error('Error initializing Ayodhya Guide:', error);
        }
    }

    async loadPlaces() {
        try {
            const response = await fetch('data/places.json');
            this.places = await response.json();
            this.filteredPlaces = [...this.places];
        } catch (error) {
            console.error('Error loading places:', error);
            // Fallback data if JSON fails to load
            this.places = this.getFallbackPlaces();
            this.filteredPlaces = [...this.places];
        }
    }

    getFallbackPlaces() {
        return [
            {
                id: 1,
                name: "Ram Janmabhoomi Temple",
                slug: "ram-janmabhoomi-temple",
                category: "temple",
                description: "The sacred birthplace of Lord Rama, featuring magnificent architecture and spiritual significance.",
                image: "images/ram-temple.jpg",
                rating: 5.0,
                location: "Ram Janmabhoomi, Ayodhya",
                coordinates: [26.7991, 82.2044],
                timings: "5:00 AM - 9:00 PM",
                entryFee: "Free",
                bestTime: "Early morning for darshan"
            },
            {
                id: 2,
                name: "Hanuman Garhi",
                slug: "hanuman-garhi",
                category: "temple",
                description: "Ancient temple dedicated to Lord Hanuman, located on a hill with panoramic views of Ayodhya.",
                image: "images/hanuman-garhi.jpg",
                rating: 4.8,
                location: "Hanuman Garhi, Ayodhya",
                coordinates: [26.7991, 82.2044],
                timings: "6:00 AM - 8:00 PM",
                entryFee: "Free",
                bestTime: "Sunrise and sunset"
            },
            {
                id: 3,
                name: "Kanak Bhawan",
                slug: "kanak-bhawan",
                category: "temple",
                description: "Beautiful temple known for its golden architecture and intricate carvings.",
                image: "images/kanak-bhawan.jpg",
                rating: 4.6,
                location: "Kanak Bhawan, Ayodhya",
                coordinates: [26.7991, 82.2044],
                timings: "5:00 AM - 9:00 PM",
                entryFee: "Free",
                bestTime: "Morning hours"
            }
        ];
    }

    setupEventListeners() {
        // Search functionality
        const searchInput = document.getElementById('searchInput');
        const searchBtn = document.getElementById('searchBtn');
        
        if (searchInput) {
            searchInput.addEventListener('input', (e) => this.handleSearch(e.target.value));
        }
        
        if (searchBtn) {
            searchBtn.addEventListener('click', () => this.handleSearch(searchInput.value));
        }

        // Filter functionality
        const filterBtns = document.querySelectorAll('.filter-btn');
        filterBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const filter = e.target.dataset.filter;
                this.handleFilter(filter);
                
                // Update active state
                filterBtns.forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
            });
        });

        // Map controls
        const resetMapBtn = document.getElementById('resetMap');
        const showAllBtn = document.getElementById('showAll');
        
        if (resetMapBtn) {
            resetMapBtn.addEventListener('click', () => this.resetMap());
        }
        
        if (showAllBtn) {
            showAllBtn.addEventListener('click', () => this.showAllPlaces());
        }


    }

    handleSearch(query) {
        if (!query.trim()) {
            this.filteredPlaces = [...this.places];
        } else {
            const searchTerm = query.toLowerCase();
            this.filteredPlaces = this.places.filter(place => 
                place.name.toLowerCase().includes(searchTerm) ||
                place.description.toLowerCase().includes(searchTerm) ||
                place.category.toLowerCase().includes(searchTerm) ||
                place.location.toLowerCase().includes(searchTerm)
            );
        }
        
        this.renderAttractions();
        this.updateMapMarkers();
    }

    handleFilter(filter) {
        this.currentFilter = filter;
        
        if (filter === 'all') {
            this.filteredPlaces = [...this.places];
        } else {
            this.filteredPlaces = this.places.filter(place => 
                place.category.toLowerCase() === filter.toLowerCase()
            );
        }
        
        this.renderAttractions();
        this.updateMapMarkers();
    }

    renderAttractions() {
        const grid = document.getElementById('attractionsGrid');
        if (!grid) return;

        grid.innerHTML = '';
        
        if (this.filteredPlaces.length === 0) {
            grid.innerHTML = '<p class="no-results">No attractions found. Try adjusting your search or filters.</p>';
            return;
        }

        this.filteredPlaces.forEach(place => {
            const card = this.createAttractionCard(place);
            grid.appendChild(card);
        });
    }

    createAttractionCard(place) {
        const card = document.createElement('div');
        card.className = 'attraction-card';
        
        const imageUrl = place.image || 'images/default-temple.jpg';
        
        card.innerHTML = `
            <div class="attraction-image">
                <img src="${imageUrl}" alt="${place.name}" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
                <div class="attraction-image-fallback" style="display: none; background: linear-gradient(135deg, #8B4513, #D2691E); color: white; height: 200px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; text-align: center; padding: 1rem;">
                    <div>🏛️<br>${place.name}</div>
                </div>
            </div>
            <div class="attraction-content">
                <div class="attraction-category">${this.capitalizeFirst(place.category)}</div>
                <h3 class="attraction-title">${place.name}</h3>
                <p class="attraction-description">${place.description}</p>
                <div class="attraction-rating">
                    <span class="stars">${this.getStars(place.rating)}</span>
                    <span class="rating-text">${place.rating}/5</span>
                </div>
                <div class="attraction-actions">
                    <a href="place.html?slug=${place.slug}" class="btn btn-primary">Learn More</a>
                    <button class="btn btn-secondary" onclick="sharePlace(${JSON.stringify(place).replace(/"/g, '&quot;')})">Share</button>
                </div>
            </div>
        `;
        
        return card;
    }

    capitalizeFirst(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    getStars(rating) {
        const fullStars = Math.floor(rating);
        const hasHalfStar = rating % 1 !== 0;
        const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);
        
        return '★'.repeat(fullStars) + (hasHalfStar ? '☆' : '') + '☆'.repeat(emptyStars);
    }

    initMap() {
        const mapContainer = document.getElementById('map');
        if (!mapContainer) return;

        // Initialize Leaflet map centered on Ayodhya
        this.map = L.map('map').setView([26.7991, 82.2044], 13);

        // Add OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(this.map);

        // Add all places as markers
        this.addMapMarkers();

        // Add map controls
        this.addMapControls();
    }

    addMapMarkers() {
        // Clear existing markers
        this.markers.forEach(marker => this.map.removeLayer(marker));
        this.markers = [];

        // Add markers for all places
        this.places.forEach(place => {
            if (place.coordinates && place.coordinates.length === 2) {
                const [lat, lng] = place.coordinates;
                
                // Create custom icon based on category
                const icon = this.createCustomIcon(place.category);
                
                // Create marker
                const marker = L.marker([lat, lng], { icon: icon })
                    .addTo(this.map)
                    .bindPopup(this.createPopupContent(place));
                
                this.markers.push(marker);
            }
        });
    }

    createCustomIcon(category) {
        const iconColors = {
            temple: '#ff9800',
            historical: '#4caf50',
            cultural: '#9c27b0'
        };

        return L.divIcon({
            className: 'custom-marker',
            html: `<div style="background-color: ${iconColors[category] || '#666'}; width: 20px; height: 20px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.3);"></div>`,
            iconSize: [20, 20],
            iconAnchor: [10, 10]
        });
    }

    createPopupContent(place) {
        const imageUrl = place.image || 'images/default-temple.jpg';
        
        return `
            <div class="map-popup">
                <div class="popup-image">
                    <img src="${imageUrl}" alt="${place.name}" style="width: 100%; height: 100px; object-fit: cover; border-radius: 8px;" onerror="this.style.display='none';">
                </div>
                <h3 style="margin: 8px 0; color: #333;">${place.name}</h3>
                <p style="margin: 0 0 8px 0; color: #666; font-size: 0.9em;">${place.description.substring(0, 100)}...</p>
                <div style="display: flex; gap: 8px;">
                    <span style="background: #e3f2fd; color: #1976d2; padding: 4px 8px; border-radius: 12px; font-size: 0.8em;">${this.capitalizeFirst(place.category)}</span>
                    <span style="color: #ffc107;">★ ${place.rating}</span>
                </div>
                <a href="place.html?slug=${place.slug}" style="display: block; margin-top: 8px; text-align: center; background: #1976d2; color: white; padding: 6px 12px; text-decoration: none; border-radius: 6px; font-size: 0.9em;">Learn More</a>
            </div>
        `;
    }

    addMapControls() {
        // Add scale control
        L.control.scale().addTo(this.map);
        
        // Add fullscreen control
        L.control.fullscreen({
            position: 'topleft',
            title: 'Full Screen',
            titleCancel: 'Exit Full Screen'
        }).addTo(this.map);
    }

    updateMapMarkers() {
        if (!this.map) return;

        // Clear all markers
        this.markers.forEach(marker => this.map.removeLayer(marker));
        this.markers = [];

        // Add markers only for filtered places
        this.filteredPlaces.forEach(place => {
            if (place.coordinates && place.coordinates.length === 2) {
                const [lat, lng] = place.coordinates;
                
                const icon = this.createCustomIcon(place.category);
                const marker = L.marker([lat, lng], { icon: icon })
                    .addTo(this.map)
                    .bindPopup(this.createPopupContent(place));
                
                this.markers.push(marker);
            }
        });

        // Fit map to show all visible markers
        if (this.markers.length > 0) {
            const group = new L.featureGroup(this.markers);
            this.map.fitBounds(group.getBounds().pad(0.1));
        }
    }

    resetMap() {
        this.currentFilter = 'all';
        this.filteredPlaces = [...this.places];
        this.renderAttractions();
        this.updateMapMarkers();
        
        // Reset filter buttons
        const filterBtns = document.querySelectorAll('.filter-btn');
        filterBtns.forEach(btn => btn.classList.remove('active'));
        document.querySelector('[data-filter="all"]')?.classList.add('active');
    }

    showAllPlaces() {
        this.resetMap();
    }


}

// Share functionality
function sharePlace(placeData) {
    if (navigator.share) {
        navigator.share({
            title: placeData.name,
            text: `Check out ${placeData.name} in Ayodhya: ${placeData.description}`,
            url: window.location.origin + '/place.html?slug=' + placeData.slug
        });
    } else {
        // Fallback for browsers that don't support Web Share API
        const shareText = `${placeData.name} - ${placeData.description}`;
        if (navigator.clipboard) {
            navigator.clipboard.writeText(shareText).then(() => {
                alert('Place information copied to clipboard!');
            });
        } else {
            alert(shareText);
        }
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    new AyodhyaGuide();
});
