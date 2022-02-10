from django.contrib import admin

from .models import Course,Category,Tags


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','category','available')

@admin.register(Category)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(Tags)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
