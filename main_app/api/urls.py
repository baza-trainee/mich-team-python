from django.urls import path
from . import views
from .views import (
    ProductListCreateView,
    ProductDetailView,
    ProductCategoryListView,
    ProductImageView,
    SizeQuantityView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', ProductCategoryListView.as_view(), name='category-list-create'),
    path('images/', ProductImageView.as_view(), name='image-list-create'),
    path('sizes_quantities/', SizeQuantityView.as_view(), name='size-quantity-list-create'),
]