from audit.models import *
from django.contrib import admin

class LogAdmin(admin.ModelAdmin):
    list_display = ('user','update_type','update_date', 'details')
    list_filter = ('update_type',)
    search_fields = ['user__username', 'user__last_name', 'user__first_name', 'user__email']
    list_per_page = 20
    date_hierarchy = 'update_date'
    raw_id_fields = ('user',)
    fields = ('user', 'by_user_id', 'details', 'url', 'update_type')

admin.site.register(Log, LogAdmin)

class UpdateTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)

admin.site.register(UpdateType, UpdateTypeAdmin)