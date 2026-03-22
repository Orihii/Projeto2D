#!/usr/bin/python
# -*- coding: utf-8 -*-

class Level:
    def __init__(self):
        self.window = None
        self.name = None
        self.entity_list = None

    def run(self, ):
        pass

#
#
#       
# Level.py (versão temporária para testar o menu)
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, BLACK

class Level:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 48)
    
    def run(self):
        running = True
        clock = pygame.time.Clock()
        
        while running:
            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # Volta ao menu
            
            self.window.fill(BLACK)
            text = self.font.render("GAME - Press ESC to return", True, (255, 255, 255))
            self.window.blit(text, (WIN_WIDTH//2 - text.get_width()//2, WIN_HEIGHT//2))
            pygame.display.flip()