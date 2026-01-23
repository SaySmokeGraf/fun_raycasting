"""Модуль с классом приложения."""

import pygame

from engine.app_config import PATH_ICON
from engine.settings import H_RES, V_RES, FPS
from engine.parts.scene import Scene
from engine.parts.drawer import Drawer


class App:
    """Класс приложения."""

    def __init__(self) -> None:
        """Инициализация экземпляра класса."""
        pygame.init()
        self._flag_running = True
        self._clock = pygame.time.Clock()
        
        screen = pygame.display.set_mode((H_RES, V_RES))
        pygame.display.set_caption('Test raycasting')
        pygame.display.set_icon(pygame.image.load(PATH_ICON))

        self._scene = Scene()
        self._drawer = Drawer(screen)

    def run(self) -> None:
        """Запуск основного рабочего цикла приложения."""
        while self._flag_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._flag_running = False
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:
                    flag_active = True
                elif event.type == pygame.KEYUP:
                    flag_active = False
                else:
                    continue
                
                if event.key == pygame.K_w:
                    self._scene.player.moving_front = flag_active
                elif event.key == pygame.K_a:
                    self._scene.player.moving_left = flag_active
                elif event.key == pygame.K_s:
                    self._scene.player.moving_back = flag_active
                elif event.key == pygame.K_d:
                    self._scene.player.moving_right = flag_active
                elif event.key == pygame.K_LEFT:
                    self._scene.player.moving_cam_ccw = flag_active
                elif event.key == pygame.K_RIGHT:
                    self._scene.player.moving_cam_cw = flag_active
            
            if self._flag_running:
                self._scene.player.move()
                x, y = self._scene.player.x, self._scene.player.y
                phi = self._scene.player.phi
                level_map = self._scene.map

                self._scene.solve_collisions()
                self._drawer.upd_screen(x, y, phi, level_map)
                self._clock.tick(FPS)


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
