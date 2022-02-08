# Back-End

## Deployed API

[https://poke-battle-py.herokuapp.com/](https://poke-battle-py.herokuapp.com/)
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

### Creating a Game

Once a `Game` has been instantiated by calling the `/game` endpoint the `Game` instance will have access to the deck that you supplied as well as a random deck from another user.

### Playing a Round

Once you have a game instance, calling the `/game/battle` endpoint will update the state of the `Game` with the `game` id passed in the request body. Your Pokemon will use the move associated with the attack `selection` you have chosen. From there the opposing Pokemon will attack back. The updated `Game` state will be sent back in the response body. If either pokemon's hp reaches 0 during the round it will be knocked out and the `active_user_poke` / `active_comp_poke` will be updated to the next Pokemon in the list. If either side runs out of Pokemon the `active_user_poke` / `active_comp_poke` will be set to `null`.
