from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def project_view(request):
    return HttpResponse ("Čia bus projektai")