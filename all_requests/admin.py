from django.contrib import admin

# Register your models here.
from all_requests.models import AllRequest


@admin.register(AllRequest)
class AllRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
