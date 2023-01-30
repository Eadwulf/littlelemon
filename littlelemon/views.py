from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)

from .serializers import MenuItemSerializer, CategorySerializer
from .models import MenuItem, Category


class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CategoryItemsView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SingleCategoryItemView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer