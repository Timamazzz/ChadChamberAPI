from django.contrib import admin

from docs_app.models import EventImage
from .models import EventType, EventCategory, Event
from django.db import models
from ckeditor.widgets import CKEditorWidget


# Register EventType model
@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register EventCategory model
@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Define inline for EventImage
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


# Register Event model with inline for EventImage
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'category', 'start_datetime', 'end_datetime', 'is_published')
    list_filter = ('event_type', 'category', 'is_published')
    search_fields = ('title', 'text', 'address')
    inlines = [EventImageInline]

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
