from PIL import Image
import imageio
import svgwrite
import math
from functools import reduce

basewidth = 50
img = Image.open('california.png').convert('RGB')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('source_50.jpg')

im = imageio.imread('source_50.jpg')

rows = len(im)
cols = len(im[0])

def average_of_colors(rgb, max_height):
    average = reduce( (lambda x, y: int(x) + int(y)), rgb ) / len(rgb)
    return average * max_height / 255

def make_line(row_array, row_number, dwg, cell_size, max_height):
    h_base = (row_number + 1) * cell_size
    points = len(row_array)
    point_array = [[cell_size,h_base + max_height]]
    for point in range(points):
        point_array.append([(point + 1) * cell_size, h_base + average_of_colors(row_array[point], max_height)])
    point_array.append([(points + 2) * cell_size,h_base + max_height])
    dwg.add(dwg.polyline(point_array, fill="white", stroke="black", stroke_width=5))


def to_svg(cell_size = 30, max_height = 30):

    dwg = svgwrite.Drawing('./export/image_lines.svg')

    for row in range(rows):
        make_line(im[row], row, dwg, cell_size, max_height)

    dwg.save()

to_svg(30, 120)
