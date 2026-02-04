"""Конфигурационный скрипт для приложения."""

from math import tan, pi

from engine.settings import VFOV, STEPS_PER_UNIT, L_RENDER

# пути
PATH_ICON = 'res/icon.png'

# рассчитываемые константы
COEFF_TAN = 1 / (2 * tan(pi * VFOV / 360))
RAY_ONE_STEP = 1 / STEPS_PER_UNIT

LIST_DISTS = list(range(0, L_RENDER * STEPS_PER_UNIT))
for i in range(len(LIST_DISTS)):
    LIST_DISTS[i] /= STEPS_PER_UNIT


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
