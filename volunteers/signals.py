from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Volunteer
from django.contrib.auth.models import Group

# This signal is triggered after a Volunteer object is saved
@receiver(post_save, sender=Volunteer)
def assign_role_groups(sender, instance, created, **kwargs):
    """
    This function is triggered after a Volunteer is created. It assigns them
    to a specific group based on their role (Recruiter or Volunteer).
    """
    if created:
        # Check the role of the volunteer and assign them to the appropriate group
        if instance.role == 'recruiter':
            group, _ = Group.objects.get_or_create(name='Recruiters')
            instance.groups.add(group)
        elif instance.role == 'volunteer':
            group, _ = Group.objects.get_or_create(name='Volunteers')
            instance.groups.add(group)
