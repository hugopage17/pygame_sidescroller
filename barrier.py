import pygame
from settings import Settings

class Barrier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.image = pygame.Surface([60, 40])
        self.image.fill(self.settings.RED)
        self.rect = self.image.get_rect()
        self.health = 10

    def update(self):
        self.rect.x -= 4
        if self.rect.x <= -60:
            self.kill()
