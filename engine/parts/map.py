"""Модуль с картой."""


class Map:
    """Класс карты."""

    def __init__(self, map_scheme: str):
        """Инициализация экземпляра класса."""
        self._read_map(map_scheme)

    def _read_map(self, map_scheme: str) -> None:
        """Прочитать карту."""
        temp_map = map_scheme.splitlines()

        self._map = []
        for line in temp_map:
            if line:
                line = list(map(int, line))
                self._map.append(line)

        self.y_max = len(self._map)
        self.x_max = len(self._map[0])
    
    def get_cell(self, x, y):
        return self._map[y][x]


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
