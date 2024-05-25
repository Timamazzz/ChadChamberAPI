from django.core.management.base import BaseCommand
from feed_app.models import EventType, EventCategory


class Command(BaseCommand):
    help = 'Initialize the database with default event types and categories'

    def handle(self, *args, **kwargs):
        event_types = ['Встреча', 'Соглашение', 'Форум']
        for event_type in event_types:
            EventType.objects.get_or_create(name=event_type)

        categories = ['Бесплатное', 'Платное']
        for category in categories:
            EventCategory.objects.get_or_create(name=category)

        self.stdout.write(self.style.SUCCESS('Database has been initialized successfully'))
