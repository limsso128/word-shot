import pygame

class Settings:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60
    PLAYER_SPEED = 5
    BULLET_SPEED = -10
    ENEMY_SPEED_MIN = 2
    ENEMY_SPEED_MAX = 5
    ENEMY_COUNT = 5
    COLORS = {
        "WHITE": (255, 255, 255),
        "BLACK": (0, 0, 0),
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
        "GREEN": (0, 255, 0)
    }