from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^heart/(?P<video_id>\d+)/(?P<hearted_time>\d+)/$', views.heart, name='heart'),
    url(r'^getHearts/(?P<video_id>\d+)',views.getHearts,name='getHearts'),
]