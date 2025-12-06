# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     text: str
#     is_done: bool = False

# # In-memory storage for items
# items = []

# @app.get("/")
# def root():
#     return {"Hello": "World"}

# @app.post("/items")
# def create_item(item: Item):
#     items.append(item)
#     return items

# @app.get("/items", response_model=list[Item])
# def list_items(limit: int = 2):
#     return items[:limit]

# @app.get("/items/{item_id}", response_model=Item)
# def get_item(item_id: int):
#     if item_id < len(items):
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


MODEL_PATH = "./models/dogs_cats_trained_model.keras"

print("🔄 Loading model...")
model = load_model(MODEL_PATH)
print("✅ Model loaded successfully!")

# Preprocessing function
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((128, 128))  # đúng input của model
    img = np.array(img).astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)  # thêm chiều batch
    return img

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read image bytes
    image_bytes = await file.read()

    # Preprocess
    img = preprocess_image(image_bytes)

    # Predict
    pred = model.predict(img)[0][0]

    result = "dog" if pred < 0.5 else "cat"
    confidence = float(pred if pred < 0.5 else (1 - pred))

    return {
        "prediction": result,
        "confidence": confidence
    }
