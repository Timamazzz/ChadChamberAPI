from django.db import models


# Model for the type of event
class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Name")

    class Meta:
        app_label = 'feed_app'
        verbose_name_plural = "Event Types"
        verbose_name = "Event Type"

    def __str__(self):
        return self.name


# Model for the category of event
class EventCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Name")

    class Meta:
        app_label = 'feed_app'
        verbose_name_plural = "Event Categories"
        verbose_name = "Event Category"

    def __str__(self):
        return self.name


# Model for the event
class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, verbose_name="Event Type")
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, verbose_name="Category")
    title = models.CharField(max_length=200, verbose_name="Title")
    start_datetime = models.DateTimeField(verbose_name="Start Date and Time")
    end_datetime = models.DateTimeField(verbose_name="End Date and Time", null=True, blank=True,
                                        help_text="If you want to enter only one "
                                                  "date and time, fill in only the "
                                                  "start date and time.")
    text = models.TextField(verbose_name="Text")
    is_published = models.BooleanField(default=False, verbose_name="Is Published")
    address = models.CharField(max_length=255, verbose_name="Address")

    class Meta:
        app_label = 'feed_app'
        verbose_name_plural = "Events"
        verbose_name = "Event"

    def __str__(self):
        return self.title
