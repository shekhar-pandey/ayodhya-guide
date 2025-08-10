// Place.js - Handles single place page functionality
// Loads place data by slug and manages place-specific interactions

class PlacePage {
    constructor() {
        this.place = null;
        this.slug = this.getSlugFromURL();
        
        this.init();
    }

    init() {
        if (!this.slug) {
            this.showError('No place specified');
            return;
        }

        this.loadPlaceData();
        this.setupEventListeners();
    }

    getSlugFromURL() {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get('slug');
    }

    async loadPlaceData() {
        try {
            // First try to load from the main places.json
            const response = await fetch('../data/places.json');
            const places = await response.json();
            
            this.place = places.find(p => p.slug === this.slug);
            
            if (!this.place) {
                // If not found, try fallback data
                this.place = this.getFallbackPlaceData();
            }
            
            if (this.place) {
                this.renderPlaceData();
                this.updatePageTitle();
                this.initMiniMap();
            } else {
                this.showError('Place not found');
            }
        } catch (error) {
            console.error('Error loading place data:', error);
            // Use fallback data
            this.place = this.getFallbackPlaceData();
            if (this.place) {
                this.renderPlaceData();
                this.updatePageTitle();
                this.initMiniMap();
            } else {
                this.showError('Failed to load place data');
            }
        }
    }

    getFallbackPlaceData() {
        const fallbackPlaces = {
            'ram-janmabhoomi-temple': {
                id: 1,
                name: "Ram Janmabhoomi Temple",
                slug: "ram-janmabhoomi-temple",
                category: "temple",
                description: "The sacred birthplace of Lord Rama, featuring magnificent architecture and spiritual significance. This temple stands as a symbol of faith and devotion for millions of Hindus worldwide.",
                image: "../images/ram-temple.jpg",
                rating: 5.0,
                location: "Ram Janmabhoomi, Ayodhya, Uttar Pradesh, India",
                coordinates: [26.7991, 82.2044],
                timings: "5:00 AM - 9:00 PM (All days)",
                entryFee: "Free entry for all devotees",
                bestTime: "Early morning (5:00 AM - 8:00 AM) for peaceful darshan",
                history: "The Ram Janmabhoomi Temple is built at the sacred site where Lord Rama, the seventh avatar of Lord Vishnu, was born. According to ancient texts, this site has been revered for thousands of years. The temple complex showcases the finest examples of traditional Indian architecture and serves as a center for spiritual learning and cultural preservation.",
                tips: [
                    "Visit early morning for the best spiritual experience",
                    "Dress modestly and remove footwear before entering",
                    "Photography may be restricted in certain areas",
                    "Participate in the evening aarti for a complete experience",
                    "Plan your visit during weekdays to avoid large crowds"
                ],
                gallery: [
                    "../images/ram-temple-1.jpg",
                    "../images/ram-temple-2.jpg",
                    "../images/ram-temple-3.jpg"
                ]
            },
            'hanuman-garhi': {
                id: 2,
                name: "Hanuman Garhi",
                slug: "hanuman-garhi",
                category: "temple",
                description: "Ancient temple dedicated to Lord Hanuman, located on a hill with panoramic views of Ayodhya. This sacred site is known for its spiritual energy and architectural beauty.",
                image: "../images/hanuman-garhi.jpg",
                rating: 4.8,
                location: "Hanuman Garhi, Ayodhya, Uttar Pradesh, India",
                coordinates: [26.7991, 82.2044],
                timings: "6:00 AM - 8:00 PM (All days)",
                entryFee: "Free entry for all devotees",
                bestTime: "Sunrise and sunset for the best views and spiritual atmosphere",
                history: "Hanuman Garhi is one of the most important temples in Ayodhya, dedicated to Lord Hanuman, the greatest devotee of Lord Rama. The temple is built on a hill and offers spectacular views of the entire city. According to legend, Lord Hanuman lived here to protect the city of Ayodhya.",
                tips: [
                    "Climb the hill early morning for the best experience",
                    "Don't miss the sunset view from the temple",
                    "Wear comfortable shoes for the climb",
                    "Visit during Hanuman Jayanti for special celebrations",
                    "Take time to meditate in the peaceful surroundings"
                ],
                gallery: [
                    "../images/hanuman-garhi-1.jpg",
                    "../images/hanuman-garhi-2.jpg",
                    "../images/hanuman-garhi-3.jpg"
                ]
            },
            'kanak-bhawan': {
                id: 3,
                name: "Kanak Bhawan",
                slug: "kanak-bhawan",
                category: "temple",
                description: "Beautiful temple known for its golden architecture and intricate carvings. This temple is dedicated to Lord Rama and Goddess Sita, showcasing the finest examples of traditional craftsmanship.",
                image: "../images/kanak-bhawan.jpg",
                rating: 4.6,
                location: "Kanak Bhawan, Ayodhya, Uttar Pradesh, India",
                coordinates: [26.7991, 82.2044],
                timings: "5:00 AM - 9:00 PM (All days)",
                entryFee: "Free entry for all devotees",
                bestTime: "Morning hours for peaceful darshan and photography",
                history: "Kanak Bhawan, also known as the Golden Palace, is one of the most beautiful temples in Ayodhya. According to legend, this temple was gifted to Goddess Sita by her mother. The temple's architecture reflects the rich cultural heritage of ancient India and serves as a testament to the skilled craftsmanship of the era.",
                tips: [
                    "Visit during morning hours for the best lighting",
                    "Admire the intricate carvings and architecture",
                    "Participate in the morning aarti",
                    "Take photographs of the beautiful facade",
                    "Learn about the temple's history from local guides"
                ],
                gallery: [
                    "../images/kanak-bhawan-1.jpg",
                    "../images/kanak-bhawan-2.jpg",
                    "../images/kanak-bhawan-3.jpg"
                ]
            }
        };

        return fallbackPlaces[this.slug];
    }

