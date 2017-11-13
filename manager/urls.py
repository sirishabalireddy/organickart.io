from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Login, name='Manager_login'),
]
