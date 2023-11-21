from django.urls import path

from .views.ProductViews import (
    ProductListAPIView,
    ProductFilterAPIView,
    ProductDetailAPIView
)

from .views.OrderViews import (
    OrderListAPIView,
)

from .views.WhareHouseViews import (
    WhareHouseListAPIView,
    WhareHouseDetailAPIView
)

from .views.HandlerViews import (
    HandlerDetailAPIView,
    HandlerListAPIView
)

from .views.CategoryViews import (
    CategoryDetailAPIView,
    CategoryListAPIView
)


app_name = "StockAPI"
urlpatterns = [
    path("product/SearchString/<str:querryString>",ProductFilterAPIView.as_view() ),
    path('product/<int:productId>',ProductDetailAPIView.as_view()),
    path("product",ProductListAPIView.as_view()),
    path("order",OrderListAPIView.as_view()),

    path("wharehouse",WhareHouseListAPIView.as_view()),
    path("wharehouse/<int:wharehouse_id>",WhareHouseDetailAPIView.as_view()),

    path("handler",HandlerListAPIView.as_view()),
    path("handler/<int:handler_id>",HandlerDetailAPIView.as_view()),

    path("category",CategoryListAPIView.as_view()),
    path("category/<int:category_id>",CategoryDetailAPIView.as_view()),

]