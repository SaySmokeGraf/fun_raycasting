"""Модуль с картой."""


class MapReadingException(Exception):
    """Исключение при чтении карты."""
    pass


class MapCellTypes:
    """Типы клеток в карте."""
    EMPTY = 0
    WALL = 1

    ALL_TYPES_SET = {0, 1}


class Map:
    """Класс карты."""

    def __init__(self, map_scheme: str, default_value: int = 0) -> None:
        """Инициализация экземпляра класса.

        :param map_scheme: карта-схема уровня
        :type map_scheme: str
        :param default_value: стандартное значение клетки, по умолчанию 0
        :type default_value: int
        """
        self._default_value = default_value
        self._read_map(map_scheme)
        self._check_read_data()

    def _read_map(self, map_scheme: str) -> None:
        """Прочитать карту.

        :param map_scheme: карта-схема уровня
        :type map_scheme: str
        """
        temp_map = map_scheme.splitlines()

        self._map = []
        self._x_max = 0
        self._y_max = 0
        for line in temp_map:
            if line:
                line = list(map(int, line))
                self._map.append(line)
                self._y_max += 1
                self._x_max = max(self._x_max, len(line) - 1)
    
    def _check_read_data(self) -> None:
        """Проверка подгруженных данных из файла уровня.

        :raises MapReadingException: при неверном стандартном значении клетки
        :raises MapReadingException: при неверной форме карты
        :raises MapReadingException: при неверном значении клетки на карте
        """
        if self._default_value not in MapCellTypes.ALL_TYPES_SET:
            exc_msg = 'Неверное стандартное значение клетки!'
            raise MapReadingException(exc_msg)
        
        for y in range(len(self._map)):
            line = self._map[y]
            if len(line) != self._x_max + 1:
                exc_msg = f'Неверная форма карты (строка {y})!'
                raise MapReadingException(exc_msg)
            
            for x in range(len(line)):
                if line[x] not in MapCellTypes.ALL_TYPES_SET:
                    exc_msg = f'Неверное значение клетки [{x}, {y}] на карте!'
                    raise MapReadingException(exc_msg)
    
    def get(self, x: int, y: int) -> int:
        """Получить значение по координатам.

        :param x: координата x
        :type x: int
        :param y: координата y
        :type y: int

        :return: значение по координатам
        :rtype: int
        """
        if self._x_max >= x >= 0 and self._y_max >= y >= 0:
            return self._map[y][x]
        else:
            return self._default_value


if __name__ == "__main__":
    print(__doc__)
    input('Введите Enter, чтобы выйти.')
