import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # create image and fill (can load image here)
        self.image = pygame.Surface([96, 96])
        self.image.fill('#c27e31')
        self.rect = self.image.get_rect()

        # physics
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 10
        self.jump_power = -20
        self.gravity = 1
        self.on_ground = True

        # initial position
        self.rect.x = 100
        self.rect.bottom = 500

    def update(self):
        # handling input for horizontal movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
        else:
            self.vel_x = 0

        # movement
        self.vel_y += self.gravity

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y




    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False
