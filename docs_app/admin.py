from django.contrib import admin

from docs_app.models import EventImage


# Register your models here.
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1
