from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse
from . import views
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('servicios/', ServiciosView.as_view(), name='servicios'),
    path('centros/', CentrosView.as_view(), name='centros'),
    
] 