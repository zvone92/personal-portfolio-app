from django.contrib import admin
from .models import About, Skill, Project

class AboutAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'cover', 'photo', 'detailed_description')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'technologies')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'github_url')

admin.site.register(About, AboutAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
