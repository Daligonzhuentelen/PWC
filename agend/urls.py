from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse
from .models import *
from . import views
from .views import *
app_name = 'agend'

urlpatterns = [
    path('', AgendaListView.as_view(), name='agenda'),
    
] 
 
 
 
 