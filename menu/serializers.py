from rest_framework.serializers import ModelSerializer

from menu.models import MenuCategory, MenuSubCategory, Dish, Ingredient


class MenuCategorySerializer(ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']

class MenuSubCategorySerializer(ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = ['id', 'name', 'cover_image']

class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']

class DishSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'photo', 'ingredients']