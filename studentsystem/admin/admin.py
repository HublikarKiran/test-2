from django.contrib import admin

from .models import AdminProfile


@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'department', 'phone')
    search_fields = ('employee_id', 'user__username', 'user__first_name', 'department')
    list_filter = ('department',)

# Register your models here.
