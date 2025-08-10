# Static Assets Directory

This directory contains static assets that will be copied to the deployment root.

## Common Static Assets

### Fonts
- Custom web fonts (if using)
- Icon fonts (Font Awesome, Material Icons, etc.)

### Icons
- Favicon files (favicon.ico, apple-touch-icon.png, etc.)
- Social media icons
- Custom SVG icons

### Other Assets
- Robots.txt
- Sitemap.xml
- Manifest.json (for PWA)
- Service worker files

## File Structure Example

```
static/
├── fonts/
│   ├── custom-font.woff2
│   └── icon-font.woff2
├── icons/
│   ├── favicon.ico
│   ├── apple-touch-icon.png
│   └── social-icons/
├── robots.txt
├── sitemap.xml
└── manifest.json
```

## Deployment

Files in this directory will be copied to the root of your deployment (e.g., GitHub Pages, Netlify, etc.) alongside your HTML, CSS, and JavaScript files.

## Optimization

- Compress all assets before deployment
- Use appropriate file formats (WebP for images, WOFF2 for fonts)
- Consider using CDNs for common libraries
