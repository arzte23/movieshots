from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from gallery.models import MediaItem, Screenshot

User = get_user_model()


class MovieShotsAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", email="testuser@email.com", password="password123"
        )
        cls.other_user = User.objects.create_user(
            username="otheruser", email="otheruser@email.com", password="password123"
        )
        cls.movie = MediaItem.objects.create(
            media_type="MOVIE",
            title="Test Movie",
            release_year=2026,
        )
        cls.screenshot1 = Screenshot.objects.create(
            media_item=cls.movie,
            image="image1.jpg",
        )
        cls.screenshot2 = Screenshot.objects.create(
            media_item=cls.movie,
            image="image2.jpg",
        )
        cls.screenshot1.favorites.add(cls.user)
        cls.screenshot2.favorites.add(cls.other_user)
        cls.list_url = reverse("screenshot_list")
        cls.detail_url = reverse("media_item_detail", args=[cls.movie.slug])
        cls.like_url = reverse("screenshot_like", args=[cls.screenshot1.pk])

    def test_get_screenshot_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_get_movie_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Movie")
        self.assertTrue("screenshots" in response.data)

    def test_like_unauthenticated(self):
        response = self.client.post(self.like_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_like_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.like_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "unliked")
        response = self.client.post(self.like_url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], "liked")

    def test_top_rated_sorting(self):
        self.screenshot1.favorites.add(self.other_user)
        response = self.client.get(self.list_url, {"ordering": "-likes_count"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data["results"] if "results" in response.data else response.data
        self.assertEqual(data[0]["id"], str(self.screenshot1.id))
        self.assertEqual(data[1]["id"], str(self.screenshot2.id))

    def test_my_collection_isolation_api(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url, {"is_favorited": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data["results"] if "results" in response.data else response.data
        returned_ids = [item["id"] for item in data]
        self.assertIn(str(self.screenshot1.id), returned_ids)
        self.assertNotIn(str(self.screenshot2.id), returned_ids)
