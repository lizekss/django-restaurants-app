from rest_framework.serializers import ModelSerializer

from menu.models import MenuCategory, MenuSubCategory


class MenuCategorySerializer(ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']

class MenuSubCategorySerializer(ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = ['name', 'cover_image']

