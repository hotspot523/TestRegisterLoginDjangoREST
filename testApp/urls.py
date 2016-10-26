from django.conf.urls import url
from testApp import views

urlpatterns = [

    url(r'^quick/$', views.test_list),
    url(r'^quick/(?P<pk>[0-9]+)/$', views.test_detail),
]
