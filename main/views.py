from django.shortcuts import render
from .models import About, Skill, Project


def portfolio(request):
    about = About.objects.first()
    skills = Skill.objects.all().order_by('pk')
    projects = Project.objects.all().order_by('pk')

    context = {'about': about,
               'skills': skills,
               'projects': projects,
    }

    return render(request, 'portfolio.html', context)
