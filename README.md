# Back-End

## Endpoints For Trainer

### Trainer List View

`/trainer`

### Trainer Detail View

`/trainer/<int:pk>`

### Get New Card

url: `/trainer/card`

**Requires Auth Token**

## Endpoints For Game

### /game

Endpoint for creating a Game instance

`body:
{
    "deck": [{POKEMON_ONE},{POKEMON_TWO},{POKEMON_THREE}]
}`

### /game/battle

Endpoint for playing a round, takes a put request

`body:
{
    "game": GAME_ID,
    "selection": ATTACK
}`

where `GAME_ID` is the id for the game we are in and `ATTACK` is one of the three following strings:

1. `base`
2. `special`
3. `defense`


