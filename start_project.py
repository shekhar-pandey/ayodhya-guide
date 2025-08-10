#!/usr/bin/env python3
"""
Main startup script for Ayodhya Guide project
This script will start the backend server and optionally serve the frontend
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if required Python packages are installed"""
    try:
        import fastapi
        import uvicorn
        print("✅ Dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies first:")
        print("cd backend && pip install -r requirements.txt")
        return False

def start_backend():
    """Start the backend server"""
    print("🚀 Starting Ayodhya Guide Backend Server...")
    
    backend_dir = Path(__file__).parent / "backend"
    if not backend_dir.exists():
        print("❌ Backend directory not found!")
        return False
    
    try:
        # Change to backend directory and start server
        os.chdir(backend_dir)
        print(f"📁 Working directory: {os.getcwd()}")
        
        # Start the server using the startup script
        if Path("start_server.py").exists():
            print("🎯 Using startup script...")
            subprocess.Popen([sys.executable, "start_server.py"])
        else:
            print("🎯 Using uvicorn directly...")
            subprocess.Popen([
                sys.executable, "-m", "uvicorn", 
                "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"
            ])
        
        print("⏳ Waiting for server to start...")
        time.sleep(3)
        
        # Test if server is running
        try:
            import requests
            response = requests.get("http://localhost:8000/", timeout=5)
            if response.status_code == 200:
                print("✅ Backend server is running at http://localhost:8000")
                return True
            else:
                print("❌ Backend server responded with error")
                return False
        except ImportError:
            print("⚠️  requests module not available, skipping server check")
            print("✅ Backend server should be running at http://localhost:8000")
            return True
        except Exception as e:
            print(f"❌ Backend server check failed: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        return False

def start_frontend_server():
    """Start a simple HTTP server for the frontend"""
    print("🌐 Starting frontend server...")
    
    try:
        # Go back to project root
        os.chdir(Path(__file__).parent)
        
        # Start HTTP server
        subprocess.Popen([
            sys.executable, "-m", "http.server", "8080"
        ])
        
        print("✅ Frontend server running at http://localhost:8080")
        return True
    except Exception as e:
        print(f"❌ Failed to start frontend server: {e}")
        return False

def main():
    """Main function"""
    print("🏛️  Ayodhya Guide - Project Startup")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Start backend
    if not start_backend():
        print("❌ Failed to start backend server")
        return
    
    # Ask user if they want to start frontend server
    print("\n" + "=" * 50)
    print("Frontend Options:")
    print("1. Open HTML files directly in browser (recommended)")
    print("2. Start local HTTP server")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "2":
        if start_frontend_server():
            print("\n🎉 Project is ready!")
            print("📱 Backend API: http://localhost:8000")
            print("🌐 Frontend: http://localhost:8080")
            print("📝 Test Contact Form: http://localhost:8080/test-contact-local.html")
            
            # Ask if user wants to open browser
            open_browser = input("\nOpen test page in browser? (y/n): ").strip().lower()
            if open_browser in ['y', 'yes']:
                webbrowser.open("http://localhost:8080/test-contact-local.html")
        else:
            print("❌ Failed to start frontend server")
    else:
        print("\n🎉 Backend is ready!")
        print("📱 Backend API: http://localhost:8000")
        print("📝 Test Contact Form: Open test-contact-local.html in your browser")
        print("🏠 Main Website: Open index.html in your browser")
    
    print("\n" + "=" * 50)
    print("💡 Tips:")
    print("- Keep this terminal open to keep the backend running")
    print("- Use Ctrl+C to stop the servers")
    print("- Check CONTACT_FORM_SETUP.md for detailed instructions")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Servers stopped.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check the error and try again.")
