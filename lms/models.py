from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="שם המקצוע")
    description = models.TextField(blank=True, verbose_name='תיאור')

    def __str__(self):
        return self.name

class Resource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='מקצוע')
    title = models.CharField(max_length=200, verbose_name='סילבוס')
    file = models.FileField(upload_to='resources/', blank=True, null=True, verbose_name='קןבץ')
    link = models.URLField(blank=True, null=True, verbose_name='קישור')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.course.name}'

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='סטודנט')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="מקצוע")
    exam_name = models.CharField(max_length=100, verbose_name='שם המטלה')
    score = models.FloatField(verbose_name='ציון')

    def __str__(self):
        return f'{self.student.username} - {self.exam_name}: {self.score}'


