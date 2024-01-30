from rest_framework import serializers
from product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    # def get_category(self, obj):
    #     return obj.category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
