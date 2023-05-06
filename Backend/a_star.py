from enum import Enum
from typing import List


class Vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class PixelType(Enum):
    WATER = 100
    FOREST = 10
    ROAD = 5


class Pixel:
    def __init__(self, pos: Vec2, pixel_type: PixelType):
        self.pos = pos
        self.pixel_type = pixel_type


def find_path(pixel_map: List[Pixel], start: Vec2, end: Vec2):
    pass
