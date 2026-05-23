from django.contrib import admin

from .models import ParentProfile


@admin.register(ParentProfile)
class ParentProfileAdmin(admin.ModelAdmin):
    list_display = ('parent_id', 'user', 'relation', 'phone')
    search_fields = ('parent_id', 'user__username', 'user__first_name', 'phone')
    list_filter = ('relation',)
    filter_horizontal = ('children',)

# Register your models here.
