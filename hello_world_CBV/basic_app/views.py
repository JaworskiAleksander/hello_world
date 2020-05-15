from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)

# import all class declarations from basic_app.models
from . import models

# Create your views here.
class IndexView(TemplateView):
    # template_name is a class-based attribute inherited from Template_View
    # it tells which template should be rendered when calling out this class as view // .as_view()
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Message of the day'
        return context

# Class Naming Convention
# ClassNameViewType(ViewType)

class SchoolListView(ListView):
    # model = models.className
    model = models.School
    # school_list - this attribute is created automatically
    # className_list = className.objects.all()
    # alternatively, you can define under which var name data will be accessible
    # context_object_name = 'className_list' when inheriting from ListView
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    # by default, context_object_name is set to className, nothing attached to it, when inheriting\
    # from DetailView
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    pass