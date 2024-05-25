from django.db import models
from feed_app.models import Event


# Create your models here.
class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Event")
    file = models.FileField("File", null=True, blank=True)
    uploaded_at = models.DateTimeField("Uploaded At", null=True, blank=True, auto_now=True)
    original_name = models.CharField("Original Name", max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'docs_app'
        verbose_name = "Event Image"
        verbose_name_plural = "Event Images"

    def __str__(self):
        return self.file.url if self.file else "Event Image"

    def save(self, *args, **kwargs):
        if self.file and not self.original_name:
            self.original_name = self.file.name
        super().save(*args, **kwargs)
