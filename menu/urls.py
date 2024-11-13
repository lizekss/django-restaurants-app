from django.urls import path

from menu.views import MenuCategoryListView, MenuSubCategoryListView, MenuSubCategoryDetailView

urlpatterns = [
    path('menu-categories', MenuCategoryListView.as_view(), name='categories-list'),
    path('subcategories', MenuSubCategoryListView.as_view(), name='subcategories-list'),
    path('subcategories/<int:subcategory_id>', MenuSubCategoryDetailView.as_view(), name='subcategory-detail'),
]