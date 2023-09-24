from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=False)

    class Meta:
        model = Item
        fields = "__all__"


class ItemListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = "__all__"

    def update(self, instance, validated_data):
        # Handle the update of nested fields here
        category_data = validated_data.pop('category', None)
        if category_data:
            # Update the category of the item
            category, _ = Category.objects.get_or_create(**category_data)
            instance.category = category

        # Update the other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

