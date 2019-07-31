from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from  .models import Agenda
from django.urls import reverse
from django.utils import timezone
from django.views import generic


class AgendaListView(generic.ListView):
    model = Agenda
    template_name = 'agend/agenda.html'
class AgendaDetailView(generic.DetailView):
    model = Agenda
    template_name = 'agend/agenda_detail.html'
    slug_field = 'titulo_agenda'