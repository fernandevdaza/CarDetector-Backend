# CarDetector Backend

Backend API for car detection and identification using AI-powered image analysis. This application analyzes images to detect and identify vehicle information including brand, model, and year.

## Features

- 🚗 **Car Detection**: AI-powered car identification from images using Google Gemini
- 📍 **Geolocation**: Extract and store GPS coordinates from image metadata
- 🔐 **Authentication**: JWT-based user authentication and authorization
- 👤 **User Management**: Complete user CRUD operations with role-based access
- 🗄️ **Database**: SQLAlchemy ORM with SQLite for data persistence
- 📝 **Metadata Processing**: Extract EXIF data from images including HEIC format support

## Technology Stack

- **Framework**: FastAPI
- **AI Model**: Google Gemini 2.5 Flash (via LangChain)
- **Database**: SQLAlchemy with SQLite
- **Authentication**: JWT tokens with passlib and python-jose
- **Image Processing**: Pillow, pillow-heif, piexif
- **Package Manager**: Poetry
- **Python**: >= 3.12

## Installation

### Prerequisites

- Python 3.12 or higher
- Poetry (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/fernandevdaza/CarDetector-Backend.git
cd CarDetector-Backend
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Create a `.env` file in the root directory with the following variables:
```env
# Google Gemini API
GOOGLE_API_KEY=your_google_api_key_here

# JWT Configuration
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256

# Database (optional, defaults to SQLite)
DATABASE_URL=sqlite:///./app.db
```

4. Run the application:
```bash
poetry run uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication (`/auth`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/` | Create a new user |
| POST | `/auth/token` | Login and get access token |
| POST | `/auth/refresh` | Refresh access token |
| PUT | `/auth/me` | Update current user profile |
| DELETE | `/auth/me` | Delete current user account |

### Car Detection (`/inference`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/inference/car-with-image` | Detect and identify car from image |

**Request Parameters**:
- `file` (required): Image file (JPG, PNG, HEIC, etc.)
- `lat` (optional): Latitude coordinate
- `lon` (optional): Longitude coordinate
- `source_video_id` (optional): Source video identifier

**Response**:
```json
{
  "message": {
    "brand": "Toyota",
    "model_name": "Corolla",
    "year": 2020,
    "lat": 40.7128,
    "lng": -74.0060
  },
  "metadata": {
    "lat": 40.7128,
    "lon": -74.0060,
    "video_lat": 40.7128,
    "video_lon": -74.0060,
    "source_video_id": "video_123"
  }
}
```

### Car Data (`/car`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/car/get_cars` | Get all detected cars |

## Usage Examples

### Detect Car from Image

```python
import requests

url = "http://localhost:8000/inference/car-with-image"
files = {"file": open("car_image.jpg", "rb")}
data = {
    "lat": 40.7128,
    "lon": -74.0060
}

response = requests.post(url, files=files, data=data)
print(response.json())
```

### User Authentication

```python
import requests

# Create user
url = "http://localhost:8000/auth/"
user_data = {
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "securepassword",
    "role": "user"
}

response = requests.post(url, json=user_data)

# Login
url = "http://localhost:8000/auth/token"
login_data = {
    "username": "user@example.com",
    "password": "securepassword"
}

response = requests.post(url, data=login_data)
token = response.json()["access_token"]
```

## Project Structure

```
CarDetector-Backend/
├── app/
│   ├── controllers/          # Business logic controllers
│   │   ├── infer_with_image_controller.py
│   │   └── yolo_model_controller.py
│   ├── core/                 # Core functionality
│   │   ├── agent.py          # AI agent configuration
│   │   ├── db.py             # Database configuration
│   │   └── state.py          # Application state
│   ├── models/               # Data models
│   │   ├── db/               # Database models
│   │   │   └── models.py
│   │   ├── DetectResponse.py
│   │   └── InferenceResponseFormat.py
│   ├── prompts/              # AI prompts
│   │   └── car_detector.py
│   ├── routers/              # API routes
│   │   ├── auth.py           # Authentication endpoints
│   │   ├── car.py            # Car data endpoints
│   │   └── inference.py      # Inference endpoints
│   └── utils/                # Utility functions
│       ├── metadata_processing.py
│       └── video_processing.py
├── main.py                   # Application entry point
├── pyproject.toml            # Poetry dependencies
└── README.md                 # This file
```

## Database Models

### Cars
- `id`: Primary key
- `brand`: Car brand (e.g., "Toyota")
- `model_name`: Car model (e.g., "Corolla")
- `year`: Manufacturing year
- `lat`: Latitude coordinate
- `lng`: Longitude coordinate

### Users
- `id`: Primary key
- `email`: User email (unique)
- `first_name`: User's first name
- `last_name`: User's last name
- `hashed_password`: Encrypted password
- `is_active`: Account status
- `role`: User role

## Development

### Running in Development Mode

```bash
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Environment Variables

Make sure to set up the following environment variables in your `.env` file:

- `GOOGLE_API_KEY`: Your Google Gemini API key (required for AI inference)
- `SECRET_KEY`: Secret key for JWT token generation
- `ALGORITHM`: Algorithm for JWT encoding (e.g., HS256)

## License

This project is maintained by Fernando Daza. All rights reserved.

## Author

**Fernando Daza**  
Email: fernando.daza.18@outlook.com

## Support

For questions or issues, please open an issue in the GitHub repository.
