class Camera:
    def __init__(self, screen_width, screen_height):
        self.x = 0
        self.y = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, player1, level_width, level_height, tile_size):

        self.x = player1.rect.centerx - self.screen_width // 2
        self.y = player1.rect.centery - self.screen_height // 2

        max_x = (level_width * tile_size) - self.screen_width
        max_y = (level_height * tile_size) - self.screen_height

        self.x = max(0, min(self.x, max_x))
        self.y = max(0, min(self.y, max_y))

