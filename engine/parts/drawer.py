"""Модуль с отрисовщиком."""

from math import floor, pi, sin, cos

import pygame

from config import *


class Drawer:
    """Класс отрисовщика."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Инициализация экземпляра класса.

        :param screen: экран для отрисовки
        :type screen: Surface
        """
        self._screen = screen

    def upd_screen(self, x: int | float, y: int | float,
                    phi: int | float, map: list[list[str]]) -> None:
        """Обновить экран."""
        pygame.draw.rect(self._screen, (0, 0, 0), (0, 0, H_RES, V_RES))
        one_step = FOV / H_RES
        max_angle = phi + FOV / 2
        floor_x_old, floor_y_old, _ = self._send_ray(x, y,
                                                 max_angle - 0 * one_step,
                                                 map)
        for i in range(H_RES):
            floor_x, floor_y, r = self._send_ray(x, y, 
                                                 max_angle - i * one_step,
                                                 map)
            
            if floor_x != floor_x_old or floor_y != floor_y_old:
                line_color = (0, 0, 0)
                floor_x_old = floor_x
                floor_y_old = floor_y
            else:
                c_temp = floor(255 - 255 * r / L_RENDER)
                line_color = (c_temp, c_temp, c_temp)
            
            if r == 0:
                coeff = 1
            else:
                coeff = COEFF_TAN / r
                if coeff > 1: coeff = 1
            line_len = coeff * V_RES

            pygame.draw.aaline(self._screen, line_color, 
                               (i, int((V_RES - line_len) / 2)),
                               (i, int((V_RES + line_len) / 2)))
            
        pygame.display.update()

    def _send_ray(self, x: int | float, y: int | float,
                  phi: int | float, map: list[list[str]]) -> None:
        one_step_x = RAY_ONE_STEP * cos(phi * pi / 180)
        one_step_y = RAY_ONE_STEP * sin(phi * pi / 180)

        for r in LIST_DISTS:
            x += one_step_x
            y -= one_step_y
            floor_x = floor(x)
            floor_y = floor(y)

            if map[floor_y][floor_x] == '1':
                return floor_x, floor_y, r
            
        return None, None, L_RENDER


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
