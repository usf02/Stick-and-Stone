import pygame
from pygame.locals import *



def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("#5a6d1e")

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

        screen.blit(background, (0, 0))

        player_sprite.update()
        player_sprite.draw(screen)

        pygame.display.flip()



if __name__ == "__main__":
    main()
