from django.contrib import admin
from .models import Service, FAQ

class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [FAQInline]
    list_display = ('title',)

# Register FAQ model directly if you want it standalone, but inline is usually better for admin.
