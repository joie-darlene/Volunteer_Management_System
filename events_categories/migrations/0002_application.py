# Generated by Django 5.1.2 on 2024-11-15 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_categories', '0001_initial'),
        ('volunteers', '0002_alter_volunteer_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='events_categories.event')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='volunteers.volunteer')),
            ],
            options={
                'unique_together': {('event', 'volunteer')},
            },
        ),
    ]
