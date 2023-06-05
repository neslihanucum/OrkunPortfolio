from django.shortcuts import render
from django.views.generic import ListView, DetailView
from orkun.models import Project

class HomeView(ListView):
    model = Project
    template_name ='home.html'
    ordering = ['-project_date']

    def get_context_data(self, *args, **kwargs):
        project = Project.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["project"] = project
        return context

class SingleProject(DetailView):
    model = Project
    template_name = "single_project.html"