import pygame
from settings import Settings

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.health = 30
        self.image = pygame.Surface([60, 60])
        self.image.fill(self.settings.WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 4
        if self.health <= 0:
            self.kill()
            
