# Generated by Django 5.0.1 on 2024-01-11 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='event',
            table='events',
        ),
        migrations.AlterModelTable(
            name='eventhistory',
            table='event_history',
        ),
    ]
