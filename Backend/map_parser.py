from PIL import Image
from pixels import Pixel, Vec2, PixelType


def init_empty_map(width: int, height: int) -> list:
    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(Pixel(Vec2(x, y), PixelType.NONE))
        pixels.append(row)
    return pixels



class MapParser:
    def __init__(self, width, height):
        self.pixels = init_empty_map(width, height)
        self.pixels_uniq = set()

    def parse_feature(self, filename, pixel_type: PixelType):
        im = Image.open(filename)
        pix = im.load()
        xy = im.size
        x, y = xy
        for i in range(x):
            for j in range(y):
                r, g, b = pix[i, j]

                if r == 255 and g == 255 and b == 255:
                    continue
                else:
                    self.pixels[i][j] = Pixel(Vec2(i, j), pixel_type)
