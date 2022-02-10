from django.contrib import admin

from teachers.models import Teacher



@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name',)