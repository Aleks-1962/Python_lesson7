"""  Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
 сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
 Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
 обычное (не целочисленное) деление клеток, соответственно.
 В методе деления должно осуществляться округление значения до целого числа.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам. """

class Kletka:
    def __init__(self, kol_vo):
        self.kol_vo = kol_vo

    def __add__(self, other):
        rez = self.kol_vo + other.kol_vo
        return f'Выполняем сложение 2-х клеток - результат: {rez}'

    def __sub__(self, other):
        rez = self.kol_vo - other.kol_vo if (self.kol_vo - other.kol_vo) > 0 else print('Ошибка. меньше 0.')
        return f'Выполняем вычитание 2-х клеток - результат: {rez}'

    def __mul__(self, other):
        rez = self.kol_vo * other.kol_vo
        return f'Выполняем умножение 2-х клеток - результат: {rez}'

    def __truediv__(self, other):
        rez = self.kol_vo // other.kol_vo
        return f'Выполняем деление 2-х клеток - результат: {rez}'

    def make_order(self, in_row):
        row = ''
        for i in range(int(self.kol_vo / in_row)):
            row += f'{"*" * in_row} \\n'
            row += f'{"*" * (self.kol_vo% in_row)}'
        return row

    def __str__(self):
        return ' '


k_r = int(input('Введите размер ячейки - '))
k_c = int(input('Введите размер клетки - '))

cells_row = Kletka(k_r)
cells_cells = Kletka(k_c)

print(cells_cells.make_order(5))
print(cells_cells + cells_row)
print(cells_cells - cells_row)
print(cells_cells * cells_row)
print(cells_cells / cells_row)
print(cells_row.make_order(3))
