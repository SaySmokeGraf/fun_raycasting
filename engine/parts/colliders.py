"""Модуль с коллайдерами."""

from __future__ import annotations
from math import floor


class CollisionException(Exception):
    """Исключение при расчете коллизий."""
    pass


class Point:
    """Класс точки."""

    def __init__(self, x: float, y: float) -> None:
        """Инициализация экземпляра класса.

        :param x: координата x
        :type x: float
        :param y: координата y
        :type y: float
        """
        self.x = x
        self.y = y
        self._is_collided = False
    
    @property
    def is_collided(self) -> bool:
        """Флаг наличия коллизии."""
        return self._is_collided
    
    @is_collided.setter
    def is_collided(self, collided: bool) -> None:
        """Сеттер для флага наличия коллизии."""
        self._is_collided = collided


class SquareCollider:
    """Класс квадратного коллайдера."""

    def __init__(self, x: float, y: float, side: float) -> None:
        """Инициализация экземпляра класса.

        :param x: координата x центра коллайдера
        :type x: float
        :param y: координата y центра коллайдера
        :type y: float
        :param side: сторона квадрата
        :type side: float
        """
        self._x = x
        self._y = y
        self._points = (Point(x - side / 2, y - side / 2),
                        Point(x + side / 2, y - side / 2),
                        Point(x + side / 2, y + side / 2),
                        Point(x - side / 2, y + side / 2))
    
    def solve_collisions(self) -> None:
        """Решить коллизии.

        :raises CollisionException: при полном пересечении коллайдера с другими
        объектами
        :raises CollisionException: при неизвестном значении суммарного
        параметра коллизии
        """
        is_collision = [self._points[i].is_collided for i in range(4)]
        sum_param = sum(is_collision)

        match sum_param:
            case 0:
                return
            case 1:
                self._solve_1_point(is_collision)
            case 2:
                self._solve_2_points(is_collision)
            case 3:
                self._solve_3_points(is_collision)
            case 4:
                exc_msg = 'Полное пересечение c другим объектом!'
                raise CollisionException(exc_msg)
            case _:
                exc_msg = 'Неизвестное значение суммарного параметра коллизии!'
                raise CollisionException(exc_msg)
            
        for point in self._points:
            point.is_collided = False
            
    def _solve_1_point(self, is_collision: tuple[bool]) -> None:
        """Решить коллизию по 1 точке.

        :param is_collision: список флагов коллизии для точек
        :type is_collision: tuple[bool]
        """
        point = self._points[is_collision.index(True)]
        floor_x = floor(point.x)
        floor_y = floor(point.y)
        dists = {'L': point.x - floor_x,
                 'R': floor_x + 1 - point.x,
                 'U': point.y - floor_y,
                 'D': floor_y + 1 - point.y}
        key_min = min(dists, key=dists.get)

        match key_min:
            case 'L':
                self.move(-dists['L'], 0)
            case 'R':
                self.move(dists['R'], 0)
            case 'U':
                self.move(0, -dists['U'])
            case 'D':
                self.move(0, dists['D'])

    def _solve_2_points(self, is_collision: tuple[bool]) -> None:
        """Решить коллизию по 2 точкам.

        :param is_collision: список флагов коллизии для точек
        :type is_collision: tuple[bool]
        """
        if is_collision[0] == is_collision[2]:
            exc_msg = 'Неизвестная схема точек коллизии!'
            raise CollisionException(exc_msg)
        
        if is_collision[0] is True:
            point = self._points[0]
            if is_collision[1] is True:
                self.move(0, floor(point.y) + 1 - point.y)
            else:
                self.move(floor(point.x) + 1 - point.x, 0)

        else:
            point = self._points[2]
            if is_collision[1] is True:
                self.move(floor(point.x) - point.x, 0)
            else:
                self.move(0, floor(point.y) - point.y)

    def _solve_3_points(self, is_collision: tuple[bool]) -> None:
        """Решить коллизию по 3 точкам.

        :param is_collision: список флагов коллизии для точек
        :type is_collision: tuple[bool]
        """
        ind = is_collision.index(False)
        outer_point = self._points[ind]
        inner_point = self._points[ind - 2]
        
        if outer_point.x > inner_point.x:
            diff_x = floor(outer_point.x) - inner_point.x
        else:
            diff_x = floor(inner_point.x) - inner_point.x
        
        if outer_point.y > inner_point.y:
            diff_y = floor(outer_point.y) - inner_point.y
        else:
            diff_y = floor(inner_point.y) - inner_point.y
            
        self.move(diff_x, diff_y)

    def move(self, x: float, y: float) -> None:
        """Сдвинуть коллайдер.

        :param x: смещение по координате x
        :type x: float
        :param y: смещение по координате y
        :type y: float
        """
        self._x += x
        self._y += y
        for point in self._points:
            point.x += x
            point.y += y

    @property
    def x(self) -> float:
        """Координата x геометрического центра коллайдера."""
        return self._x
    
    @property
    def y(self) -> float:
        """Координата y геометрического центра коллайдера."""
        return self._y
    
    @property
    def points(self) -> tuple[Point]:
        """Значащие точки коллайдера."""
        return self._points


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
