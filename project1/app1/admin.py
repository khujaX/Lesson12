from django.contrib import admin
from .models import Site

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price"]
    list_display_links = ["name"]
    search_fields = ["id", "name", "price"]

admin.site.register(Site, SiteAdmin)
