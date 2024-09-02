from .views import ProductViewSet, UserApiView
from django.urls import path

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
    })),
    path('user', UserApiView.as_view())
]
