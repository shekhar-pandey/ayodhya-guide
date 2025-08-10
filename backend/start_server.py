#!/usr/bin/env python3
"""
Simple startup script for the Ayodhya Guide backend server
Run this from the backend directory: python start_server.py
"""

import uvicorn
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("Starting Ayodhya Guide Backend Server...")
    print("Server will be available at: http://localhost:8000")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
