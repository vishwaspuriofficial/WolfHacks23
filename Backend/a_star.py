from enum import Enum
from typing import List
from pixels import Pixel, Vec2, PixelType
from map_parser import MapParser


def get_pixel_map():
    mp = MapParser(1920, 1080)
    mp.parse_feature('map1080/natural.png', PixelType.FOREST)
    mp.parse_feature('map1080/highway.png', PixelType.ROAD)
    mp.parse_feature('map1080/water.png', PixelType.WATER)
    return mp.pixels


def find_path(pixel_map: List[Pixel], start: Vec2, end: Vec2):
    pass

print(get_pixel_map())