from django.urls import path
from basic_app import views

# this line is needed if you want to address urls in templates like this
# app_name:view_name
app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
]
