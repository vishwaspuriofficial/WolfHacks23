from enum import Enum


class Vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class PixelType(Enum):
    NONE = 0
    BORDER = 100000
    WATER = 100
    FOREST = 10
    ROAD = 5


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

    def __repr__(self):
        if self.pixel_type == PixelType.NONE:
            return ' '
        elif self.pixel_type == PixelType.BORDER:
            return 'B'
        elif self.pixel_type == PixelType.WATER:
            return 'W'
        elif self.pixel_type == PixelType.FOREST:
            return 'F'
        # return f'<({self.pos.x}, {self.pos.y}) {self.pixel_type.name}>'