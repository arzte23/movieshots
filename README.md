# 🎬 MovieShots

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.16-red?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon_Tech-336791?style=for-the-badge&logo=postgresql)

**MovieShots** is a visual discovery platform for movie and TV show enthusiasts. Unlike traditional databases that rely on text descriptions, MovieShots allows users to find content based on "vibes", aesthetics, and specific visual themes.

Want to watch something with a "Christmas" atmosphere? Search for the tag, browse through atmospheric screenshots, and if an image catches your eye — click "View Movie" to discover the source and start watching.

---

## 🚀 Live Demo & API

- **Live Site:** [https://movieshots.onrender.com](https://movieshots.onrender.com)
- **API Documentation (Swagger):** [https://movieshots.onrender.com/api/schema/swagger-ui/](https://movieshots.onrender.com/api/schema/swagger-ui/)

---

## ✨ Key Features

### 🔍 Visual Discovery
- **Tag-Based Search:** Find movies by visual themes (e.g., "Christmas", "Neon", "Rain").
- **Smart Filtering:** Filter by Movies, TV Shows, or browse the "Top Rated" feed.
- **Detailed Info:** View full movie metadata and all associated screenshots on a single page.

### 👤 User Experience
- **Personal Collection:** Like screenshots to add them to your private "My Collection" page.
- **Instant Interactions:** AJAX-based "Like" system works without page reloads.
- **Authentication:** Secure signup via Email/Username or **Google OAuth** (Social Login).
- **UI/UX:** Responsive design with **Dark/Light mode** toggle and image lightbox gallery.

### ⚙️ REST API
- **Fully Documented:** Interactive Swagger/OpenAPI documentation (`drf-spectacular`).
- **Advanced Search:** Filter via API by tags, title, description, and media type.
- **Secure:** JWT (JSON Web Token) authentication for external clients.

---

## 🛠 Tech Stack

### Backend
- **Framework:** Python, Django 5.2
- **API:** Django REST Framework (DRF)
- **Authentication:** `django-allauth` (OAuth2), `dj-rest-auth`, `SimpleJWT`
- **Database:** PostgreSQL (hosted on Neon Tech)
- **Search & Filtering:** `django-filter`, `django-taggit`

### Infrastructure & Media
- **Deployment:** Render (PaaS)
- **Web Server:** Gunicorn + Whitenoise (for static files)
- **Media Storage:** Cloudinary (optimized image delivery)

### Tools & Quality
- **Linting:** Ruff
- **Testing:** `unittest` (Standard Django testing suite)
- **Documentation:** OpenAPI 3.0 (`drf-spectacular`)

---

## 🔌 API Endpoints

The project exposes a robust REST API. Below are a few key endpoints:

- `GET /api/v1/screenshots/` - Get a list of screenshots (supports filtering by tags, ordering by date/likes).
- `GET /api/v1/items/<slug>/` - Get detailed movie info with nested screenshots.
- `POST /api/v1/screenshots/<id>/like/` - Like/Unlike a screenshot.
- `POST /api/v1/auth/login/` - Obtain JWT Access/Refresh tokens.

*Check the [Swagger UI](https://movieshots.onrender.com/api/docs/) for the full interactive documentation.*

---

## 💻 Local Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arzte23/movieshots.git
   cd movieshots
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables: Create a .env file in the root directory and add the following:**
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_local_or_neon_db_url
   CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
   CLOUDINARY_API_KEY=your_cloudinary_api_key
   CLOUDINARY_API_SECRET=your_cloudinary_api_secret
   # Optional (for Google Auth)
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_SECRET=your_google_secret
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server:**
   ```bash
   python manage.py runserver
   ```

---

## 🧪 Running Tests
The project includes unit tests for both the Django Templates (Views) and the API endpoints.
```bash
# Run all tests
python manage.py test

# Run specific API tests
python manage.py test api
```

## 👨‍💻 Author
Developed by [**arzte23**](https://github.com/arzte23).

If you find this project interesting, please give it a ⭐️ on GitHub!