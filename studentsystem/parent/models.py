from django.contrib.auth.models import User
from django.db import models

from student.models import StudentProfile


class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent_id = models.CharField(max_length=20, unique=True)
    relation = models.CharField(
        max_length=20,
        choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Guardian', 'Guardian')],
    )
    phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, blank=True)
    address = models.TextField()
    children = models.ManyToManyField(StudentProfile, blank=True)

    def __str__(self):
        return f'{self.parent_id} - {self.user.get_full_name() or self.user.username}'

# Create your models here.
