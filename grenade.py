import pygame
from settings import Settings

class Grenade(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.image = pygame.Surface([20, 20])
        self.image.fill(self.settings.GREEN)
        self.rect = self.image.get_rect()
        self.damage = 50

    def update(self):
        def update(self):
        self.rect.x += 6
        if self.rect.x >= self.settings.SCREEN_WIDTH + 60:
            self.kill()
