import random
from cell import Cell
import math

class CellRandomCos(Cell):
    def __init__(self, row, column, max_size=20, min_size = 0):
        Cell.__init__(self, row, column)
        size_range = max_size - min_size
        rand180 = random.randrange(180)
        self.size = min_size + (math.cos(math.radians(rand180)) * size_range + size_range) / 2
