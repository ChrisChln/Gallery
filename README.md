# Image Processing Application

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.1-brightgreen)](https://www.djangoproject.com/)
[![Pillow](https://img.shields.io/badge/Pillow-9.4.0-red)](https://python-pillow.org/)

A cloud-ready web application for real-time image processing with AWS deployment capabilities.

## Key Features
- Upload local images (JPG/PNG, ≤5MB)
- Apply various filters in real-time:
  - Grayscale Conversion
  - Sepia Tone
  - Gaussian Blur
  - Edge Detection
  - Posterization 
  - Solarization
- Cloud storage integration (AWS S3)
- Responsive web interface
- Secure file validation

## Tech Stack
**Frontend**: HTML5/CSS3/JavaScript  
**Backend**: Django 4.1 (Python)  
**Image Processing**: Pillow 9.4+  
**Cloud Infrastructure**: 
- AWS EC2 (Ubuntu 22.04)
- AWS S3 Storage
- Nginx + Gunicorn

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- virtualenv

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/Image-Processing-Application.git
cd Image-Processing-Application

# Create virtual environment
python3 -m virtualenv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Database setup
python manage.py migrate

# Run development server
python manage.py runserver
```