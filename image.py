from PIL import Image
import imageio
import svgwrite
import math

basewidth = 100
img = Image.open('source_dog.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('source_100.jpg')

im = imageio.imread('source_100.jpg')

rows = len(im)
cols = len(im[0])

def make_circle(value, center, offset, color, dwg):
    dwg.add(dwg.circle(center=(center[0] + offset[0], center[1] + offset[1]), r=value/2, stroke='none', fill=color, opacity='1'))

def make_circles(row, col, rgb, dwg, cell_size):
    center = [col * cell_size, row * cell_size]
    shift = cell_size / 4
    make_circle(math.sqrt(int(rgb[0])), center, [-shift, 0], "#f00", dwg)
    make_circle(math.sqrt(int(rgb[1]))/1.4, center, [shift, 0], "#0f0", dwg)
    make_circle(math.sqrt(int(rgb[1]))/1.4, center, [-shift, shift * 2], "#0f0", dwg)
    make_circle(math.sqrt(int(rgb[2])), center, [shift, shift * 2], "#00f", dwg)


def to_svg(cell_size = 30):

    top_offset = 20
    left_offset = 20

    dwg = svgwrite.Drawing('./export/grid.svg')
    dwg.add(dwg.rect(insert=(0, 0), size=(basewidth * cell_size,hsize * cell_size), rx=None, ry=None, fill='black'))

    for row in range(rows):
        for col in range(cols):
            make_circles(row, col, im[row][col], dwg, cell_size)

    dwg.save()
to_svg()
