import pygame
from actors import Actor


class PowerUp(Actor):
    """
    This class represents a PowerUp in the game. Its icon will be a carrot.
    This powerup will enable players to kill monsters.
    """

    def __init__(self, icon_file, x, y):
        """
        Construct a Monster with given image, on the given stage, at
        x- and y- position.
        """
        super().__init__(icon_file, x, y)

    def move(self, game) -> None:
        """
        A PowerUp cannot move, it will be consumed by the player and stay in its
        position.
        """
        pass
