from django.db import models

from restaurants.models import Restaurant


class MenuCategory(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')

    def __str__(self):
        return f'{self.name} menu at {self.restaurant}'

class MenuSubCategory(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='subcategory_covers/', blank=True)
    parent_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='dish_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_category = models.ForeignKey(MenuSubCategory, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name