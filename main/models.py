from django.db import models


class About(models.Model):

    cover = models.ImageField(upload_to='about', default='/about/mini-startrail.jng')
    photo = models.ImageField(upload_to='about', default='/about/profilna.jng')
    short_description    = models.TextField()
    detailed_description = models.TextField()

    def __str__(self):
        return "Who am i"


class Skill(models.Model):

    icon = models.ImageField(upload_to='skills')
    name  = models.CharField(max_length=100, verbose_name='skill name')
    technologies = models.TextField(verbose_name='Technologies')

    def __str__(self):
        return self.name


class Project(models.Model):

    image = models.ImageField(upload_to='projects')
    name  = models.CharField(max_length=100, verbose_name='Project name')
    description = models.TextField(verbose_name='About project')
    github_url = models.TextField(verbose_name='Github url')

    def __str__(self):
        return self.name
