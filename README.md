## Pokulation - Overview
---
Pokulation is a Pokémon simulation game that challenges the player to beat levels by sliding discs across the play field to eliminate all the targets. It uses the Pokémon type effectiveness chart to determine the collision outcomes, for example fire is super effective against water, so when the two tiles collide the fire object is destroyed.

In it's current state there are no playable levels, but a single "debug" stage in the 12th level slot. Levels will be added soon, but the functional components of the game are all present!


## Project Structure 
---
The project files and folders are organized as follows:
```
Pokulation Game       (root folder)
+-- README.md         
+-- Pokulation        (game folder)
  +-- constants.py    (python file for all game constants)
  +-- main.py         (main file. Run this to play the game)
  +-- game            
    +-- casting       (folder for all object classes)
    +-- views         (folder for each scene i.e. title_screen.py)
  +-- assets          
    +-- sprites       (folder containing all png image files)
    +-- sounds        (folder containing all wav sound files)
```

## Video Walkthrough
---
https://youtu.be/Qzx5fxQysK8

## Development Environment
---
This project was created in VS Code for mac. Written in the python language using the python arcade module.

## Future Improvements
---
- I am planning on adding more levels to fill out the level select screen.
- One additional feature I'd like to add to the game are environmental hazards, like pits that detroy all pieces that touch them or ponds that destroy anything that takes super effective damage from water etc..
- I plan on implementing modifiers that can dynamically adjust the size of the objects if they roll into it. Some more modifiers could be super speed, super slow, or multiplication.
- I'd also like to change the collision effects so pieces lose health when they are struck instead of just disappearing. One the piece loses all it's lives it would then be eliminated.

## Author Info
---
Erik Rutledge 
erik.rutledge14@gmail.com 
2/4/2023 
