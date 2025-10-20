import pygame as pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.settings.COLORS["BLUE"])
        self.rect = self.image.get_rect()
        self.rect.centerx = self.settings.SCREEN_WIDTH // 2
        self.rect.bottom = self.settings.SCREEN_HEIGHT - 10
        self.speed = self.settings.PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.settings.SCREEN_WIDTH:
            self.rect.x += self.speed
