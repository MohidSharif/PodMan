import pygame
from actors import Actor

class Wall(Actor):
    """
    This class will represent a wall in the game. This will be used to create
    the map of the game.
    """

    def __init__(self, icon_file, x, y):
        """
        Construct a Wall with given image, on the given stage, at
        x- and y- position.
        """
        super().__init__(icon_file, x, y)

    def move(self, game) -> None:
        """
        Walls do not need to move, so they will stay in their position.
        """
        pass
