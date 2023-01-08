from django.contrib import admin
from .models import Qualification


class QualificationAdmin(admin.ModelAdmin):
    list_display = ['qualification_name', 'precent', 'salary']
admin.site.register(Qualification, QualificationAdmin)