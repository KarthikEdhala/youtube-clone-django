# YouTube Clone

A full-featured YouTube clone built with **Django 6** and **ImageKit** for video hosting. Users can register, upload videos, stream with adaptive HLS playback, like/dislike, and browse channels — all wrapped in a clean, responsive UI.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-green?logo=django&logoColor=white)
![ImageKit](https://img.shields.io/badge/ImageKit-Video%20CDN-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite3-lightgrey?logo=sqlite)

---

## Features

- **User Authentication** — Register, login, and logout using Django's built-in auth system
- **Video Upload** — Upload videos with optional custom thumbnails
- **HLS Streaming** — Adaptive bitrate video playback via ImageKit (240p to 1080p)
- **Like / Dislike** — Toggle-based voting system per video
- **Channel Pages** — View all videos uploaded by a specific user
- **Auto Thumbnails** — Automatically generated thumbnails with username watermarks
- **Video Management** — Delete your own videos (removes from ImageKit + database)
- **Responsive Design** — Clean CSS-based UI that works on desktop and mobile

---

## Tech Stack

| Layer       | Technology                          |
|-------------|-------------------------------------|
| Backend     | Python 3.12, Django 6.0             |
| Database    | SQLite3                             |
| Video CDN   | [ImageKit.io](https://imagekit.io/) |
| Frontend    | Django Templates, CSS, hls.js       |
| Auth        | Django built-in authentication      |

---

## Project Structure

```
Youtube-Clone/
├── requirements.txt
├── README.md
└── youtube/                     # Django project root
    ├── manage.py
    ├── .env                     # Environment variables (you create this)
    ├── db.sqlite3               # SQLite database (auto-created)
    ├── youtube/                  # Project configuration
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── accounts/                 # Authentication app
    │   ├── views.py
    │   ├── forms.py
    │   ├── urls.py
    │   └── templates/accounts/
    │       ├── login.html
    │       ├── register.html
    │       └── logged_out.html
    ├── videos/                   # Core video app
    │   ├── models.py
    │   ├── views.py
    │   ├── forms.py
    │   ├── urls.py
    │   ├── admin.py
    │   ├── imagekit_client.py
    │   └── templates/videos/
    │       ├── list.html
    │       ├── detail.html
    │       ├── upload.html
    │       └── channel.html
    ├── templates/
    │   └── base.html             # Base layout with navbar
    └── static/
        └── css/                  # Stylesheets
            ├── variables.css
            ├── base.css
            ├── navbar.css
            ├── messages.css
            ├── buttons.css
            ├── forms.css
            ├── auth.css
            ├── videos.css
            ├── videoplayer.css
            └── upload.css
```

---

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.12+** — [Download Python](https://www.python.org/downloads/)
- **pip** — Comes bundled with Python
- **Git** — [Download Git](https://git-scm.com/downloads)
- **ImageKit Account** — [Sign up for free](https://imagekit.io/registration)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Youtube-Clone.git
cd Youtube-Clone
```

### 2. Create a Virtual Environment

```bash
# macOS / Linux
python3 -m venv env
source env/bin/activate

# Windows
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file inside the `youtube/` directory:

```bash
touch youtube/.env
```

Add the following keys (get these from your [ImageKit dashboard](https://imagekit.io/dashboard)):

```env
IMAGEKIT_PUBLIC_KEY=your_imagekit_public_key
IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key
```

### 5. Run Database Migrations

```bash
cd youtube
python manage.py migrate
```

### 6. Create a Superuser (Optional)

This gives you access to the Django admin panel at `/admin/`.

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and go to **http://127.0.0.1:8000/**

---

## Usage

| Action          | How                                                       |
|-----------------|-----------------------------------------------------------|
| Register        | Click **Sign Up** in the navbar                           |
| Login           | Click **Sign In** in the navbar                           |
| Upload a video  | Login, then click **Upload** in the navbar                |
| Watch a video   | Click any video thumbnail on the homepage                 |
| Like / Dislike  | Click the thumbs up or thumbs down on the video page      |
| View a channel  | Click a username to see all their uploaded videos         |
| Delete a video  | On the video page, the owner sees a **Delete** button     |
| Admin panel     | Go to `/admin/` and login with your superuser credentials |

---

## ImageKit Setup

This project uses [ImageKit.io](https://imagekit.io/) as the video CDN for uploading, storing, streaming, and generating thumbnails.

1. Create a free account at [imagekit.io](https://imagekit.io/registration)
2. Go to your **Dashboard** > **Developer Options**
3. Copy your **Public Key** and **Private Key**
4. Paste them into your `youtube/.env` file

ImageKit handles:
- Video file storage
- Adaptive HLS streaming (240p–1080p)
- Auto-generated video thumbnails
- On-the-fly image watermarking with usernames
- Optimized video delivery via CDN

---

## API Endpoints

| Method | URL                          | Auth Required | Description            |
|--------|------------------------------|---------------|------------------------|
| GET    | `/`                          | No            | Homepage (video list)  |
| GET    | `/<id>/`                     | No            | Video detail page      |
| GET    | `/channel/<username>/`       | No            | Channel page           |
| GET    | `/upload/`                   | Yes           | Upload form            |
| POST   | `/upload/submit/`            | Yes           | Submit video upload    |
| POST   | `/<id>/delete/`              | Yes           | Delete a video         |
| POST   | `/<id>/vote/`                | Yes           | Like or dislike        |
| GET    | `/accounts/login/`           | No            | Login page             |
| GET    | `/accounts/register/`        | No            | Registration page      |
| POST   | `/accounts/logout/`          | Yes           | Logout                 |

---

## Troubleshooting

| Problem                          | Solution                                                                 |
|----------------------------------|--------------------------------------------------------------------------|
| `ModuleNotFoundError: dotenv`    | Run `pip install python-dotenv`                                          |
| `ModuleNotFoundError: imagekitio`| Run `pip install imagekitio`                                             |
| Videos not uploading             | Check your `.env` file — make sure both ImageKit keys are correct        |
| Thumbnails not showing           | Ensure the video was uploaded to ImageKit successfully                    |
| `OperationalError: no such table`| Run `python manage.py migrate`                                           |
| Port already in use              | Run `python manage.py runserver 8080` to use a different port            |
| Static files not loading         | Make sure you're running from the `youtube/` directory                   |

---

## License

This project is open source and available under the [MIT License](LICENSE).
