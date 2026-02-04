"""Модуль с классом приложения."""

import pygame

from threading import Thread

from engine.app_config import PATH_ICON
from engine.settings import H_RES, V_RES, FPS
from engine.parts.scene import Scene
from engine.parts.drawer import Drawer
from engine.parts.map import Map
from engine.parts.characters import Player


class DrawingThread(Thread):
    """Поток отрисовки."""

    def __init__(self, screen: pygame.Surface, level_map: Map,
                 player: Player) -> None:
        """Инициализация экземпляра класса.

        :param screen: экран для отрисовки
        :type screen: Surface
        :param level_map: карта уровня
        :type level_map: Map
        :param player: игрок
        :type player: Player
        """
        super().__init__()
        self.is_running = True

        self._drawer = Drawer(screen)
        self._level_map = level_map
        self._player = player
    
    def run(self) -> None:
        """Основной цикл потока."""
        while self.is_running:
            self._drawer.upd_screen(self._player.x, self._player.y,
                                    self._player.angle, self._level_map)


class App:
    """Класс приложения."""

    def __init__(self) -> None:
        """Инициализация экземпляра класса."""
        pygame.init()
        self._is_running = True
        self._clock = pygame.time.Clock()
        
        screen = pygame.display.set_mode((H_RES, V_RES))
        pygame.display.set_caption('Test raycasting')
        pygame.display.set_icon(pygame.image.load(PATH_ICON))

        self._scene = Scene()
        self._drawing_thread = DrawingThread(screen, self._scene.map,
                                             self._scene.player)
        self._drawing_thread.start()

    def run(self) -> None:
        """Запуск основного рабочего цикла приложения."""
        while self._is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
                    self._drawing_thread.is_running = False
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:
                    flag_active = True
                elif event.type == pygame.KEYUP:
                    flag_active = False
                else:
                    continue
                
                if event.key == pygame.K_w:
                    self._scene.player.set_moving_front(flag_active)
                elif event.key == pygame.K_a:
                    self._scene.player.set_moving_left(flag_active)
                elif event.key == pygame.K_s:
                    self._scene.player.set_moving_back(flag_active)
                elif event.key == pygame.K_d:
                    self._scene.player.set_moving_right(flag_active)
                elif event.key == pygame.K_LEFT:
                    self._scene.player.set_moving_ccw(flag_active)
                elif event.key == pygame.K_RIGHT:
                    self._scene.player.set_moving_cw(flag_active)
            
            if self._is_running:
                self._scene.player.move()
                self._scene.solve_collisions()
                self._clock.tick(FPS)


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
