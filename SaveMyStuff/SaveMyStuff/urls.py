from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from API import views
from rest_framework.authtoken import views as authviews




router = DefaultRouter()

router.register(r'categories', views.CategoryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'properties', views.PropertyViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'propertyitems', views.PropertyItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', authviews.obtain_auth_token)
]

