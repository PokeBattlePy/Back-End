# Generated by Django 4.0.1 on 2022-02-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_pokemoncard_moves_alter_pokemoncard_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='cards',
            field=models.JSONField(default=[]),
        ),
        migrations.DeleteModel(
            name='PokemonCard',
        ),
    ]
