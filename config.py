"""Конфигурационный скрипт."""

from math import tan, pi


# разрешение
H_RES = 600             # [пиксели]
V_RES = 400             # [пиксели]

# отрисовка
FPS = 60                # [1/с]
L_RENDER = 5            # [клетки]
STEPS_PER_UNIT = 20     # [шаги/клетка]
FOV = 90                # [градусы]
VFOV = 60               # [градусы]

# параметры игрока
PHI_START = 0           # [градусы]
PLAYER_SPEED = 1.0      # [клетки/с]
PLAYER_CAM_SPEED = 90   # [градусы/с]

# пути
PATH_ICON = 'res/icon.png'
PATH_MAP = 'res/map.txt'


class Direct():
    """Константы углов в градусах по направлениям."""
    FRONT = 0
    LEFT = 90
    RIGHT = -90
    BACK = 180


# рассчитываемые константы
COEFF_TAN = 1 / (2 * tan(pi * VFOV / 360))
RAY_ONE_STEP = 1 / STEPS_PER_UNIT


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
