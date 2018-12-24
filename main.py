import pygame
import random
from game import Game
from settings import Settings

def main():
    pygame.init()
    settings = Settings()
    size = [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Run n Shoot")
    pygame.mouse.set_visible(False)

    done = False
    clock = pygame.time.Clock()
    game = Game()
 
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()
 
if __name__ == "__main__":
    main()
