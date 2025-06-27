from django.shortcuts import render
from .models import Skill, Experience, Project

def resume_view(request):
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    return render(request, 'resume.html', {
        'skills': skills,
        'experiences': experiences,
        'projects': projects
    })
