"""Модуль с персонажами для движка."""

from math import sin, cos, pi

from engine.settings import PLAYER_CAM_SPEED, PLAYER_SPEED, FPS


_VECTOR_TO_ANGLE = {
    (1, 0): 0,
    (1, 1): 45,
    (0, 1): 90,
    (-1, 1): 135,
    (-1, 0): 180,
    (-1, -1): 225,
    (0, -1): 270,
    (1, -1): 315
}


class Player:
    """Класс игрока."""

    def __init__(self, x0: int | float, y0: int | float,
                 angle0: int | float) -> None:
        """Инициализация экземпляра класса.

        :param x0: начальная координата x
        :type x0: int | float
        :param y0: начальная координата y
        :type y0: int | float
        """
        self.x = x0
        self.y = y0
        self.angle = angle0
        self._speed = PLAYER_SPEED / FPS
        self._cam_speed = PLAYER_CAM_SPEED / FPS

        self._moving_front = False
        self._moving_left = False
        self._moving_back = False
        self._moving_right = False
        self._moving_ccw = False
        self._moving_cw = False
    
    def move(self) -> None:
        """Произвести перемещение и вращение."""
        front_back = self._moving_front - self._moving_back
        left_right = self._moving_left - self._moving_right
        if not (front_back == left_right == 0):
            relative_angle = _VECTOR_TO_ANGLE[(front_back, left_right)]
            cos_angle = cos((self.angle + relative_angle) * pi / 180)
            sin_angle = sin((self.angle + relative_angle) * pi / 180)
            self.x += self._speed * cos_angle
            self.y += -self._speed * sin_angle
        
        ccw_cw = self._moving_ccw - self._moving_cw
        self.angle = (self.angle + ccw_cw * self._cam_speed) % 360
    
    def set_moving_front(self, is_moving: bool) -> None:
        """Установить состояние движения вперед.

        :param is_moving: флаг наличия движения в направлении
        :type is_moving: bool
        """
        self._moving_front = bool(is_moving)
    
    def set_moving_left(self, is_moving: bool) -> None:
        """Установить состояние движения влево.

        :param is_moving: флаг наличия движения в направлении
        :type is_moving: bool
        """
        self._moving_left = bool(is_moving)
    
    def set_moving_back(self, is_moving: bool) -> None:
        """Установить состояние движения назад.

        :param is_moving: флаг наличия движения в направлении
        :type is_moving: bool
        """
        self._moving_back = bool(is_moving)

    def set_moving_right(self, is_moving: bool) -> None:
        """Установить состояние движения вправо.

        :param is_moving: флаг наличия движения в направлении
        :type is_moving: bool
        """
        self._moving_right = bool(is_moving)
    
    def set_moving_ccw(self, is_moving: bool) -> None:
        """Установить состояние вращения против часовой стрелки.

        :param is_moving: флаг наличия движения в направлении
        :type is_moving: bool
        """
        self._moving_ccw = bool(is_moving)
    
    def set_moving_cw(self, is_moving: bool) -> None:
        """Установить состояние вращения по часовой стрелке.

        :param is_moving: флаг наличия движения в направлении
        :type is_moving: bool
        """
        self._moving_cw = bool(is_moving)


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
