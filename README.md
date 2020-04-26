## PodMan
This project involves recreating our own version of Pac Man called Pod Man. This game will have similar features to that of Pac Man using 'pygame'.

## Authors 
* Sarah Eddeb
* Saransh Jain
* Gabriella Jessica Susanto
* Mohid Sharif

## Navigation
<a name="top"></a> 
1. [Game Description](#intro) 
2. [How to Install the Game](#install)
3. [Game Controls](#gamecontrols)

## <a name="intro"></a>Game Description 
PodMan is our Python implementation of the game "PacMan". The main highlight of PodMan
is its code structure. With its object oriented code structure, 
users can freely edit our code with ease to make their own implementation of the 
classic game. 

PodMan only requires 1 player. 

In the beginning of the game the entire board will have food 
in every possible place the player can go. The player can consume two different types of food.
The first is the most common in the game, which only increment the player's score by a small amount
when consumed. The second type is a powerup (represented by a carrot). Once consumed, the player will
be able to kill monsters (the moment powerup is consumed monsters will run away from the player). Once
a monster is killed they will respawn in the middle of the game. Consuming a monster gives more points
in comparison to consuming the first type of food. (Note this powerup will only last for about
15 seconds.)

The rules are very simple. The player must try to consume all the food in the game without getting killed
by monsters. 

## <a name="install"></a>How to Install the Game
It's very simple to download and play Pod Man. It only requires 3 steps:
1. You can download the latest version of Python [here.](https://www.python.org/downloads/)
2. Download our code from the repository
3. Run the game.py file and play!

## <a name="gamecontrols"></a>Game Controls
Players can control where they move to using the keys a (move left), s (move down), w (move up) and d (move right).

Once the player runs the game.py file they can immediately start playing.

There will be a "Restart" button present on the game screen.
- Players can click on the "Restart" button at anytime to restart the game if needed. 

The game will let the player know if they lost or won by the end of the game.

Addendum:

    Mohid Sharif:
        I mainly worked on the player class and all the interactions the player has with other actors on the game
        screen. I made all the functions for the player class such as move, and check_move, I also added the
        remove_actor funcitons to the actor class. I made the handler for the player to move when the W, A, S, D keys
        are pressed, which then allows for the player to be able to eat food, powerup and kill monsters. I also fixed
        the move function in the monster class where the monsters would eat each other while moving randomly. I added
        a timer for the powerup attribute for the player, where when the player consumes a powerup, the player will
        be able to kill monsters for 15 seconds. I also added a label for the score the player currently has, this
        reads from the score attribute in the game class and displays it on the top of the game screen.
        For the readme file I contributed to the "How to Install the Game" section.
      
      Sarah Eddb:
        My main focus in this project was creating the game class. The game class contains the main game loop where all the 
        pieces of the game are put together. It also includes other necessary methods such as get_actor and remove_actor which 
        lets other classes perform the appropriate interactions. I also worked on the abstract class Actor. All components in 
        the game extend from the class Actor. Additionally, I created the game map (the maze the player goes through) as well 
        as the wall, food, power up, player and monster icons.



