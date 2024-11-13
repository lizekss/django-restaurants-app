from django.urls import path

from restaurants.views import RestaurantListView

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurants-list'),
]
