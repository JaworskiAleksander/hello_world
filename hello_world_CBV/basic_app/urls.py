from django.urls import path
from basic_app import views

# this line is needed if you want to address urls in templates like this
# app_name:view_name
app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),

    # School links
    path('<int:pk>', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete'),

    # Students ... should't this be split into two, separate applications?!
    path('students/', views.StudentListView.as_view(),name='student_list'),

]