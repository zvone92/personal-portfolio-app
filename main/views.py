from django.shortcuts import render
from .models import About, Skill, Project


def portfolio(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {'about': about,
               'skills': skills,
               'projects': projects,
    }

    return render(request, 'portfolio.html', context)
