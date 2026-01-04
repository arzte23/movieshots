from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import MediaItem, Screenshot

User = get_user_model()


class GalleryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", email="testuser@email.com", password="password123"
        )
        cls.movie = MediaItem.objects.create(
            media_type="MOVIE", title="Test Movie", release_year=2026
        )
        cls.screenshot = Screenshot.objects.create(
            media_item=cls.movie, image="test_image.jpg"
        )

    def test_home_page_status(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_top_rated_page(self):
        response = self.client.get(reverse("top_rated"))
        self.assertEqual(response.status_code, 200)

    def test_like_functionality(self):
        self.client.login(
            username="testuser", email="testuser@email.com", password="password123"
        )
        url = reverse("toggle_favorite", args=[self.screenshot.pk])
        self.client.post(url, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        self.assertTrue(self.screenshot.favorites.filter(pk=self.user.pk).exists())
        self.client.post(url, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        self.assertFalse(self.screenshot.favorites.filter(pk=self.user.pk).exists())

    def test_anonymous_cannot_like(self):
        url = reverse("toggle_favorite", args=[self.screenshot.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.screenshot.favorites.exists())

    def test_my_collection_page(self):
        url = reverse("favorite_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.client.login(
            username="testuser", email="testuser@email.com", password="password123"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.screenshot.favorites.add(self.user)
        response = self.client.get(url)
        self.assertIn(self.screenshot, response.context["screenshots"])

    def test_my_collection_isolation(self):
        other_user = User.objects.create_user(
            username="otheruser", email="otheruser@email.com", password="password123"
        )
        other_movie = MediaItem.objects.create(
            media_type="SERIES", title="Other TV Show", release_year=1928
        )
        other_screenshot = Screenshot.objects.create(
            media_item=other_movie, image="other.jpg"
        )
        other_screenshot.favorites.add(other_user)
        self.client.login(
            username="testuser", email="testuser@email.com", password="password123"
        )
        response = self.client.get(reverse("favorite_list"))
        self.assertNotIn(other_screenshot, response.context["screenshots"])
