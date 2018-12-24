import pygame
from settings import Settings

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.image = pygame.Surface([60, 60])
        self.image.fill(self.settings.BLUE)
        self.rect = self.image.get_rect()
            
    def jump(self):
        while self.rect.y > 280:
            self.rect.y -= 2
