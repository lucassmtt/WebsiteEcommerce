from rest_framework.routers import DefaultRouter
from api import views


app_name = 'api'


router = DefaultRouter(trailing_slash=False)


router.register(r'categories', views.CategoryViewSet)


router.register(r'products', views.ProductViewSet)


router.register(r'users', views.UserViewSet)


router.register(r'orders', views.OrderViewSet)


router.register(r'orders-items', views.OrderItemViewSet)


router.register(r'userAdmin', views.UserAdminViewSet)


router.register(r'adminOrders', views.AdminPedidos)

## TODO: requires readjustment
router.register(r'users-orders', views.UsuariosPedidos)


urlpatterns = router.urls
