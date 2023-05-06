from enum import Enum
from typing import List
from pixels import Pixel, Vec2, PixelType
from map_parser import MapParser, init_empty_map
from astar import AStar


def get_pixel_map(map_name, width, height):
    mp = MapParser(width, height)
    mp.parse_feature(f'{map_name}/highway.png', PixelType.ROAD)
    mp.parse_feature(f'{map_name}/water.png', PixelType.WATER)
    mp.parse_feature(f'{map_name}/natural.png', PixelType.FOREST)
    # mp.parse_feature(f'{map_name}/coastline.png', PixelType.BORDER)
    return mp.pixels

def print_map(map):
    for row in map:
        for col in row:
            print(col, end='')
        print()


class MazeSolver(AStar):

    """sample use of the astar algorithm. In this exemple we work on a maze made of ascii characters,
    and a 'node' is just a (x,y) tuple that represents a reachable position"""

    def __init__(self, pixel_map, width, height):
        self.lines = pixel_map
        self.width = width
        self.height = height

    def heuristic_cost_estimate(self, n1: PixelType, n2: PixelType):
        """computes the 'direct' distance between two (x,y) tuples"""
        x, y = n1
        pixel: Pixel = self.lines[y][x]
        return pixel.pixel_type.value

    def distance_between(self, n1, n2):
        """this method always returns 1, as two 'neighbors' are always adajcent"""
        return 1

    def neighbors(self, node):
        """ for a given coordinate in the maze, returns up to 4 adjacent(north,east,south,west)
            nodes that can be reached (=any adjacent coordinate that is not a wall)
        """
        x, y = node
        results = []
        if x > 0:
            results.append((x - 1, y))
        if x < self.width - 1:
            results.append((x + 1, y))
        if y > 0:
            results.append((x, y - 1))
        if y < self.height - 1:
            results.append((x, y + 1))
        return results


def solve(pixel_map, width, height, start, end):
    solver = MazeSolver(pixel_map, width, height)
    path = solver.astar(start, end)
    return list(path)



