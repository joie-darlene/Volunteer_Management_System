from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Model for volunteers
class Volunteer(AbstractUser):
    ROLE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('volunteer', 'Volunteer'),
    ]
    # Fields for Volunteer model
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    skills = models.TextField(blank=True)
    availability = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='volunteer_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='volunteer_user_permissions',
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "volunteers"
