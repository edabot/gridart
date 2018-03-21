from PIL import Image
import imageio
import svgwrite
import math
from functools import reduce

basewidth = 40
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
    return int(average * max_height / 255)

def make_line(row_array, row_number, dwg, cell_size, max_height):
    h_base = (row_number + 1) * cell_size
    points = len(row_array)
    line_max = h_base + max_height
    point_string = "M " + str(cell_size) + ' ' + str(h_base + average_of_colors(row_array[1], max_height))
    for point in range(1,points):
        control_x = str((point + 1.5) * cell_size)
        new_x = str((point + 2) * cell_size)
        new_y = h_base + average_of_colors(row_array[point], max_height)
        old_y = h_base + average_of_colors(row_array[point - 1], max_height)
        if new_y > old_y:
            point_string += ' S ' + control_x + ' ' + str(old_y) +  ' ' + new_x + ' ' + str(new_y)
        else:
            point_string += ' S ' + control_x + ' ' + str(new_y) +  ' ' + new_x + ' ' + str(new_y)
    dwg.add(dwg.path(d=point_string, fill="white", stroke="black", stroke_width=5))


def to_svg(cell_size = 30, max_height = 30):

    dwg = svgwrite.Drawing('./export/image_lines.svg')
    for row in range(rows):
        make_line(im[row], row, dwg, cell_size, max_height)

    dwg.save()

to_svg(20, 50)
