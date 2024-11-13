from django.urls import path

from menu.views import MenuCategoryListView, MenuSubCategoryListView

urlpatterns = [
    path('menu-categories', MenuCategoryListView.as_view(), name='categories-list'),
    path('subcategories', MenuSubCategoryListView.as_view(), name='subcategories-list'),
]