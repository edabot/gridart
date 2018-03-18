import random
from cell import Cell

class CellRandom(Cell):
    def __init__(self, row, column, max_size = 20, min_size = 0):
        Cell.__init__(self, row, column)
        self.size = random.randrange(min_size, max_size) / 2
