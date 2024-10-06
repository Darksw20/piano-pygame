# Piano Tiles

# Author : Prajjwal Pathak (pyguru)
# Date : Thursday, 30 November, 2021

import json
import random
import pygame
from threading import Thread

from objects import Tile, Square, Text, Button, Counter

# Presentation Layer
class GameView:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Piano Tiles')
        
        # Colors
        self.background_color = (255, 255, 255)
        self.tile_color = (0, 0, 0)
        self.score_color = (255, 0, 0)
        
        # Font
        self.font = pygame.font.SysFont(None, 36)

    def draw_tile(self, tile):
        pygame.draw.rect(self.screen, self.tile_color, tile.get_rect())

    def display_score(self, score):
        score_surf = self.font.render(f'Score: {score}', True, self.score_color)
        self.screen.blit(score_surf, (10, 10))

    def display_game_over(self, score):
        self.screen.fill(self.background_color)
        game_over_surf = self.font.render(f'Game Over! Final Score: {score}', True, self.score_color)
        self.screen.blit(game_over_surf, (self.width // 4, self.height // 2))

    def update_display(self):
        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill(self.background_color)

    def quit(self):
        pygame.quit()