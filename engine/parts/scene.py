"""Модуль со сценой."""

from math import floor

from config import PATH_MAP
from engine.parts.characters import Player


class Scene:
    """Класс сцены."""

    def __init__(self) -> None:
        """Инициализация экземпляра класса."""
        self._read_data_from_map()
        self.player = Player(self.player_x0, self.player_y0)
    
    def _read_data_from_map(self) -> None:
        """Прочитать карту."""
        f = open(PATH_MAP, 'r')
        self.lvl_map = f.read().splitlines()
        f.close()
        
        for i in range(len(self.lvl_map)):
            self.lvl_map[i] = [square for square in self.lvl_map[i]]
            if 'x' in self.lvl_map[i]:
                player_floor_y0 = i
                player_floor_x0 = self.lvl_map[i].index('x')
                self.lvl_map[player_floor_y0][player_floor_x0] = '0'

        self.y_max = len(self.lvl_map)
        self.x_max = len(self.lvl_map[0])
        self.player_x0 = player_floor_x0 + 0.5
        self.player_y0 = player_floor_y0 + 0.5

    def solve_collisions(self):
        """Разрешить коллизии по необходимости."""
        floor_x = floor(self.player.x)
        floor_y = floor(self.player.y)
        if self.lvl_map[floor_y][floor_x] == '1':
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
            if self.lvl_map[floor_y][floor_x] == '1':
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
