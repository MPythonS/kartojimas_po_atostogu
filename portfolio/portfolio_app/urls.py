from django.urls import path

from portfolio_app.views import project_view

urlpatterns = [
    path('project/', project_view)
]