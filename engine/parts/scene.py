"""Модуль со сценой."""

from math import floor

from engine.parts.characters import Player
from engine.parts.map import Map
from levels.level import PLAYER_PHI0, PLAYER_X0, PLAYER_Y0, MAP_SCHEME


class Scene:
    """Класс сцены."""

    def __init__(self) -> None:
        """Инициализация экземпляра класса."""
        self.map = Map(MAP_SCHEME)
        self.player = Player(PLAYER_X0, PLAYER_Y0, PLAYER_PHI0)

    def solve_collisions(self):
        """Разрешить коллизии по необходимости."""
        floor_x = floor(self.player.x)
        floor_y = floor(self.player.y)
        if self.map.get(floor_x, floor_y) == 1:
            dists = {'left': self.player.x - floor_x,
                     'right': floor_x + 1 - self.player.x,
                     'up': self.player.y - floor_y,
                     'down': floor_y + 1 - self.player.y}
            key_min = min(dists, key=dists.get)
            
            if key_min == 'left':
                self.player.x = floor_x
                del dists['left']
            elif key_min == 'right':
                self.player.x = floor_x + 1
                del dists['right']
            elif key_min == 'up':
                self.player.y = floor_y
                del dists['up']
            elif key_min == 'down':
                self.player.y = floor_y + 1
                del dists['down']

            floor_x = floor(self.player.x)
            floor_y = floor(self.player.y)
            if self.map.get(floor_x, floor_y) == 1:
                key_min = min(dists, key=dists.get)

                if key_min == 'left':
                    self.player.x = floor_x
                elif key_min == 'right':
                    self.player.x = floor_x + 1
                elif key_min == 'up':
                    self.player.y = floor_y
                elif key_min == 'down':
                    self.player.y = floor_y + 1


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
