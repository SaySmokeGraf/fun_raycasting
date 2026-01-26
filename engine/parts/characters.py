"""Модуль с объектами для движка."""

from math import sin, cos, pi

from engine.app_config import Direct
from engine.settings import PLAYER_CAM_SPEED, PLAYER_SPEED, FPS


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

        self.moving_front = False
        self.moving_left = False
        self.moving_back = False
        self.moving_right = False
        self.moving_cam_cw = False
        self.moving_cam_ccw = False
    
    def move(self) -> None:
        """Произвести перемещение и вращение."""
        if self.moving_front:
            self._move_onedir(dangle=Direct.FRONT)
        if self.moving_left:
            self._move_onedir(dangle=Direct.LEFT)
        if self.moving_back:
            self._move_onedir(dangle=Direct.BACK)
        if self.moving_right:
            self._move_onedir(dangle=Direct.RIGHT)
        if self.moving_cam_cw:
            self.angle -= self._cam_speed
            if self.angle < 0: self.angle += 360
        if self.moving_cam_ccw:
            self.angle += self._cam_speed
            if self.angle > 360: self.angle -= 360
    
    def _move_onedir(self, dangle: int | float = 0) -> None:
        """Перемещение в одном направлении.

        :param dangle: угол направления движения относительно направления взгляда
        игрока в градусах, по умолчанию 0
        :type dangle: int | float
        """
        self.x += self._speed * cos((self.angle + dangle) * pi / 180)
        self.y += -self._speed * sin((self.angle + dangle) * pi / 180)


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
