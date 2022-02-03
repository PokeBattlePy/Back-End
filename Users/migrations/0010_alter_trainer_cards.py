# Generated by Django 4.0.1 on 2022-02-03 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_alter_trainer_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='cards',
            field=models.JSONField(default=[{'back': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/147.png', 'front': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/147.png', 'moves': {'base': {'class': 'physical', 'name': 'slam', 'power': 80, 'type': 'normal'}, 'special': {'class': 'physical', 'name': 'bind', 'power': 15, 'type': 'normal'}}, 'name': 'dratini', 'official_artwork': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/147.png', 'pokemon_int': 147, 'rarity': 'uncommon', 'stats': {'attack': 70.4, 'defense': 49.50000000000001, 'hp': 45.1, 'special-attack': 55.00000000000001, 'special-defense': 55.00000000000001}, 'types': ['dragon']}, {'back': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/122.png', 'front': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/122.png', 'moves': {'base': {'class': 'physical', 'name': 'double-slap', 'power': 15, 'type': 'normal'}, 'special': {'class': 'physical', 'name': 'pound', 'power': 40, 'type': 'normal'}}, 'name': 'mr-mime', 'official_artwork': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/122.png', 'pokemon_int': 122, 'rarity': 'common', 'stats': {'attack': 45, 'defense': 65, 'hp': 40, 'special-attack': 100, 'special-defense': 120}, 'types': ['psychic', 'fairy']}]),
        ),
    ]