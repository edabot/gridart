import random
from PIL import Image, ImageDraw
import svgwrite
from cell_random_cos import CellRandomCos
from grid import Grid

class GridRandomCos(Grid):
    def __init__(self, rows, columns, max_size, min_size):
        self.rows, self.columns, self.max_size, self.min_size = rows, columns, max_size, min_size
        self.grid = self.prepare_grid()

    def prepare_grid(self):
        grid_array = []
        for row in range(self.rows):
            row_array = []
            for column in range(self.columns):
                row_array.append(CellRandomCos(row, column, self.max_size, self.min_size))
            grid_array.append(row_array)
        return grid_array


    def to_svg(self, cell_size = 50):

        top_offset = 20
        left_offset = 20
        img_width = cell_size * self.columns
        img_height = cell_size * self.rows
        dwg = svgwrite.Drawing('./export/grid_random_cos.svg')

        for cell in self.each_cell():
            x1 = cell.column * cell_size + top_offset
            y1 = cell.row * cell_size + left_offset

            dwg.add(dwg.circle(center=(x1, y1), r=cell.size, stroke='none', fill='purple', opacity='0.5'))

        dwg.save()
