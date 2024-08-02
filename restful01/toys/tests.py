from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Toy


class ToyAPITestCase(APITestCase):

    def setUp(self):
        """
        Configuration initial for the tests
        """
        self.client = APIClient()
        self.toy1 = Toy.objects.create(
            name="Toy 1",
            description="Description 1",
            price=100,
            category="Category 1",
            was_included_in_home=False,
        )
        self.toy2 = Toy.objects.create(
            name="Toy 2",
            description="Description 2",
            price=100,
            category="Category 2",
            was_included_in_home=False,
        )
        self.toys_list_url = reverse("toy-list")
        self.toys_detail_url = lambda pk: reverse("toy-detail", args=[pk])

    def test_list_toys(self):
        """
        Testing get all toys list
        """
        response = self.client.get(self.toys_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Toy 1")
        self.assertEqual(response.data[1]["name"], "Toy 2")

    def test_create_toy(self):
        """
        Testing create a new toy
        """
        data = {
            "name": "Toy 3",
            "description": "Description 3",
            "price": 150,
            "category": "Category 3",
            "was_included_in_home": False,
        }
        response = self.client.post(self.toys_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Toy 3")
        self.assertEqual(Toy.objects.count(), 3)

    def test_create_toy_missing_fields(self):
        """
        Testing create a new toy with wrong fild
        """
        data = {
            "name": "Toy 4",
            "description": "Description 4",
            # Price is missing
            "category": "Category 4",
            "was_included_in_home": False,
        }
        response = self.client.post(self.toys_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("price", response.data)

    def test_delete_toy(self):
        """
        Testing delete a toy using url params id 
        """
        response = self.client.delete(self.toys_detail_url(self.toy1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Toy.objects.count(), 1)

    def test_delete_nonexistent_toy(self):
        """
        Testing delete a inexist toy
        """
        response = self.client.delete(self.toys_detail_url(999))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
