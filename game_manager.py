import pygame as pygame
from player import Player
from enemy import Enemy

class GameManager:
    def __init__(self, settings):
        self.settings = settings
        self.player = Player(settings)
        self.player_group = pygame.sprite.GroupSingle(self.player)

        self.bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        for _ in range(self.settings.ENEMY_COUNT):
            self.enemy_group.add(Enemy(settings))

        self.score = 0

    def update(self):
        self.player_group.update()
        self.bullet_group.update()
        self.enemy_group.update()

        # 충돌 체크
        hits = pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, True, True)
        for hit in hits:
            self.score += 1
            self.enemy_group.add(Enemy(self.settings))

    def draw(self, screen):
        screen.fill(self.settings.COLORS["BLACK"])
        self.player_group.draw(screen)
        self.bullet_group.draw(screen)
        self.enemy_group.draw(screen)