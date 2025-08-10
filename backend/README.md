# Ayodhya Guide Backend

This is the backend API server for the Ayodhya Guide application.

## Quick Start

### Option 1: Using the startup script (Recommended)
```bash
cd ayodhya-guide/backend
python start_server.py
```

### Option 2: Using uvicorn directly
```bash
cd ayodhya-guide/backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /` - API information
- `GET /api/places` - Get all places
- `GET /api/places/{slug}` - Get specific place
- `GET /api/categories` - Get all categories
- `POST /api/search` - Search places
- `POST /api/contact` - Submit contact form
- `GET /health` - Health check

## Contact Form

The contact form endpoint accepts:
```json
{
  "name": "User Name",
  "email": "user@example.com",
  "subject": "Optional Subject",
  "message": "User message"
}
```

## Dependencies

Install with:
```bash
pip install -r requirements.txt
```

## Troubleshooting

- **Port already in use**: Kill the process using port 8000 or use a different port
- **Module not found**: Make sure you're running from the backend directory
- **Import errors**: Check that all dependencies are installed
