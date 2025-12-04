"""Главный скрипт."""

import pygame

from math import floor

from config import *
from src.objects import *


class App:
    def __init__(self):
        pygame.init()
        self.flag_running = True
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((H_RES, V_RES))
        pygame.display.set_caption('Test raycasting')
        pygame.display.set_icon(pygame.image.load(PATH_ICON))

        self.level = Level()
        self.player = Player(self.level.player_x0, self.level.player_y0)

    def run(self):
        while self.flag_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag_running = False
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:
                    flag_active = True
                elif event.type == pygame.KEYUP:
                    flag_active = False
                else:
                    continue
                
                if event.key == pygame.K_w:
                    self.player.moving_front = flag_active
                elif event.key == pygame.K_a:
                    self.player.moving_left = flag_active
                elif event.key == pygame.K_s:
                    self.player.moving_back = flag_active
                elif event.key == pygame.K_d:
                    self.player.moving_right = flag_active
                elif event.key == pygame.K_LEFT:
                    self.player.moving_cam_ccw = flag_active
                elif event.key == pygame.K_RIGHT:
                    self.player.moving_cam_cw = flag_active
            
            self.player.move()
            self._solve_collisions()
            self._upd_screen()
            self.clock.tick(FPS)
    
    def _upd_screen(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, H_RES, V_RES))
        one_step = FOV / H_RES
        max_angle = self.player.phi + FOV / 2
        floor_x_old, floor_y_old, _ = self._send_ray(self.player.x,
                                            self.player.y,
                                            phi=max_angle - 0 * one_step)
        for i in range(H_RES):
            floor_x, floor_y, r = self._send_ray(self.player.x, self.player.y, 
                                                 max_angle - i * one_step)
            
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

            pygame.draw.aaline(self.screen, line_color, 
                               (i, int((V_RES - line_len) / 2)),
                               (i, int((V_RES + line_len) / 2)))
            
        pygame.display.update()

    def _send_ray(self, x, y, phi):
        one_step_x = RAY_ONE_STEP * cos(phi * pi / 180)
        one_step_y = RAY_ONE_STEP * sin(phi * pi / 180)

        for r in LIST_DISTS:
            x += one_step_x
            y -= one_step_y
            floor_x = floor(x)
            floor_y = floor(y)

            if self.level.lvl_map[floor_y][floor_x] == '1':
                return floor_x, floor_y, r
            
        return None, None, L_RENDER
    
    def _solve_collisions(self):
        floor_x = floor(self.player.x)
        floor_y = floor(self.player.y)
        if self.level.lvl_map[floor_y][floor_x] == '1':
            dists = {'left': self.player.x - floor_x,
                     'right': floor_x + 1 - self.player.x,
                     'up': self.player.y - floor_y,
                     'down': floor_y + 1 - self.player.y}
            key_min = min(dists, key=dists.get)
            
            if key_min == 'left':
                self.player.x = floor_x
                del dists['left']
            elif key_min == 'right':
                self.player.x = floor_x + 1
                del dists['right']
            elif key_min == 'up':
                self.player.y = floor_y
                del dists['up']
            elif key_min == 'down':
                self.player.y = floor_y + 1
                del dists['down']

            floor_x = floor(self.player.x)
            floor_y = floor(self.player.y)
            if self.level.lvl_map[floor_y][floor_x] == '1':
                key_min = min(dists, key=dists.get)

                if key_min == 'left':
                    self.player.x = floor_x
                elif key_min == 'right':
                    self.player.x = floor_x + 1
                elif key_min == 'up':
                    self.player.y = floor_y
                elif key_min == 'down':
                    self.player.y = floor_y + 1


if __name__ == '__main__':
    app = App()
    app.run()
