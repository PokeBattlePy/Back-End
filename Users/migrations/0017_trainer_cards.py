# Generated by Django 4.0.1 on 2022-02-06 09:13

from django.db import migrations, models
import django.contrib

class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_remove_trainer_cards'),
    ]

    operations = [
    migrations.AddField(
        model_name='trainer',
        name='cards',
        field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list),
    ),
]
