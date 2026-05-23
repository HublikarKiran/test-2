from django.contrib.auth.models import User
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    admission_number = models.CharField(max_length=30, unique=True)
    course = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.roll_number} - {self.user.get_full_name() or self.user.username}'


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    semester = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.code} - {self.name}'


class Mark(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    internal_marks = models.PositiveIntegerField(default=0)
    external_marks = models.PositiveIntegerField(default=0)
    total_marks = models.PositiveIntegerField(default=0)
    result = models.CharField(max_length=10, choices=[('Pass', 'Pass'), ('Fail', 'Fail')])

    def save(self, *args, **kwargs):
        self.total_marks = self.internal_marks + self.external_marks
        self.result = 'Pass' if self.total_marks >= 40 else 'Fail'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.student.roll_number} - {self.subject.name}'


class Attendance(models.Model):
    PRESENT = 'Present'
    ABSENT = 'Absent'

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[(PRESENT, 'Present'), (ABSENT, 'Absent')],
    )

    class Meta:
        unique_together = ('student', 'subject', 'date')

    def __str__(self):
        return f'{self.student.roll_number} - {self.subject.code} - {self.status}'

# Create your models here.
