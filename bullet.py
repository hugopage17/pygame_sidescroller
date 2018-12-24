import pygame
from settings import Settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.image = pygame.Surface([10, 5])
        self.image.fill(self.settings.GREEN)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 10
        if self.rect.x >= self.settings.SCREEN_WIDTH + 60:
            self.kill()
        
