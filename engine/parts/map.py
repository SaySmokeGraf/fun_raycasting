"""Модуль с картой."""


class Map:
    """Класс карты."""

    def __init__(self, map_scheme: str) -> None:
        """Инициализация экземпляра класса.

        :param map_scheme: карта-схема уровня
        :type map_scheme: str
        """
        self._read_map(map_scheme)

    def _read_map(self, map_scheme: str) -> None:
        """Прочитать карту.

        :param map_scheme: карта-схема уровня
        :type map_scheme: str
        """
        temp_map = map_scheme.splitlines()

        self._map = []
        for line in temp_map:
            if line:
                line = list(map(int, line))
                self._map.append(line)
    
    def get(self, x: int, y: int) -> int:
        """Получить значение по координатам.

        :param x: координата x
        :type x: int
        :param y: координата y
        :type y: int

        :return: значение по координатам
        :rtype: int
        """
        return self._map[y][x]


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
