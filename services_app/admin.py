from django.contrib import admin
from .models import Service
from django.db import models
from ckeditor.widgets import CKEditorWidget


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ('name', 'short_description')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
