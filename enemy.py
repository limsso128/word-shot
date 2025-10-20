import pygame as pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.settings.COLORS["GREEN"])
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, self.settings.SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(self.settings.ENEMY_SPEED_MIN, self.settings.ENEMY_SPEED_MAX)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.settings.SCREEN_HEIGHT:
            self.reset()