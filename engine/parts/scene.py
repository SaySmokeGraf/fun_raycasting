"""Модуль со сценой."""

from math import floor

from engine.parts.characters import Player
from engine.parts.map import Map, MapCellTypes
from levels.level import (PLAYER_ANGLE0, PLAYER_X0, PLAYER_Y0,
                          DEFAULT_CELL_VALUE, MAP_SCHEME)


class ObjectsPlacementException(Exception):
    """Исключение расположения объектов на сцене."""
    pass


class Scene:
    """Класс сцены."""

    def __init__(self) -> None:
        """Инициализация экземпляра класса."""
        self._map = Map(MAP_SCHEME, DEFAULT_CELL_VALUE)
        self._player = Player(PLAYER_X0, PLAYER_Y0, PLAYER_ANGLE0)
        self._check_objects_placement()
    
    def _check_objects_placement(self) -> None:
        """Проверить расположение объектов на сцене.

        :raises ObjectsPlacementException: при неверном расположении игрока
        """
        player_cell = self._map.get(floor(PLAYER_X0), floor(PLAYER_Y0))
        if player_cell == MapCellTypes.WALL:
            exc_msg = 'Неверное расположение игрока!'
            raise ObjectsPlacementException(exc_msg)

    def solve_collisions(self):
        """Разрешить коллизии по необходимости."""
        floor_x = floor(self._player.x)
        floor_y = floor(self._player.y)
        if self._map.get(floor_x, floor_y) == MapCellTypes.WALL:
            dists = {'left': self._player.x - floor_x,
                     'right': floor_x + 1 - self._player.x,
                     'up': self._player.y - floor_y,
                     'down': floor_y + 1 - self._player.y}
            key_min = min(dists, key=dists.get)
            
            if key_min == 'left':
                self._player.x = floor_x
                del dists['left']
            elif key_min == 'right':
                self._player.x = floor_x + 1
                del dists['right']
            elif key_min == 'up':
                self._player.y = floor_y
                del dists['up']
            elif key_min == 'down':
                self._player.y = floor_y + 1
                del dists['down']

            floor_x = floor(self._player.x)
            floor_y = floor(self._player.y)
            if self._map.get(floor_x, floor_y) == MapCellTypes.WALL:
                key_min = min(dists, key=dists.get)

                if key_min == 'left':
                    self._player.x = floor_x
                elif key_min == 'right':
                    self._player.x = floor_x + 1
                elif key_min == 'up':
                    self._player.y = floor_y
                elif key_min == 'down':
                    self._player.y = floor_y + 1
    
    @property
    def map(self) -> Map:
        """Карта уровня."""
        return self._map
    
    @property
    def player(self) -> Player:
        """Игрок."""
        return self._player


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
