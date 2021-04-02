from django.urls import path, include
from .views import  GenericAPIView, ProductViewSet, ProductAPIView, ProductDetails, OrderAPIView, OrderViewSet, OrderDetails, ShippingAPIView, ShippingViewSet, ShippingDetails,UserViewSet,UserDetails,UserAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product'),
router.register('order', OrderViewSet, basename='order'),
router.register('shipping', ShippingViewSet, basename='shipping'),
router.register('user', UserViewSet, basename='user')


urlpatterns= [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('product/', ProductAPIView.as_view()),
    path('generic/product/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/', ProductDetails.as_view),
    path('generic/product/<int:id>/', GenericAPIView.as_view()),
    path('order/', OrderAPIView.as_view()),
    path('generic/order/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/', OrderDetails.as_view),
    path('generic/order/<int:id>/', GenericAPIView.as_view()),
    path('shipping/', ShippingAPIView.as_view()),
    path('generic/shipping/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/', ShippingDetails.as_view),
    path('generic/shipping/<int:id>/', GenericAPIView.as_view()),
    path('shipping/', UserAPIView.as_view()),
    path('generic//<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/', UserDetails.as_view),
    path('generic/user/<int:id>/', GenericAPIView.as_view()),
]

