# Generated by Django 4.0.1 on 2022-02-06 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0019_remove_trainer_decks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='cards',
            new_name='decks',
        ),
    ]
