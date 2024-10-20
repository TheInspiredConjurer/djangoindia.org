# Generated by Django 5.1.2 on 2024-10-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_eventregistration_attendee_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='attendee_type',
            field=models.CharField(choices=[('guest', 'Guest'), ('host', 'Host'), ('speaker', 'Speaker'), ('volunteer', 'Volunteer')], default='guest', max_length=20),
        ),
    ]
