# Generated by Django 5.0.1 on 2024-01-12 17:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f4322c0f-af4e-4e46-a5ad-d60f217a4419'), editable=False, primary_key=True, serialize=False),
        ),
    ]
