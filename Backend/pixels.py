from enum import Enum


class Vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class PixelType(Enum):
    NONE = 1000
    BORDER = 100000
    WATER = 6000
    FOREST = 2000
    ROAD = 10


class Pixel:
    def __init__(self, pos: Vec2, pixel_type: PixelType):
        self.pos = pos
        self.pixel_type = pixel_type

    def __str__(self):
        if self.pixel_type == PixelType.NONE:
            return ' '
        elif self.pixel_type == PixelType.BORDER:
            return 'B'
        elif self.pixel_type == PixelType.WATER:
            return 'W'
        elif self.pixel_type == PixelType.FOREST:
            return 'F'
        elif self.pixel_type == PixelType.ROAD:
            return 'R'

    def __repr__(self):
        if self.pixel_type == PixelType.NONE:
            return ' '
        elif self.pixel_type == PixelType.BORDER:
            return 'B'
        elif self.pixel_type == PixelType.WATER:
            return 'W'
        elif self.pixel_type == PixelType.FOREST:
            return 'F'
        elif self.pixel_type == PixelType.ROAD:
            return 'R'
        # return f'<({self.pos.x}, {self.pos.y}) {self.pixel_type.name}>'