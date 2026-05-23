from django.contrib.auth.models import User
from django.db import models

from student.models import Subject


class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    subjects = models.ManyToManyField(Subject, blank=True)
    joining_date = models.DateField()

    def __str__(self):
        return f'{self.employee_id} - {self.user.get_full_name() or self.user.username}'


class FacultyNotice(models.Model):
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
