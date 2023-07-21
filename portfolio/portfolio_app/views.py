from django.http import HttpResponse
from django.shortcuts import render

from portfolio_app.models import Project


# Create your views here.
# def projects_view(request):
#     return HttpResponse ("Čia atvaizduojamas HttpResponse")

def home_view(request):
    return render(request, 'home.html')

def project_view(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

def contacts_view(request):
    return render(request, 'contacts.html')