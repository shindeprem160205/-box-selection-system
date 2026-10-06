from rest_framework import generics

from .models import Box
from .serializers import BoxSerializer


class BoxListCreateView(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer