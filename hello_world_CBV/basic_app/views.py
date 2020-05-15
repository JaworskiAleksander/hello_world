from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from django.urls import reverse_lazy

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

#------------------------------------------------
# SCHOOL VIEWS

class SchoolListView(ListView):
    # model = models.className
    model = models.School
    # school_list - this attribute is created automatically
    # className_list = className.objects.all()
    # alternatively, you can define under which var name data will be accessible
    # context_object_name = 'className_list' when inheriting from ListView
    context_object_name = 'schools'
    # from now on, use context_object_name to grab data provided by SchoolListView

class SchoolDetailView(DetailView):
    # by default, context_object_name is set to className, nothing attached to it, when inheriting\
    # from DetailView
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    # connecting CreateView with model class
    model = models.School
    # specifying which fields can be entered by user
    fields = ('name', 'principal', 'location')
    # by default, django will search for app_name/className_form.html template to use
    # you can change that by specifying template_name

class SchoolUpdateView(UpdateView):
    # specify which fields user will be able to update
    fields = ('name', 'principal')
    # connect this class to a proper model class
    model = models.School

class SchoolDeleteView(DeleteView):
    # connect class with a proper model Class
    model = models.School
    # for DeleteView default context_object_name is lower_cased class name you've set model with
    # DeleteView sends all fields, unless defined 'fields' class attribute
    # success_url class attribute - defines what template to use once an object is removed successfuly
    success_url = reverse_lazy('basic_app:list')


#------------------------------------------------
# STUDENT VIEWS