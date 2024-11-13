from django.contrib import admin

from .models import MenuCategory, MenuSubCategory, Dish, Ingredient


admin.site.register(MenuCategory)
admin.site.register(MenuSubCategory)
admin.site.register(Dish)
admin.site.register(Ingredient)
