from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    #^mazos/nueva/$
    url(r'^mazos/(?P<pk>[0-9]+)/edit/$', views.ejercito_nuevo, name='ejercito_nuevo'),
    ]
