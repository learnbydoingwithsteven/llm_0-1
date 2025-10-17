"""
Launch the 100 LLM Courses Catalog
Simple HTTP server with automatic browser opening
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve the catalog"""
    
    def log_message(self, format, *args):
        """Custom logging"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def open_browser():
    """Open browser after short delay"""
    time.sleep(1.5)
    url = f'http://localhost:{PORT}'
    print(f"\n🌐 Opening browser at {url}")
    webbrowser.open(url)

def start_server():
    """Start the HTTP server"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    handler = CustomHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("=" * 70)
        print("🎓 100 LLM COURSES: ZERO TO HERO")
        print("=" * 70)
        print(f"\n✅ Server running at http://localhost:{PORT}")
        print(f"📂 Serving from: {os.getcwd()}")
        print("\n💡 Tips:")
        print("   - Double-click course cards to mark as completed")
        print("   - Use Ctrl/Cmd + K to search courses")
        print("   - Press Ctrl+C to stop the server")
        print("\n" + "=" * 70)
        
        # Open browser in background thread
        threading.Thread(target=open_browser, daemon=True).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down server...")
            print("Thanks for learning! Keep building! 🚀\n")

if __name__ == '__main__':
    start_server()
