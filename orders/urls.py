from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'create/$', views.order_create, name='orders_create'),
]