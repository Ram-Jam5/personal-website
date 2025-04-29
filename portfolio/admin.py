from django.contrib import admin
from .models import Project
# Register your models here.

admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
    search_fields = ('title',)
    list_editable = ('description', 'url')