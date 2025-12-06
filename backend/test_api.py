"""
Demo script to test the Dogs & Cats Classifier API
Usage: python test_api.py <path_to_image>
"""

import sys
import requests
from pathlib import Path

API_URL = "http://localhost:8000/predict"

def test_prediction(image_path):
    """Test the prediction API with an image file"""
    
    # Check if file exists
    if not Path(image_path).exists():
        print(f"❌ Error: File not found: {image_path}")
        return
    
    print(f"📤 Uploading image: {image_path}")
    
    try:
        # Open and send the image
        with open(image_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(API_URL, files=files)
        
        # Check response
        if response.status_code == 200:
            data = response.json()
            prediction = data['prediction']
            confidence = data['confidence']
            
            # Display result
            icon = '🐶' if prediction == 'dog' else '🐱'
            print(f"\n✅ Prediction successful!")
            print(f"{icon} Result: {prediction.upper()}")
            print(f"📊 Confidence: {confidence * 100:.1f}%")
            
            # Visual confidence bar
            bar_length = 50
            filled = int(bar_length * confidence)
            bar = '█' * filled + '░' * (bar_length - filled)
            print(f"[{bar}] {confidence * 100:.1f}%")
            
        else:
            print(f"❌ Error: HTTP {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to API. Is the server running?")
        print("   Run: python -m uvicorn main:app --reload")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_api.py <path_to_image>")
        print("Example: python test_api.py dog.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    test_prediction(image_path)
