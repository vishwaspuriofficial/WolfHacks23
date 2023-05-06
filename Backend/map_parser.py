from PIL import Image
from pixels import Pixel, Vec2, PixelType


def init_empty_map(width: int, height: int) -> list:
    return [[Pixel(Vec2(x, y), PixelType.NONE) for y in range(height)] for x in range(width)]


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
                pixel = pix[i, j]

                r, g, b = pixel
                if r == 255 and g == 255 and b == 255:
                    pt = PixelType.NONE
                else:
                    pt = pixel_type
                self.pixels[i][j] = Pixel(Vec2(i, j), pt)
