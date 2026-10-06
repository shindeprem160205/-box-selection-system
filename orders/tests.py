from decimal import Decimal

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from boxes.models import Box
from products.models import Product

from .models import Order, OrderItem
from .services import (
    calculate_total_weight,
    product_fits_box,
    recommend_box,
)


class BoxRecommendationTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=Decimal("30"),
            width=Decimal("20"),
            height=Decimal("3"),
            weight=Decimal("2"),
        )

        self.small_box = Box.objects.create(
            name="Small Box",
            internal_length=Decimal("35"),
            internal_width=Decimal("25"),
            internal_height=Decimal("10"),
            max_weight=Decimal("5"),
            cost=Decimal("50"),
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            internal_length=Decimal("50"),
            internal_width=Decimal("40"),
            internal_height=Decimal("20"),
            max_weight=Decimal("10"),
            cost=Decimal("80"),
        )

        self.order = Order.objects.create()

        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )

    def test_total_weight(self):
        total_weight = calculate_total_weight(self.order)

        self.assertEqual(
            total_weight,
            Decimal("2"),
        )

    def test_product_fits_box(self):
        self.assertTrue(
            product_fits_box(
                self.product,
                self.small_box,
            )
        )

    def test_cheapest_suitable_box_is_selected(self):
        recommended_box = recommend_box(
            self.order,
            Box.objects.all(),
        )

        self.assertEqual(
            recommended_box,
            self.small_box,
        )

    def test_box_rejected_when_weight_exceeds_capacity(self):
        self.small_box.max_weight = Decimal("1")
        self.small_box.save()

        recommended_box = recommend_box(
            self.order,
            Box.objects.all(),
        )

        self.assertEqual(
            recommended_box,
            self.medium_box,
        )

    def test_box_rejected_when_dimensions_do_not_fit(self):
        self.small_box.internal_length = Decimal("20")
        self.small_box.save()

        recommended_box = recommend_box(
            self.order,
            Box.objects.filter(id=self.small_box.id),
        )

        self.assertIsNone(recommended_box)

    def test_product_fits_after_rotation(self):
        rotated_product = Product.objects.create(
            name="Rotated Product",
            length=Decimal("10"),
            width=Decimal("20"),
            height=Decimal("5"),
            weight=Decimal("1"),
        )

        rotated_box = Box.objects.create(
            name="Rotated Box",
            internal_length=Decimal("20"),
            internal_width=Decimal("5"),
            internal_height=Decimal("10"),
            max_weight=Decimal("5"),
            cost=Decimal("60"),
        )

        self.assertTrue(
            product_fits_box(
                rotated_product,
                rotated_box,
            )
        )

    def test_no_suitable_box_returns_none(self):
        self.small_box.max_weight = Decimal("1")
        self.small_box.save()

        self.medium_box.max_weight = Decimal("1")
        self.medium_box.save()

        recommended_box = recommend_box(
            self.order,
            Box.objects.all(),
        )

        self.assertIsNone(recommended_box)


class BoxRecommendationAPITests(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=Decimal("30"),
            width=Decimal("20"),
            height=Decimal("3"),
            weight=Decimal("2"),
        )

        self.small_box = Box.objects.create(
            name="Small Box",
            internal_length=Decimal("35"),
            internal_width=Decimal("25"),
            internal_height=Decimal("10"),
            max_weight=Decimal("5"),
            cost=Decimal("50"),
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            internal_length=Decimal("50"),
            internal_width=Decimal("40"),
            internal_height=Decimal("20"),
            max_weight=Decimal("10"),
            cost=Decimal("80"),
        )

        self.order = Order.objects.create()

        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )

    def test_recommend_box_api(self):
        response = self.client.post(
            f"/api/orders/{self.order.id}/recommend-box/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["order_id"],
            self.order.id,
        )

        self.assertEqual(
            response.data["recommended_box"]["name"],
            "Small Box",
        )

        self.assertEqual(
            str(response.data["recommended_box"]["cost"]),
            "50.00",
        )

    def test_recommend_box_returns_400_when_no_box_fits(self):
        self.small_box.max_weight = Decimal("1")
        self.small_box.save()

        self.medium_box.max_weight = Decimal("1")
        self.medium_box.save()

        response = self.client.post(
            f"/api/orders/{self.order.id}/recommend-box/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.assertEqual(
            response.data["detail"],
            "No suitable box found for this order.",
        )

    def test_recommend_box_returns_404_for_invalid_order(self):
        response = self.client.post(
            "/api/orders/9999/recommend-box/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )
    def test_order_rejects_zero_quantity(self):
        response = self.client.post(
            "/api/orders/",
            {
                "items": [
                    {
                        "product": self.product.id,
                        "quantity": 0,
                    }
                ]
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )