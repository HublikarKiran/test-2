from django.contrib import admin

from .models import FacultyNotice, FacultyProfile


@admin.register(FacultyProfile)
class FacultyProfileAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'department', 'designation', 'phone', 'joining_date')
    search_fields = ('employee_id', 'user__username', 'user__first_name', 'department')
    list_filter = ('department', 'designation')
    filter_horizontal = ('subjects',)


@admin.register(FacultyNotice)
class FacultyNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'faculty', 'created_at')
    search_fields = ('title', 'faculty__employee_id')
    list_filter = ('created_at',)

# Register your models here.
