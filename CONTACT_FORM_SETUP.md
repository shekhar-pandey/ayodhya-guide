# Contact Form Setup Guide

## Problem Fixed
The contact forms in your Ayodhya Guide application were failing because they were configured to use Formspree with an incorrect endpoint format.

## Solution Implemented
I've replaced the Formspree implementation with a custom backend solution that handles contact form submissions locally.

## Files Modified
1. **`contact.html`** - Updated contact form to use local backend
2. **`index.html`** - Updated homepage contact form to use local backend  
3. **`backend/app/main.py`** - Enhanced contact endpoint with subject field support
4. **`test-contact-local.html`** - Test page for local development

## How to Use

### 1. Start the Backend Server
```bash
cd ayodhya-guide/backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 2. Test the Contact Form
- Open `test-contact-local.html` in your browser
- Fill out the form and submit
- Check the backend console for form submission logs

### 3. Use in Production
The contact forms in `contact.html` and `index.html` now work with your local backend.

## Backend Endpoint
- **URL:** `POST /api/contact`
- **Request Body:**
  ```json
  {
    "name": "User Name",
    "email": "user@example.com", 
    "subject": "Optional Subject",
    "message": "User message"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Thank you for your message! We'll get back to you soon.",
    "status": "success",
    "data": { ... }
  }
  ```

## Features
- ✅ Form validation
- ✅ Loading states
- ✅ Success/error messages
- ✅ Subject field support
- ✅ CORS enabled for local development
- ✅ Proper error handling

## Next Steps
1. **Email Integration:** Add actual email sending functionality to the backend
2. **Database Storage:** Store contact form submissions in a database
3. **Admin Panel:** Create an admin interface to view submissions
4. **Spam Protection:** Add CAPTCHA or other anti-spam measures

## Troubleshooting
- **Backend won't start:** Check if port 8000 is available
- **CORS errors:** Ensure the backend is running and accessible
- **Form not submitting:** Check browser console for JavaScript errors
- **Backend errors:** Check the terminal where uvicorn is running

## Production Deployment
For production deployment, you'll need to:
1. Set up proper email services (SendGrid, AWS SES, etc.)
2. Configure environment variables for API keys
3. Set up proper CORS origins
4. Add rate limiting and security measures
