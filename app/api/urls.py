from rest_framework.routers import DefaultRouter
from api import views


app_name = 'api'


router = DefaultRouter(trailing_slash=False)
router.register(r'categorias', views.CategoryViewSet)
router.register(r'produtos', views.ProductViewSet)
router.register(r'usuarios', views.UserViewSet)
router.register(r'pedidos', views.OrderViewSet)
router.register(r'item-pedidos', views.OrderItemViewSet)

urlpatterns = router.urls
