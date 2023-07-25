from django.urls import path

from . import views


urlpatterns = [
    # path('httpresponse/', projects_view),
    path('', views.home_view, name='home'),
    path('project/', views.project_view, name='project'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('input/', views.input_view, name='input_form'),
]