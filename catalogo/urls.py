from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductoViewSet

router = DefaultRouter()
router.register('api/productos', ProductoViewSet, basename='producto')

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('', include(router.urls)),
]