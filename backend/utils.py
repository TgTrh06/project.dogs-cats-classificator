import numpy as py
from PIL import Image
import io

def preprocess(image):
    img = Image.open(io.BytesIO(image)).resize((150,150))
    img = py.array(img) / 255.0
    img = py.expand_dims(img, axis=0)
    return img