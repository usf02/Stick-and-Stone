import pygame
from pygame.locals import *

from player import Player


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("#5a6d1e")

    # Initialise player object and sprite
    player = Player()
    player_sprite = pygame.sprite.RenderPlain(player)
    level_data, generator = generate_level(1)

    # Blit background to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    player.jump()

        screen.blit(background, (0, 0))

        player_sprite.update()
        player_sprite.draw(screen)

        pygame.display.flip()



if __name__ == "__main__":
    main()
