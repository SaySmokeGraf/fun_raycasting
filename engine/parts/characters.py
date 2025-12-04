"""Модуль с объектами для движка."""

from math import sin, cos, pi

from config import *


class Player:
    """Класс игрока."""

    def __init__(self, x0: int | float, y0: int | float) -> None:
        """Инициализация экземпляра класса.

        :param x0: начальная координата x
        :type x0: int | float
        :param y0: начальная координата y
        :type y0: int | float
        """
        self.x = x0
        self.y = y0
        self.phi = PHI_START
        self.v = PLAYER_SPEED / FPS
        self.cam_v = PLAYER_CAM_SPEED / FPS

        self.moving_front = False
        self.moving_left = False
        self.moving_back = False
        self.moving_right = False
        self.moving_cam_cw = False
        self.moving_cam_ccw = False
    
    def move(self) -> None:
        """Произвести перемещение и вращение."""
        if self.moving_front:
            self._move_onedir(dphi=Direct.FRONT)
        if self.moving_left:
            self._move_onedir(dphi=Direct.LEFT)
        if self.moving_back:
            self._move_onedir(dphi=Direct.BACK)
        if self.moving_right:
            self._move_onedir(dphi=Direct.RIGHT)
        if self.moving_cam_cw:
            self.phi -= self.cam_v
            if self.phi < 0: self.phi += 360
        if self.moving_cam_ccw:
            self.phi += self.cam_v
            if self.phi > 360: self.phi -= 360
    
    def _move_onedir(self, dphi: int | float = 0) -> None:
        """Перемещение в одном направлении.

        :param dphi: угол направления движения относительно направления взгляда
        игрока в градусах, по умолчанию 0
        :type dphi: int | float
        """
        self.x += self.v * cos((self.phi + dphi) * pi / 180)
        self.y += -self.v * sin((self.phi + dphi) * pi / 180)


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
