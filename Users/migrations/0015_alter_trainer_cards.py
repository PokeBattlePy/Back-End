# Generated by Django 4.0.1 on 2022-02-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_alter_trainer_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='cards',
            field=models.JSONField(default=list),
        ),
    ]