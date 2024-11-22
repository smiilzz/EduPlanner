from rest_framework import routers
from .api import ApiViewSet
from .views import Lista_Api, obtener_feriados, lista_proyectos_y_feriados, proyectos_y_feriados_html
from django.urls import path

router = routers.DefaultRouter()

router.register('api/Api', ApiViewSet, 'api')

urlpatterns = [
    path('', Lista_Api, name='Lista_Api'),
    path('feriados/', obtener_feriados, name='feriados'),
    path('proyecto-feriados/', lista_proyectos_y_feriados, name='proyectos_feriados'),
    path('proyectos-feriados-html/', proyectos_y_feriados_html, name='proyectos_feriados_html'),
] + router.urls