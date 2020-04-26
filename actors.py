import pygame
import os


class Actor:
    """
    An abstract class that will represent all actors in the game (i.e. Player,
    Monster, Food, etc).
    This class will include all methods and attributes that all actors in the
    game must have.

    === Public Attributes ===
    x_coor: this represents the x coordinate of the player on the map
    y_coor: this represents the y coordinate of the player on the map
    icon: the icon that will represent the actor
    """
    x_coor: int
    y_coor: int
    icon: pygame.Surface

    def __init__(self, icon_file, x_coor, y_coor, delay=5) -> None:
        """
        Initializes a new actor with the coordinates <x_coor>, <y_coor> and the
        icon image <icon_file>
        """
        self.icon = pygame.image.load(os.path.join("images", icon_file))
        self.set_position(x_coor, y_coor)

    def set_position(self, x, y):
        """
        (Actor, int, int) -> None
        Set the position of this Actor to the given x- and y-coordinates.
        """

        (self.x_coor, self.y_coor) = (x, y)

    def move(self, x, y):
        """
        (Actor, int, int) -> bool

        Move the actor to the (x, y) coordinate given
        """

        self.set_position(x, y)
        return True

    def set_move(self, dx, dy):
        """
        (Actor, int, int) -> bool

        Move the actor in the direction of dx, and dy given
        """

        self.set_position(self.x_coor + dx, self.y_coor + dy)
        return True

    def set_position(self, x, y):
        """
        (Actor, int, int) -> None
        Set the position of this Actor to the given x- and y-coordinates.
        """

        (self.x_coor, self.y_coor) = (x, y)
