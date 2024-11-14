from django.urls import path

from menu.views import MenuCategoryListView, MenuSubCategoryListView, MenuSubCategoryDetailView, \
    DishCreateView, MenuSubCategoryCreateView, MenuCategoryCreateView, \
    MenuCategoryUpdateView, MenuSubCategoryUpdateView, DishUpdateView

urlpatterns = [
    path('menu-categories/', MenuCategoryListView.as_view(), name='categories-list'),
    path('menu-categories/create/',
         MenuCategoryCreateView.as_view(), name='category-create'),
    path('menu-categories/update/<int:pk>/',
         MenuCategoryUpdateView.as_view(), name='category-update'),
    path('subcategories/', MenuSubCategoryListView.as_view(),
         name='subcategories-list'),
    path('subcategories/<int:subcategory_id>/',
         MenuSubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('subcategories/create/', MenuSubCategoryCreateView.as_view(),
         name='subcategory-create'),
    path('subcategories/update/<int:pk>/',
         MenuSubCategoryUpdateView.as_view(), name='subcategory-update'),
    path('dishes/create/', DishCreateView.as_view(), name='dish-create'),
    path('dishes/update/<int:pk>/', DishUpdateView.as_view(), name='dish-update'),
]
