from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from portfolio_app.models import Project

# Create your views here.
# def projects_view(request):
#     return HttpResponse("Čia atvaizduojamas HttpResponse")

def home_view(request):
    return render(request, 'home.html')

def project_view(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

def contacts_view(request):
    return render(request, 'contacts.html')

def input_view(request):
    if request.method == 'POST':
        # Įsitikinkite, kad data yra teisingame formatu
        project_start_date_str = request.POST.get('project_start_date')
        project_start_date = datetime.strptime(project_start_date_str, '%Y-%m-%d').date()

        # Kitas kodas nepakeistas
        title = request.POST.get('title')
        project_resume = request.POST.get('project_resume')
        utl = request.POST.get('utl')
        utl1 = request.POST.get('utl1')
        utl2 = request.POST.get('utl2')
        utl3 = request.POST.get('utl3')
        utl4 = request.POST.get('utl4')
        utl5 = request.POST.get('utl5')
        utl6 = request.POST.get('utl6')
        utl7 = request.POST.get('utl7')
        project_status = request.POST.get('project_status')
        c_remarks = request.POST.get('c_remarks')

        project = Project.objects.create(
            title=title,
            project_resume=project_resume,
            utl=utl,
            utl1=utl1,
            utl2=utl2,
            utl3=utl3,
            utl4=utl4,
            utl5=utl5,
            utl6=utl6,
            utl7=utl7,
            project_start_date=project_start_date,
            project_status=project_status,
            c_remarks=c_remarks,
        )

        project_image = request.FILES.get('project_image')
        if project_image:
            print('Yra paveikslėlis')
            project.project_image = project_image
        project.save()

        return redirect('project')  # 'project' yra jūsų projekto sąrašo URL pavadinimas

    return render(request, 'input.html')
