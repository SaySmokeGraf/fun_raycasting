"""Модуль с объектами для проекта."""

from math import sin, cos, pi
from src.config import *


LIST_DISTS = list(range(0, L_RENDER*STEPS_PER_UNIT))
for i in range(len(LIST_DISTS)):
    LIST_DISTS[i] /= STEPS_PER_UNIT


class Player(object):
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
        self.phi = PHI_START
        self.v = PLAYER_SPEED/FPS
        self.cam_v = PLAYER_CAM_SPEED/FPS

        self.moving_front = False
        self.moving_left = False
        self.moving_back = False
        self.moving_right = False
        self.moving_cam_cw = False
        self.moving_cam_ccw = False
    
    def move(self):
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
    
    def _move_onedir(self, dphi=0):
        self.x += self.v*cos((self.phi+dphi)*pi/180)
        self.y += -self.v*sin((self.phi+dphi)*pi/180)

class Level(object):
    def __init__(self):
        self._read_data_from_map()
    
    def _read_data_from_map(self):
        f = open(PATH_MAP, 'r')
        self.lvl_map = f.read().splitlines()
        f.close()
        
        for i in range(len(self.lvl_map)):
            self.lvl_map[i] = [square for square in self.lvl_map[i]]
            if 'x' in self.lvl_map[i]:
                player_floor_y0 = i
                player_floor_x0 = self.lvl_map[i].index('x')
                self.lvl_map[player_floor_y0][player_floor_x0] = '0'

        self.y_max = len(self.lvl_map)
        self.x_max = len(self.lvl_map[0])
        self.player_x0 = player_floor_x0 + 0.5
        self.player_y0 = player_floor_y0 + 0.5


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
