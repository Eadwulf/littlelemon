from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    secret, manager_view,
    MenuItemsViewSet, MenuItemViewSet, CategoryItemsViewSet, CategoryItemViewSet,
)


urlpatterns = [
    path('auth-token', obtain_auth_token),

    path('secret', secret),
    path('manager-secret', manager_view),

    path('menu', MenuItemsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('menu/<int:pk>', MenuItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='menuitem-detail'),

    path('categories', CategoryItemsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>', CategoryItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='category-detail'),
]