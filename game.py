from __future__ import annotations
import pygame
import os
from pygame import *
from actors import Actor
from food import Food
from wall import Wall
from player import Player
from monsters import Monster
from powerup import PowerUp
from typing import Optional

# Constants for width and height of the screen
ICON_SIZE = 25
WIDTH = 40
HEIGHT = 17


class Game:
    """
    This class represents the game Pod-Man. It contains a method that will allow
    a user to play the game. It sets up the screen with all the appropriate
    actors.
    ==== Public Attributes ====
    screen: The game screen
    stage_width: The stage width
    stage_height: The stage height
    icon_size: A tuple containing the width and height of the icons
    player: Represents the player in the game
    keys_pressed: The key pressed by the user
    ==== Private Attributes ====
    _game_running: Boolean value representing whether the game is running or not
    _actors: A list containing all the actors in the game
    """
    screen: Optional[Pygame.Surface]
    stage_width: int
    stage_height: int
    size: Optional[tuple]
    player: Optional[Player]
    keys_pressed: Optional[bool]
    _game_running: bool
    
    def __init__(self):
        self._game_running = False
        self.screen = None
        self.player = None
        self.keys_pressed = None
        self.score = 0
        self.player_powerup_timer = 0
        self.clock = pygame.time.Clock()
        self._actors = None
        self.stage_width, self.stage_height = 0, 0
        self.size = (ICON_SIZE * WIDTH, ICON_SIZE * HEIGHT+25)

    def remove_actor(self, actor: Actor) -> None:
        """
        Remove the given <actor> from the game's list of actors.
        """
        for a in self._actors:
            if a == actor:
                self._actors.remove(a)

    def get_actor(self, x: int, y: int) -> Optional[Actor]:
        """
        Return the actor object that exists in the location given by
        <x> and <y>. If no actor exists in that location, return None.
        """
        a = []
        for actor in self._actors:
            if actor.x_coor == x and actor.y_coor == y:
                a.append(actor)
        return a

    def move_actors(self) -> None:
        """
        Move all actors in the game as appropriate.
        """

        for actor in self._actors:
            actor.move(self)

    def game_over(self, msg):
        pygame.init()
        surface = pygame.display.set_mode((ICON_SIZE * WIDTH, ICON_SIZE * HEIGHT+25))
        pygame.display.set_caption('Game Over!')

        back = (0, 168, 201)
        text = (0, 0, 128)

        font_obj = pygame.font.Font('freesansbold.ttf', 32)
        text_surface_obj = font_obj.render(msg, True, text, back)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (500, 200)

        while True:
            surface.fill(back)
            surface.blit(text_surface_obj, text_rect_obj)
            for eve in pygame.event.get():
                if eve.type == QUIT:
                    pygame.quit()
            pygame.display.update()

    def setup_game(self, filename: str) -> None:
        """
        Set up a game with walls, player, food, monsters, and powerUp food on
        the screen
        """
        # open data file to initialize the game screen
        with open(os.path.join("images", filename)) as f:
            data = [line.split() for line in f]

        w = len(data[0])
        h = len(data) + 1

        self._actors = []
        self.stage_width, self.stage_height = w, h - 1
        self.size = (w * ICON_SIZE, h * ICON_SIZE)
        # loop though each line to the file and set up the game
        for i in range(len(data)):
            for j in range(len(data[i])):
                # initialize all objects in the file and add them to the _actors attribute
                legend = data[i][j]
                if legend == 'P':  # P is player object
                    player = Player(
                        "player.png", j, i)
                    self.player = player
                    self._actors.append(player)
                elif legend == 'X':  # X is a wall object
                    self._actors.append(
                        Wall("wall.png", j, i))
                elif legend == 'M':  # M is a monster object
                    self._actors.append(
                        Monster("monster.png", j, i))
                elif legend == 'O':  # O is a food object
                    self._actors.append(
                        Food("food.png", j, i))
                elif legend == 'U':  # U is a powerup object
                    self._actors.append(
                        PowerUp("powerUp.png",
                                j, i))

    def draw_screen(self):
        """
        Draw the screen the user sees with all actors at their appropriate positions
        """
        self.screen.fill((0, 168, 201))
        # draw a timer label on screen
        myfont = pygame.font.SysFont("monospace", 15)
        timer = myfont.render("PowerUp time left: " + str(int(self.player_powerup_timer)), 1, (0, 0, 10))
        self.screen.blit(timer, (85, 0))
        # draw a score label on screen
        myfont = pygame.font.SysFont("monospace", 15)
        score = myfont.render("Score: " + str(self.score), 1, (0, 0, 10))
        self.screen.blit(score, (300, 0))

        # loops through _actors list and draws game with actors at their specific locations
        for a in self._actors:
            rect = pygame.Rect(a.x_coor * ICON_SIZE, a.y_coor * ICON_SIZE+25,
                               ICON_SIZE,
                               ICON_SIZE)
            self.screen.blit(a.icon, rect)
        display.flip()

    def play_game(self):
        """
        Main loop of the game.
        Initialize the game and draw the screen, record all actions by the user
        then make changes accordingly, redraw screen after every action performed
        by the user and every change to the actors' positions
        """
        pygame.init()
        self.screen = pygame.display.set_mode \
            (self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        # game running initialized to true and game is setup with map.txt file
        self._game_running = True
        self.setup_game("map.txt")
        # while game is running
        while self._game_running:
            # timer for player's power up
            if self.player.has_power_up:
                # setup the clock's ticks
                if self.player_powerup_timer is 0:
                    self.player_powerup_timer = 15

                dt = self.clock.tick(30)/1000
                # keep decreasing timer
                if dt < 1:
                    self.player_powerup_timer -= dt
                # runs for ~15 seconds, thus the powerup lasts 15 seconds
                if int(self.player_powerup_timer) is 0:
                    # return players_has_power_up back to False, and monster is_vulnerable to False
                    self.player.has_power_up = False
                    for a in game._actors:
                        if 'Monster' in str(a):
                            a.is_vulnerable = False
                    self.player_powerup_timer = 0
            # delay of 100
            pygame.time.wait(100)
            # read event on game screen
            for eve in pygame.event.get():
                # end the game or record event
                if eve.type == QUIT:
                    self._game_running = False
                elif eve.type == pygame.KEYDOWN:
                    self.player.handle_event(eve.key)
            if self.player not in self._actors:
                self.game_over("Game Over Score: " + str(self.score))
                self._game_running = False
            # keep moving actors every loop, and redraw screen
            self.move_actors()
            self.draw_screen()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.play_game()

