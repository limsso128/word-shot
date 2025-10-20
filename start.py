import pygame

class start:
    def __init__(self, settings):
        self.settings = settings
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Word Shot - Start")
        self.clock = pygame.time.Clock()
        self.running = True

        # 배경 이미지
        self.background = pygame.image.load("assets/background1.png.png")
        self.background = pygame.transform.scale(
            self.background,
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT)
        )

        # Start 버튼 이미지
        self.start_button = pygame.image.load("assets/start_button.png.png")
        self.start_button_rect = self.start_button.get_rect(center=(
            self.settings.SCREEN_WIDTH // 2,
            self.settings.SCREEN_HEIGHT // 2
        ))

        def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(event.pos):
                        self.running = False  # 버튼 클릭 시 시작 화면 종료