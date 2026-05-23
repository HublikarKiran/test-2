from django.contrib.auth.models import User
from django.db import models


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100, default='Administration')
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.employee_id} - {self.user.get_full_name() or self.user.username}'

# Create your models here.
