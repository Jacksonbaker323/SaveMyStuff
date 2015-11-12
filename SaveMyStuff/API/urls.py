from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^categories/$', views.category_list),
    url(r'^categories$', views.category_detail),
]