from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
