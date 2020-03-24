from django.contrib import admin
from .models import About, Skills, Projects

class AboutAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'photo', 'detailed_description')

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'technologies')

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'github_url')

admin.site.register(About, AboutAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Projects, ProjectsAdmin)
