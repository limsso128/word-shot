import pygame as pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, settings):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((5, 10))
        self.image.fill(self.settings.COLORS["RED"])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = self.settings.BULLET_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()