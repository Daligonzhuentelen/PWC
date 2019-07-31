from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from galeria.models import Imagen
from django.utils import timezone
from django.views import generic


class ImagenListView(generic.ListView):
    model = Imagen
    template_name = 'galeria/galeria.html'
