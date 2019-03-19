from django.urls import path
from pagina.views import vLandingpage

urlpatterns = [
    path('', vLandingpage, name = 'landingpage')
]
