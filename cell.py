import random

class Cell:
    def __init__(self, row, column):
        self.row, self.column = row, column
        self.size = random.randrange(40)
