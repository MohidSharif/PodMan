from typing import Optional

import pygame
from actors import Actor
from food import Food
from wall import Wall
from monsters import Monster
from powerup import PowerUp


class Player(Actor):
    """
    A class that will represent the player in the game =
    This class will include all methods and attributes that the player must have in the game.

    """
    has_power_up: bool
    is_dead: bool
    _last_event: Optional[int]

    def __init__(self, icon_file, game, x=0, y=0) -> None:
        """
        Construct a Player with given image, on the given stage, at
        x- and y- position.
        """
        super().__init__(icon_file, game, x, y)
        self.is_dead = False
        self.has_power_up = False
        self._last_event = None  # last even that has occurred by the user

    def check_move(self, game, dx, dy) -> bool:
        """
        Check if the move by dx and dy is possible.
        If a move is possible (a space is available) then move to it.
        If another Actor is occupying that space, then depending on the type of actor, the
        player will move if possible.
        """
        act = True  # if the action is performable
        # get the actors in the position the player wants to move to
        new_x = self.x_coor + dx
        new_y = self.y_coor + dy
        a = game.get_actor(new_x, new_y)
        # loop through all actors in the new position
        for actor in a:
            # interactions will happen here, i.e. player dies, monsters die, food disappears
            # score is also increased here
            if 'Wall' in str(actor):
                return False

            if 'Player' in str(self) and 'Monster' in str(actor) and not self.has_power_up:
                game.remove_actor(self)
                self.is_dead = True
            elif 'Player' in str(self) and 'Monster' in str(actor) and self.has_power_up:
                game.remove_actor(actor)
                game.score += 200

            if 'Food' in str(actor):
                game.score += 10
                game.remove_actor(actor)
                # increase score

            if 'powerup' in str(actor):
                if self.has_power_up:
                    game.player_powerup_timer = 15
                self.has_power_up = True
                game.remove_actor(actor)
                for a in game._actors:
                    if 'Monster' in str(a):
                        a.is_vulnerable = True
        # if the move was valid then the move is made here
        if not act:
            return False
        else:
            return super().move(new_x, new_y)

    def handle_event(self, event):
        """
        (KeyboardPlayer, int) -> None
        Record the last event directed at this Player.
        All previous events are ignored.
        """
        self._last_event = event

    def move(self, game) -> None:
        """
        Move this Actor by dx and dy, if possible.
        If a move is possible (a space is available) then move to it.
        If another Actor is occupying that space, then depending on the type of actor, the
        player will move if possible.
        """
        dx = 0
        dy = 0
        # move in a direction depending on which keys were pressed last
        if self._last_event is not None:
            if self._last_event == pygame.K_s:  # Player moves DOWN with s key
                dx, dy = 0, 1
            if self._last_event == pygame.K_a:  # Player moves LEFT with a key
                dx, dy = -1, 0
            if self._last_event == pygame.K_d:  # Player moves RIGHT with d key
                dx, dy = 1, 0
            if self._last_event == pygame.K_w:  # Player moves UP with w key
                dx, dy = 0, -1
            if dx is not None and dy is not None:
                self.check_move(game, dx, dy)
            # make last even None again
            self._last_event = None
