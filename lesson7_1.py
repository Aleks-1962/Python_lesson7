""" Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица."""


class Matrix:

    def __init__(self, matr_1, matr_2):
        self.matr_1 = matr_1
        self.matr_2 = matr_2

    def __add__(self, result):
        for i in range(len(matr_1)):
            for j in range(len(matr_1[0])):
                result[i][j] = matr_1[i][j] + matr_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in result]))

    def __str__(self):
        return ''


m = int(input('Для создания матрицы введите число колонок (больше 1): '))
n = int(input('Для создания матрицы введите число строк (больше 1): '))

matr_1 = [[i * j for j in reversed(range(m))] for i in range(n)]
matr_2 = [[j * i for i in range(m)] for j in reversed(range(n))]

m = Matrix.__add__(matr_1, matr_2)

print(matr_1)
print(matr_2)
print(m)
