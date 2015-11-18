from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from API import views
from django.conf.urls import include



urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^categories/$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

