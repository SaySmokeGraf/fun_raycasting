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
        """Решить коллизии по необходимости."""
        points = self._player.collider.points
        for point in points:
            cell = self._map.get(floor(point.x), floor(point.y))
            if cell == MapCellTypes.WALL:
                point.is_collided = True
        self._player.collider.solve_collisions()
    
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
