# 🎬 MovieShots

**MovieShots** is a web application for collecting and sharing aesthetic high-resolution movie screenshots. It allows users to browse movies, view detailed shots, and curate their own personal collection of favorites.

The project demonstrates a full-stack development workflow using **Django**, **PostgreSQL**, and **Cloudinary**.

🚀 **Live Demo:** https://movieshots.onrender.com/

---

## ✨ Features

* **Movie Gallery:** Browse movies and view associated high-quality screenshots.
* **Lightbox Viewer:** Full-screen image viewing experience using Fancybox.
* **User Authentication:** Secure signup, login, and logout functionality (powered by `django-allauth`).
* **Interactive UI:** * **AJAX Likes:** Add screenshots to favorites instantly without page reloads.
    * Dynamic buttons that update state in real-time.
* **Personal Collection:** A dedicated "My Collection" page for managing saved screenshots.
* **Responsive Design:** Fully optimized for desktop and mobile devices using Bootstrap 5.
* **Cloud Storage:** Images are optimized and served via Cloudinary CDN.

---

## 🛠️ Tech Stack

### Backend
* **Python 3.12.3**
* **Django 6.0**
* **PostgreSQL** (Neon Tech) - Production database.
* **Whitenoise** - Static file serving.

### Frontend
* **HTML5 / CSS3**
* **Bootstrap 5** - Styling and layout.
* **JavaScript (Vanilla)** - AJAX logic for likes.
* **Fancybox UI** - Image lightbox.

### Tools & Services
* **Cloudinary** - Media management and storage.
* **Render** - Cloud hosting and deployment.
* **Git & GitHub** - Version control.

---

## ⚙️ Local Installation

If you want to run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/arzte23/movieshots.git
    cd movieshots
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add the following keys:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=your_local_or_neon_db_url
    CLOUDINARY_CLOUD_NAME=your_cloud_name
    CLOUDINARY_API_KEY=your_api_key
    CLOUDINARY_API_SECRET=your_api_secret
    ```

5.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (optional):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the server:**
    ```bash
    python manage.py runserver
    ```

---

## 🗺️ Roadmap

Future improvements planned for this project:
* [ ] Add REST API via Django REST Framework.
* [ ] Filtering screenshots by tags/colors.
* [ ] Social login (Google/GitHub).
* [ ] Dark Mode toggle.

---

## 👤 Author

Developed by **arzte23**.

Feel free to reach out or contribute!