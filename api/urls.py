from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^heart', views.heart, name='heart'),
]