import random
import pygame

class LevelGenerator:
    def __init__(self, width, height, tile_size=32):
        self.width = width
        self.height = height
        self.tile_size = tile_size

        # Tile types
        self.EMPTY = 0
        self.GROUND = 1
        self.PLATFORM = 2
        self.WALL = 3

    def create_level(self, difficulty=1):
        # initialising empty level
        level = [[self.EMPTY for x in range(self.width)] for y in range(self.height)]

        self._create_ground(level)
        self._create_walls(level)
        self._create_platforms(level, difficulty)

        return level

    def _create_ground(self, level):

        for y in range(self.height - 3, self.height):
            for x in range(self.width):
                level[y][x] = self.GROUND

        """ for y in range(self.height - 3, self.height):
            for x in range(self.width - 8, self.width):
                level[y][x] = self.GROUND

        current_height = self.height - 3
        for x in range(8, self.width - 8):
            if random.random() < 0.3:
                current_height += random.choice([-1, 0, 1])
                current_height = max(self.height - 8, min(self.height - 2, current_height))

        for y in range(current_height, self.height):
            level[y][x] = self.GROUND """
        
    def _create_walls(self, level):

        for y in range(self.height):
            level[y][0] = self.WALL
            level[y][self.width - 1] = self.WALL

        
    def _create_platforms(self, level, difficulty):

        num_platforms = 5 + (difficulty * 3)

        for _ in range(num_platforms):
            x = random.randint(10, self.width - 15)
            y = random.randint(8, self.height - 10)
            length = random.randint(3, 8)

            # check if area is clear
            clear = True
            for i in range(length):
                if level[y][x + i] != self.EMPTY:
                    clear = False
                    break
            
            if clear:
                for i in range(length):
                    level[y][x + i] = self.PLATFORM

    

    def render_level(self, level, screen, camera_x, camera_y):

        colors = {
            self.EMPTY: '#5a6d1e',
            self.GROUND: '#503c18',
            self.PLATFORM: '#503c18',
            self.WALL: '#2e3849',
        }

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        #only render what's currently within the screen
        start_x = max(0, camera_x // self.tile_size)
        end_x = min(self.width, (camera_x + screen_width) // self.tile_size + 1)
        start_y = max(0, camera_y // self.tile_size)
        end_y = min(self.height, (camera_y + screen_height) // self.tile_size + 1)

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                tile_type = level[y][x]
                if tile_type == self.EMPTY:
                    continue

                color = colors.get(tile_type, (0, 0, 0))

                rect = pygame.Rect(
                    x * self.tile_size - camera_x,
                    y * self.tile_size - camera_y,
                    self.tile_size,
                    self.tile_size
                )

                pygame.draw.rect(screen, color, rect)

                # solid blocks get borders
                if tile_type in [self.GROUND, self.PLATFORM, self.WALL]:
                    pygame.draw.rect(screen, (0, 0, 0), rect, 1)
                    
        