    renderPlaceData() {
        if (!this.place) return;

        // Update page elements
        this.updateElement('placeName', this.place.name);
        this.updateElement('placeTitle', this.place.name);
        this.updateElement('placeCategory', this.place.category);
        this.updateElement('placeRating', this.place.rating);
        this.updateElement('placeDescription', this.place.description);
        this.updateElement('placeLocation', this.place.location);
        this.updateElement('placeTimings', this.place.timings);
        this.updateElement('placeEntryFee', this.place.entryFee);
        this.updateElement('placeBestTime', this.place.bestTime);

        // Update image
        const placeImage = document.getElementById('placeImage');
        if (placeImage) {
            placeImage.src = this.place.image;
            placeImage.alt = this.place.name;
            placeImage.onerror = () => {
                placeImage.src = '../images/placeholder.jpg';
            };
        }

        // Render history
        if (this.place.history) {
            this.updateElement('placeHistory', this.place.history);
        }

        // Render tips
        if (this.place.tips) {
            const tipsHtml = this.place.tips.map(tip => `<li>${tip}</li>`).join('');
            this.updateElement('placeTips', `<ul>${tipsHtml}</ul>`);
        }

        // Render gallery
        if (this.place.gallery) {
            this.renderGallery();
        }
    }

    updateElement(id, content) {
        const element = document.getElementById(id);
        if (element) {
            element.textContent = content;
        }
    }

    renderGallery() {
        const galleryContainer = document.getElementById('placeGallery');
        if (!galleryContainer || !this.place.gallery) return;

        const galleryHtml = this.place.gallery.map(image => `
            <div class="gallery-item">
                <img src="${image}" alt="${this.place.name}" 
                     onerror="this.src='../images/placeholder.jpg'">
            </div>
        `).join('');

        galleryContainer.innerHTML = galleryHtml;
    }

    updatePageTitle() {
        if (this.place) {
            document.title = `${this.place.name} - Ayodhya Guide`;
        }
    }

    initMiniMap() {
        const miniMap = document.getElementById('placeMap');
        if (!miniMap || !this.place.coordinates) return;

        // Create a simple map representation
        miniMap.innerHTML = `
            <div style="display: flex; align-items: center; justify-content: center; height: 100%; background: #e9ecef; color: #6c757d; border-radius: 10px;">
                <div style="text-align: center;">
                    <h4>Location</h4>
                    <p>${this.place.location}</p>
                    <p>Coordinates: ${this.place.coordinates[0]}°N, ${this.place.coordinates[1]}°E</p>
                </div>
            </div>
        `;
    }

    setupEventListeners() {
        // Show on map button
        const showOnMapBtn = document.getElementById('showOnMap');
        if (showOnMapBtn) {
            showOnMapBtn.addEventListener('click', () => {
                this.showOnMap();
            });
        }

        // Share button
        const shareBtn = document.getElementById('sharePlace');
        if (shareBtn) {
            shareBtn.addEventListener('click', () => {
                this.sharePlace();
            });
        }
    }

    showOnMap() {
        if (!this.place || !this.place.coordinates) return;

        // In a real implementation, this would open the main page with the map centered on this location
        const mainPageUrl = `../index.html?center=${this.place.coordinates[0]},${this.place.coordinates[1]}&place=${this.place.slug}`;
        window.open(mainPageUrl, '_blank');
    }

    sharePlace() {
        if (!this.place) return;

        const shareData = {
            title: this.place.name,
            text: this.place.description,
            url: window.location.href
        };

        if (navigator.share) {
            navigator.share(shareData);
        } else {
            // Fallback for browsers that don't support Web Share API
            this.copyToClipboard(`${this.place.name} - ${this.place.description}\n\n${window.location.href}`);
        }
    }

    copyToClipboard(text) {
        if (navigator.clipboard) {
            navigator.clipboard.writeText(text).then(() => {
                this.showMessage('Link copied to clipboard!');
            });
        } else {
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            this.showMessage('Link copied to clipboard!');
        }
    }

    showMessage(message) {
        // Create a simple toast message
        const toast = document.createElement('div');
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #D2691E;
            color: white;
            padding: 1rem 2rem;
            border-radius: 10px;
            z-index: 1000;
            animation: slideIn 0.3s ease;
        `;
        toast.textContent = message;
        
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                document.body.removeChild(toast);
            }, 300);
        }, 3000);
    }

    showError(message) {
        const mainContent = document.querySelector('.main-content');
        if (mainContent) {
            mainContent.innerHTML = `
                <div class="container">
                    <div class="error-message" style="text-align: center; padding: 4rem 0;">
                        <h2>Error</h2>
                        <p>${message}</p>
                        <a href="../index.html" class="btn btn-primary">Return to Home</a>
                    </div>
                </div>
            `;
        }
    }
}

// Add CSS animations for toast messages
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Initialize the place page when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new PlacePage();
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PlacePage;
}
