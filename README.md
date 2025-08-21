# Snapgram
A simplified Instagram-like social media platform built with Django, HTML, and CSS. Users can sign up, log in, upload posts, like/unlike content, follow/unfollow other users, search for profiles. Features include profile pages, post likes counter, comment system, and responsive design for desktop and mobile.



## Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Database: SQLite (default in Django)

Authentication: Django Auth System

Deployment: (e.g., Render/Heroku) (add this if you plan to deploy)

Others: Pillow for image uploads


## ✅ Requirements

Python 3.10+

Django 4.x

Virtual environment (recommended)

Pillow (for image handling)

SQLite (comes by default)


## Setup

### Clone the repository
git clone https://github.com/your-username/instagram-clone.git
cd instagram-clone

### Create virtual environment
python -m venv venv
source venv/bin/activate  # for Mac/Linux
venv\Scripts\activate     # for Windows

### Install dependencies
pip install -r requirements.txt

### Run migrations
python manage.py migrate

### Start server
python manage.py runserver
