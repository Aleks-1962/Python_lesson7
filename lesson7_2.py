""" Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""
from abc import ABC


class Clothes(ABC):



    def __init__(self, in_param):
        self.in_param = in_param



    @property
    def summa_cloth(self):
        return ' '


class Coat(Clothes):
    def summa_cloth(self):
        a = round((self.in_param / 6.5 + 0.5), 1)
        return f'Для пальто требуется - {a} метров ткани'

    def abstract(self):
        return 'пальто'


class Costume(Clothes):
    def summa_cloth(self):
        b = round((2 * self.in_param + 0.3), 1)
        return f'Для пошива костюма нужно: {b} метров ткани'

    def abstract(self):
        return 'костюм'


v = int(input('Введите размер для пальто - '))
h = int(input('Введите рост для костюма - '))

coat = Coat(v)
costume = Costume(h)

print(coat.summa_cloth())
print(costume.summa_cloth())

print(costume.abstract())
print(coat.abstract())
