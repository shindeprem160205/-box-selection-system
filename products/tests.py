from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase


class ProductAPITests(APITestCase):

    def test_product_rejects_negative_dimensions(self):
        response = self.client.post(
            "/api/products/",
            {
                "name": "Invalid Product",
                "length": -10,
                "width": 20,
                "height": 5,
                "weight": 2,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.assertIn("length", response.data)