import pygame
from player import Player
from barrier import Barrier
from settings import Settings
from bullet import Bullet
from enemy import Enemy
from grenade import Grenade
import random

class Game(object):
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.settings = Settings()
        self.all_sprites_list = pygame.sprite.Group()
        self.barrier_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.grenade_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        
        self.player = Player()
        self.player.rect.x = 20
        self.player.rect.y = self.settings.SCREEN_HEIGHT - 80
        self.all_sprites_list.add(self.player) 
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullet = Bullet()
                    self.bullet.rect.x = 20
                    self.bullet.rect.y = self.settings.SCREEN_HEIGHT - 80
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)
                if event.key == pygame.K_g:
                    self.grenade = Grenade()
                    self.grenade.rect.x = 20
                    self.grenade.rect.y = self.settings.SCREEN_HEIGHT - 40
                    self.all_sprites_list.add(self.grenade)
                    self.bullet_list.add(self.grenade)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False

    def spawn(self):
        self.spawn_num = random.randrange(1,500)
        if self.spawn_num == 3:
            self.barrier = Barrier()
            self.barrier.rect.x = self.settings.SCREEN_WIDTH + 60
            self.barrier.rect.y = self.settings.SCREEN_HEIGHT - 60
            self.all_sprites_list.add(self.barrier)
            self.barrier_list.add(self.barrier)            
        elif self.spawn_num == 12 or self.spawn_num == 24:
            self.enemy = Enemy()
            self.enemy.rect.x = self.settings.SCREEN_WIDTH + 60
            self.enemy.rect.y = self.settings.SCREEN_HEIGHT - 80
            self.all_sprites_list.add(self.enemy)
            self.enemy_list.add(self.enemy)
            
    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()
            
            barrier_hit_list = pygame.sprite.spritecollide(self.player, self.barrier_list, True)
            for barrier in barrier_hit_list:
                self.game_over = True
 
    def display_frame(self, screen):
        screen.fill(self.settings.BLACK)
 
        if self.game_over:
            pygame.quit()
 
        if not self.game_over:
            self.all_sprites_list.draw(screen)
 
        pygame.display.flip()
