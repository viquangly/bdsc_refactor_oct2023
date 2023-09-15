
from abc import ABC


class Period(ABC):
    unit = None

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError('value must be of type int')

        if value < 1:
            raise ValueError('value must be >= 1')

        self.value = value

    def __str__(self):
        return f'{self.value}{self.__class__.unit}'


class Week(Period):
    unit = 'w'


class Year(Period):
    unit = 'y'


if __name__ == '__main__':
    week_5 = Week(5)
    str(week_5)

    week_error = Week(-1)

    year_2 = Year(2)
    str(year_2)

    isinstance(year_2, Period)
    isinstance(week_5, Period)
