import django_filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from .models import MenuCategory, MenuSubCategory, Dish
from .serializers import MenuCategorySerializer, MenuSubCategorySerializer, DishSerializer


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


class MenuSubCategoryDetailFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Dish
        fields = ['sub_category', 'name']

class MenuSubCategoryDetailView(ListAPIView):
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuSubCategoryDetailFilter

    def get_queryset(self):
        subcategory_id = self.kwargs.get('subcategory_id')
        queryset = Dish.objects.filter(sub_category_id=subcategory_id)

        return queryset
