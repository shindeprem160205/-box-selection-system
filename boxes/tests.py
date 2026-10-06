from rest_framework import status
from rest_framework.test import APITestCase


class BoxAPITests(APITestCase):

    def test_box_rejects_negative_cost(self):
        response = self.client.post(
            "/api/boxes/",
            {
                "name": "Invalid Box",
                "internal_length": 30,
                "internal_width": 20,
                "internal_height": 10,
                "max_weight": 5,
                "cost": -50,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.assertIn("cost", response.data)