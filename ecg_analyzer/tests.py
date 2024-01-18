from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import ECG, Lead, UserProfile


class ECGAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.ecg = ECG.objects.create(owner=self.user)
        self.lead = Lead.objects.create(
            ecg=self.ecg,
            name="I",
            number_of_samples=100,
            signal=[ 0, -1, 1, -2, 2, 0, 1, -1, 2, -2, ],
        )
        self.client.login(username="testuser", password="testpassword")

    def test_get_ecg_list(self):
        url = "/ecgs/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_ecg(self):
        url = "/ecgs/"
        data = {
            "date": "2024-01-18",
            "leads": [
                {
                    "name": "I",
                    "number_of_samples": 100,
                    "signal": [0, -1, 1, -2, 2, 0, 1, -1, 2, -2],
                },
                {
                    "name": "II",
                    "number_of_samples": 100,
                    "signal": [1, 0, -1, 2, -2, 1, 0, -1, 2, -2],
                },
            ],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ECGAuthorizationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="password")
        self.other_user = User.objects.create_user(
            username="other_user", password="password"
        )
        UserProfile.objects.create(user=self.user, is_admin=True)
        UserProfile.objects.create(user=self.other_user, is_admin=False)
        self.ecg = ECG.objects.create(owner=self.user)
        self.lead = Lead.objects.create(
            ecg=self.ecg,
            name="I",
            number_of_samples=100,
            signal=[ 0, -1, 1, -2, 2, 0, 1, -1, 2, -2, ],
        )

    def test_user_can_access_own_ecg(self):
        self.client.login(username="user", password="password")
        url = f"/ecgs/{self.ecg.pk}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_access_other_user_ecg(self):
        self.client.login(username="other_user", password="password")
        url = f"/ecgs/{self.ecg.pk}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
