# 🐶🐱 Dogs & Cats Classifier - Hướng Dẫn Sử Dụng

## Giới thiệu
Ứng dụng web phân loại hình ảnh chó và mèo sử dụng Machine Learning với FastAPI backend và HTML frontend.

## Cài đặt

### 1. Cài đặt dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Chạy server
```bash
uvicorn main:app --reload
```

Server sẽ chạy tại: `http://localhost:8000`

## Sử dụng

### Cách 1: Truy cập giao diện web
1. Mở trình duyệt và truy cập: `http://localhost:8000/static/index.html`
2. Click vào vùng upload hoặc kéo thả ảnh vào
3. Click nút "🔮 Phân Tích Hình Ảnh"
4. Xem kết quả phân loại và độ tin cậy

### Cách 2: Sử dụng API trực tiếp
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/your/image.jpg"
```

## API Endpoints

### POST /predict
Phân loại hình ảnh chó hoặc mèo

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (image file)

**Response:**
```json
{
  "prediction": "dog",  // hoặc "cat"
  "confidence": 0.95    // độ tin cậy từ 0-1
}
```

## Tính năng

✨ **Giao diện đẹp mắt với Nature Theme:**
- Thiết kế hiện đại với màu xanh lá tự nhiên
- Light & Dark mode với toggle button
- Responsive trên mọi thiết bị
- Glassmorphism effect với backdrop blur
- Smooth animations và transitions
- External CSS với CSS Variables

🚀 **Chức năng:**
- Upload ảnh bằng click hoặc drag & drop
- Preview ảnh trước khi phân tích
- Hiển thị kết quả với độ tin cậy
- Progress bar trực quan với gradient
- Xử lý lỗi thân thiện
- Theme persistence với localStorage

🔧 **Kỹ thuật:**
- FastAPI backend với CORS enabled
- TensorFlow/Keras model
- Async file handling
- RESTful API design
- Nature theme với Montserrat font
- CSS custom properties (variables)

## Cấu trúc thư mục
```
backend/
├── main.py                          # FastAPI application
├── requirements.txt                 # Python dependencies
├── models/
│   └── dogs_cats_trained_model.keras  # Trained model
├── static/
│   ├── index.html                   # Frontend interface
│   └── styles.css                   # Nature theme CSS
└── notebook/
    └── output/
        ├── training_history.pkl
        └── model.weights.h5
```

## Troubleshooting

### Lỗi: Module not found
```bash
pip install -r requirements.txt
```

### Lỗi: CORS
Đảm bảo CORS middleware đã được cấu hình trong `main.py`

### Lỗi: Model not found
Kiểm tra đường dẫn model trong `main.py` (MODEL_PATH)

## Yêu cầu hệ thống
- Python 3.8+
- TensorFlow 2.x
- FastAPI
- Uvicorn

## License
MIT License