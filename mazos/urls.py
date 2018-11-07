from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    #^mazos/nueva/$
    #url(r'^$', views.ejercito_nuevo, name='ejercito_nuevo'),
    url(r'^$', views.listar_arenas, name='listar_arenas'),
    url(r'^mazos/(?P<pk>[0-9]+)/$', views.detalle_arenas,  name='detalle_arenas'),
    url(r'^mazos/nuevo/$', views.ejercito_nuevo, name='ejercito_nuevo'),
    url(r'^mazos/(?P<pk>[0-9]+)/editar/$', views.ejercito_editar, name='ejercito_editar'),
    url(r'^mazos/(?P<pk>\d+)/eliminar/$', views.ejercito_eliminar, name='ejercito_eliminar'),
    ]
