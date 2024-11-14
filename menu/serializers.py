from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from menu.models import MenuCategory, MenuSubCategory, Dish, Ingredient


class MenuCategorySerializer(ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']


class MenuCategoryFullSerializer(ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = '__all__'


class MenuSubCategorySerializer(ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = ['id', 'name', 'cover_image']


class MenuSubCategoryFullSerializer(ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = '__all__'


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class IngredientFullSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class DishSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'photo', 'ingredients']


class DishFullSerializer(ModelSerializer):
    ingredients = PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(), many=True)

    class Meta:
        model = Dish
        fields = '__all__'
