# Back-End

## Endpoints For Game

#### /game

**requires auth token**
Endpoint for creating a Game instance

body:
{
    `DECK FROM TRAINER`
}

#### /game/battle

**requires auth token**
Endpoint for playing a round, takes a put request

body:
{
    "game":`GAME_ID`,
    "selection":`ATTACK`
}

where `GAME_ID` is the id for the game we are in and `ATTACK` is one of the three following strings:

1. `base`
2. `special`
3. `defense`

