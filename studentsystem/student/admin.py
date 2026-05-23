from django.contrib import admin

from .models import Attendance, Mark, StudentProfile, Subject


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'admission_number', 'user', 'course', 'semester', 'phone')
    search_fields = ('roll_number', 'admission_number', 'user__username', 'user__first_name')
    list_filter = ('course', 'semester')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'semester')
    search_fields = ('code', 'name')
    list_filter = ('semester',)


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'internal_marks', 'external_marks', 'total_marks', 'result')
    search_fields = ('student__roll_number', 'subject__name', 'subject__code')
    list_filter = ('result', 'subject')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'date', 'status')
    search_fields = ('student__roll_number', 'subject__name', 'subject__code')
    list_filter = ('status', 'date', 'subject')

# Register your models here.
