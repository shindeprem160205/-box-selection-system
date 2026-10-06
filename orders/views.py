from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from boxes.models import Box

from .models import Order
from .serializers import OrderSerializer
from .services import recommend_box


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.prefetch_related(
        "items__product"
    )
    serializer_class = OrderSerializer


class RecommendBoxView(APIView):
    def post(self, request, order_id):
        order = get_object_or_404(
            Order.objects.prefetch_related("items__product"),
            id=order_id,
        )

        boxes = Box.objects.all()

        recommended_box = recommend_box(order, boxes)

        if recommended_box is None:
            return Response(
                {
                    "detail": "No suitable box found for this order."
                },
                status=400,
            )

        return Response(
            {
                "order_id": order.id,
                "recommended_box": {
                    "id": recommended_box.id,
                    "name": recommended_box.name,
                    "cost": recommended_box.cost,
                },
            }
        )