from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course, Grade

@login_required(login_url='/admin/login/')
def dashboard(request):
    student_grades = Grade.objects.filter(student=request.user)
    courses = Course.objects.all()
    context = {
        'grades': student_grades,
        'courses': courses,
    }
    return render(request, 'lms/dashboard.html', context)
