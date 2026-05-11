from django.contrib import admin
from .models import Course, Resource, Grade

class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [ResourceInline, GradeInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Resource)
admin.site.register(Grade)



