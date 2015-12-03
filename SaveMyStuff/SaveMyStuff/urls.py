from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from API import views




router = DefaultRouter()

router.register(r'categories', views.CategoryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'properties', views.PropertyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

