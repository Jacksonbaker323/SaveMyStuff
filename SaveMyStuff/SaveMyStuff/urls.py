from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from API import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^categories/$', views.category_list),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.category_detail),
]


#Finished up here: http://www.django-rest-framework.org/tutorial/1-serialization/
