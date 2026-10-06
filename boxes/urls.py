from django.urls import path

from .views import BoxListCreateView


urlpatterns = [
    path("", BoxListCreateView.as_view(), name="box-list-create"),
]