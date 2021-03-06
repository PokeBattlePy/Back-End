# Generated by Django 4.0.1 on 2022-02-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0021_remove_trainer_decks_remove_trainer_prev_battles'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='cards',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='trainer',
            name='decks',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='trainer',
            name='prev_battles',
            field=models.JSONField(default=list),
        ),
    ]
