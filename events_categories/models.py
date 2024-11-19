from django.db import models
from volunteers.models import Volunteer  # Import Volunteer model if it’s in another app


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(
        max_length=255, null=True, blank=True)  # Optional
    date = models.DateField(null=True, blank=True)  # Optional
    time = models.TimeField(null=True, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "events"  # to force the naming of the table


# New Application model
class Application(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='applications')
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.volunteer} applied to {self.event}"

    class Meta:
        unique_together = ('event', 'volunteer')  # Ensure a volunteer can apply only once per event
