import django_filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from .models import MenuCategory, MenuSubCategory
from .serializers import MenuCategorySerializer, MenuSubCategorySerializer


class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuSubCategoryFilter(django_filters.FilterSet):
    dish_name = django_filters.CharFilter(field_name='dishes__name', lookup_expr='icontains')

    class Meta:
        model = MenuSubCategory
        fields = ['dish_name', 'parent_category']


class MenuSubCategoryListView(ListAPIView):
    queryset = MenuSubCategory.objects.all()
    serializer_class = MenuSubCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuSubCategoryFilter
