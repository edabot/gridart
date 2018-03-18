from grid_random import GridRandom
from grid_random_cos import GridRandomCos

grid = GridRandom(10,10, 40)
grid.to_svg()
grid = GridRandomCos(40,40, 25, 5)
grid.to_svg()
