from django.urls import path

from .views.ProductViews import (
    ProductListAPIView,
    ProductFilterAPIView,
    ProductDetailAPIView
)


app_name = "StockAPI"
urlpatterns = [
    path("product/SearchString/<str:querryString>",ProductFilterAPIView.as_view() ),
    path('product/<int:productId>',ProductDetailAPIView.as_view()),
    path("product",ProductListAPIView.as_view()),

]