from django.urls import path

from .views import OrderListCreateView, RecommendBoxView


urlpatterns = [
    path(
        "",
        OrderListCreateView.as_view(),
        name="order-list-create",
    ),
    path(
        "<int:order_id>/recommend-box/",
        RecommendBoxView.as_view(),
        name="recommend-box",
    ),
]