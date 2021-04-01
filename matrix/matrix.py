class Matrix:
    def __init__(self, matrix_string: str):
        # another solution (functional)
        # [list(map(int, elements.split())) for elements in matrix_string.splitlines()]
        self.matrix = [
            [int(element) for element in elements.split()]
            for elements in matrix_string.splitlines()
        ]

    def row(self, index):
        return self.matrix[index - 1].copy()

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
