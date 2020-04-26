import pygame
import random
from actors import Actor

class Monster(Actor):
    """A Monster class."""
    is_vulnerable: bool # if the player has a powerup, the monster is vulnerable
    is_dead: bool # if the player runs into the monster with a powerup active

    def __init__(self, icon_file, x=0, y=0, delay=5):
        """
        Construct a Monster with given image, on the given stage, at
        x- and y- position.
        """
        super().__init__(icon_file, x, y)
        self.is_vulnerable = False
        self.is_dead = False

    def check_move(self, game, dx, dy) -> bool:
        """
        Check if the move by dx and dy is possible.
        If a move is possible (a space is available) then move to it.
        If another Actor is occupying that space, then depending on the type of actor, the
        player will move if possible.
        """
        # find all actors occupying the given space
        new_x = self.x_coor + dx
        new_y = self.y_coor + dy
        a = game.get_actor(new_x, new_y)
        # loop through all the actors in that space
        for actor in a:
            # all interactions with monster happen here, i.e. kill monster, kill player
            if 'Wall' in str(actor):
                return False

            if 'Player' in str(actor) and self.is_vulnerable is True:
                game.remove_actor(self)
            elif 'Player' in str(actor):
                game.remove_actor(actor)
        
        return super().move(new_x, new_y)

    def move(self, game) -> None:
        """
        Move this Actor by dx and dy, if possible.
        If a move is possible (a space is available) then move to it.
        """
        dx = 0
        dy = 0
        # randomly move the monster in a direction
        if self.is_dead is False:
            while dx == 0 and dy == 0:
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
            self.check_move(game, dx, dy)
