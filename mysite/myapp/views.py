from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer,ItemListSerializer, ItemSerializer
from .models import Category, Item

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving items.
    """
    # permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing, retrieving and creating orders.
    """
    # permission_classes = (IsAuthenticated,)
    # serializer_class = ItemListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ItemListSerializer
        else:
            return ItemSerializer

    def get_queryset(self):
        """
        This view should return a list of all the orders
        for the currently authenticated user.
        """
        user = self.request.user
        return Item.objects.all()


class CreateItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

