# Snapgram

A simplified Instagram-like social media platform built with Django, Supabase, and Cloudinary. Users can sign up, log in, upload posts, like/unlike content, follow/unfollow other users, and search for profiles. Features include:
✅ Profile pages
✅ Post likes counter
✅ Comment system
✅ Responsive design for desktop and mobile

## 🚀 Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Database: Supabase

Image Handling: Cloudinary, Pillow

Authentication: Django Auth System

Deployment: Render

## ✅ Features

User authentication (Sign Up / Login / Logout)

Upload and display posts with images

Like/Unlike functionality

Follow/Unfollow users

Comment system

Search users

Responsive UI

## ⚙️ Requirements

Python 3.10+

Django 4.x

Virtual environment (recommended)

Supabase account (for PostgreSQL DB)

Cloudinary account (for image storage)

Pillow (for image handling)

## 📦 Setup
1. Clone the repository
git clone https://github.com/Coderxplus/snapgram.git
cd snapgram

2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables

Create a .env file and set:

SECRET_KEY=your_django_secret_key
DEBUG=False
ALLOWED_HOSTS=your_render_url,localhost
DATABASE_URL=your_supabase_database_url
CLOUDINARY_URL=your_cloudinary_url

5. Apply migrations
python manage.py migrate

6. Run the development server
python manage.py runserver

🌐 Deployment

This project is deployed on Render.
Live Demo: https://snapgram-4xft.onrender.com/

📷 Screenshots



⭐ Contribute

Feel free to fork, improve, and submit a pull request!