from django.urls import path
from pagina.views import vLandingpage, vprueba

urlpatterns = [
    path('', vLandingpage, name = 'landingpage'),
    path('prueba', vprueba, name = 'p')
]
