# Generated by Django 4.0.1 on 2022-02-01 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_trainer_decks_alter_trainer_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncard',
            name='name',
            field=models.CharField(default='gyarados', max_length=32),
        ),
    ]
