from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from basic_app.models import *

# Create your views here.
class IndexView(TemplateView):
    # template_name is a class-based attribute inherited from Template_View
    # it tells which template should be rendered when calling out this class as view // .as_view()
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Message of the day'
        return context


