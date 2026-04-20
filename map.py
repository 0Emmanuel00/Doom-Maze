import pygame as pg
from random import randrange, randint, choice

_ = False
MAP_SIZE = 100
WALL_TYPES = [1, 2, 3, 4, 5]

# Generate initial static map
def generate_static_map():
    mini_map = []
    safe_zone = 5
    for y in range(MAP_SIZE):
        row = []
        for x in range(MAP_SIZE):
            # Safe zone around spawn (center is around 50,50)
            center_x, center_y = MAP_SIZE // 2, MAP_SIZE // 2
            dist_to_center = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            
            if x == 0 or x == MAP_SIZE - 1 or y == 0 or y == MAP_SIZE - 1:
                row.append(1)
            elif dist_to_center <= safe_zone:
                row.append(_)
            elif x % 15 == 0 or y % 15 == 0:
                row.append(_)
            elif randint(1, 100) < 30:
                row.append(choice(WALL_TYPES))
            else:
                row.append(_)
        mini_map.append(row)
    return mini_map


class Map:
    def __init__(self, game):
        self.game = game
        self.world_map = {}
        self.rows = MAP_SIZE
        self.cols = MAP_SIZE
        self.get_map()

    def get_map(self):
        mini_map = generate_static_map()
        for j, row in enumerate(mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def is_wall(self, x, y):
        x, y = int(x), int(y)
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return True
        return (x, y) in self.world_map

    def get_tile(self, x, y):
        x, y = int(x), int(y)
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return 1
        return self.world_map.get((x, y), 0)

    def get_random_empty_position(self, center=(0, 0), radius=25):
        cx, cy = center
        x = int(cx) + randrange(-radius, radius + 1)
        y = int(cy) + randrange(-radius, radius + 1)
        x = max(1, min(self.cols - 2, x))
        y = max(1, min(self.rows - 2, y))
        while self.is_wall(x, y) or (x, y) == (int(cx), int(cy)):
            x = int(cx) + randrange(-radius, radius + 1)
            y = int(cy) + randrange(-radius, radius + 1)
            x = max(1, min(self.cols - 2, x))
            y = max(1, min(self.rows - 2, y))
        return x + 0.5, y + 0.5

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
