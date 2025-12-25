# 🎬 MovieShots

**Find your next movie through the power of cinematography.**

MovieShots is a visual-first movie discovery platform built with Django. Unlike traditional movie databases that focus on text descriptions, MovieShots allows users to search by **visual atmosphere, mood, and themes** (e.g., "Christmas", "Neon", "Noir").

[**🔴 Live Demo**](https://movieshots.onrender.com) ---

## 💡 The Idea

Sometimes you don't want to read a plot summary. You want a specific **vibe**.
1.  **Search:** A user wants to watch a Christmas movie. They search for `"Christmas"`.
2.  **Explore:** Instead of a list of titles, they see a gallery of atmospheric screenshots from various films tagged with "Christmas".
3.  **Choose:** The user spots a visual style they like.
4.  **Decide:** They click the screenshot, view the movie details and other shots from the same film, and decide to watch it.

## ✨ Key Features

* **Visual Search Engine:** Advanced search using Django `Q` objects to filter by Tags or Movie Titles.
* **Gallery & Lightbox:** High-quality image grid with **Fancybox** integration for zooming, sliding, and downloading screenshots.
* **Smart Navigation:** Pagination for large search results and organized browsing.
* **Movie Details:** Dedicated pages for each movie/series with a collection of related screenshots.
* **Download:** Direct download button for high-res screenshots.
* **Responsive Design:** Fully adaptive UI built with **Bootstrap 5**.

## 🛠️ Tech Stack

* **Backend:** Python 3.12.3, Django 6.0
* **Database:** PostgreSQL (Production), SQLite (Local)
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
* **Deployment:** Render (Gunicorn, Whitenoise)
* **Utilities:** `django-taggit` (for tagging), `Pillow` (image processing)

---

## 📸 Screenshots

### 1. Home & Search
![Home Page](https://imgur.com/wrGvETI)

### 2. Search Results ("Christmas")
![Search Results](https://imgur.com/XsRiJuv)

### 3. Movie Detail View
![Movie Detail](https://imgur.com/6rGt89u)

---

## 🚀 Local Installation

If you want to run this project locally:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/arzte23/movieshots](https://github.com/arzte23/movieshots)
    cd movieshots
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**
    Create a `.env` file in the root directory:
    ```env
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL=sqlite:///db.sqlite3
    ```

5.  **Run migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (for Admin Panel)**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the server**
    ```bash
    python manage.py runserver
    ```

Access the app at `http://127.0.0.1:8000/`.

---

## 👤 Author

Developed by **[arzte23]**.

---

*Note: This project is deployed on Render using the free tier, so the first load might take up to 50 seconds due to "spin-down" mode.*