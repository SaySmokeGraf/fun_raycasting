"""Raycasting app config script."""

from math import tan, pi


H_RES = 600             # [pixels]
V_RES = 400             # [pixels]
FPS = 60                # [1/s]
L_RENDER = 5            # [cell]
STEPS_PER_UNIT = 20     # [step/cell]

FOV = 90                # [grad]
VFOV = 60               # [grad]
PHI_START = 0           # [grad]
PLAYER_SPEED = 1.0      # [cell/sec]
PLAYER_CAM_SPEED = 90   # [grad/sec]

PATH_ICON = 'res/icon.png'
PATH_MAP = 'res/map.txt'

class Direct():
    FRONT = 0
    LEFT = 90
    RIGHT = -90
    BACK = 180

# countable consts
COEFF_TAN = 1 / (2 * tan(pi * VFOV / 360))
RAY_ONE_STEP = 1 / STEPS_PER_UNIT
