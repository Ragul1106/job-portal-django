from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'employment_type', 'is_active', 'created_at')
    list_filter = ('employment_type', 'is_active', 'created_at', 'location')
    search_fields = ('title', 'company', 'location')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('user__username', 'job__title', 'job__company')
    list_editable = ('status',)
    date_hierarchy = 'applied_at'
