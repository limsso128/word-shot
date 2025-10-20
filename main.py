import pygame as pygame
import pygame as pygame
from player import Player
from enemy import Enemy
from bullet import Bullet
from settings import Settings
from game_manager import GameManager
# from start import start


class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # start = start(self.settings)
        # start.run()

        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        pygame.display.set_caption("Word Shot")
        self.clock = pygame.time.Clock()
        self.manager = GameManager(self.settings)
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(self.settings.FPS)
            self.events()
            self.manager.update()
            self.manager.draw(self.screen)
            pygame.display.flip()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(self.manager.player.rect.centerx,
                                    self.manager.player.rect.top, self.settings)
                    self.manager.bullet_group.add(bullet)

if __name__ == "__main__":
    Main().run()



# pygame.init()
# print(pygame.ver)
