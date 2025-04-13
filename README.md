# Image Processing Application

A web-based image processing tool built with Django, offering a range of image editing features. This application allows users to upload images, editing and download image. Using AWS S3 for storage file, for local storage switch to local storage branch.

## Features

- Image Upload: Users can upload images with titles.
- Image Display: Gallery-style display of images. 
- Download: Users can download images. 
- Edit: Edit image title.
- Delete: Remove image from gallery. 
- Image Filters: Gray, Sepia,Poster, Blur, Edge, and Solar
- AWS S3: Images stored in S3
- Cloud Deployment: Can be hosted on AWS EC2. 

## Project Structure

```
Image-Processing-Application/
├── gallery/               # Main Django app
├── image_site/            # Django project config and settings
├── media/                 # Uploaded image storage
├── manage.py             
├── requirements.txt       
└── README.md              
```

## Getting Started

Follow these steps to run the project locally.

```bash
sudo dnf install python3 -y
```

### 1. Clone the Repository

```bash
git clone https://github.com/ChrisChln/Gallery.git
cd Gallery
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server(For local only)

```bash
python manage.py runserver
```

## Usage

1. Upload an image from your local device.
2. Edit it with tools like crop, rotate, or apply filters.
3. Review and manage your image history or revert changes as needed.

---

## Deploying to AWS EC2

This guide helps you run your Django project on an AWS EC2 instance (Amazon Linux 2023).

### Prerequisites

- An EC2 instance is launched and accessible.
- Python 3, pip, and Git are installed on the instance.
- Your project is already on the instance (via `git clone` or `scp`).


---

### Install Python and Set Up Virtual Environment EC2

```bash
sudo dnf install python3-pip -y
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd Gallery
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000
```

---
### AWS S3 Storage
Editing setting.py:
```
# AWS_ACCESS_KEY_ID = 'ENTER YOU OWN KEY ID'  
# AWS_SECRET_ACCESS_KEY = 'ENTER YOUR OWN ACCESS KEY'  
# AWS_STORAGE_BUCKET_NAME = 'BUCKET NAME'  
```

---

## Contributing

Pull requests are welcome. If you'd like to suggest features or report bugs, please open an issue or submit a PR.



