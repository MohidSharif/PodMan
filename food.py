import pygame
from actors import Actor


class Food(Actor):
    """
    This class will be used to represent food in the game.
    """

    def __init__(self, icon_file, x, y):
        """
        Construct a Food with given image, on the given stage, at
        x- and y- position.
        """
        super().__init__(icon_file, x, y)

    def move(self, game) -> None:
        """
        Food cannot move, will stay in their position and will disappear after
        being consumed by the player.
        """
        pass
