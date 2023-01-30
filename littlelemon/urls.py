from django.urls import path

from .views import (
    MenuItemsView, SingleMenuItemView, CategoryItemsView, SingleCategoryItemView,
)


urlpatterns = [
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menuitem-detail'),

    path('categories', CategoryItemsView.as_view()),
    path('categories/<int:pk>', SingleCategoryItemView.as_view(), name='category-detail'),
]