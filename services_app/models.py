from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    short_description = models.CharField(max_length=255, verbose_name="Short Description")
    text = models.TextField(verbose_name="Text")

    class Meta:
        app_label = 'services_app'
        verbose_name_plural = "Services"
        verbose_name = "Service"

    def __str__(self):
        return self.name
