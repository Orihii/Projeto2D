#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, BLACK
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        
        # Player
        self.player = EntityFactory.get_entity("player")
        self.enemy = EntityFactory.get_entity("enemy")

    def run(self):
        running = True 
        while running:
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # Volta ao menu
            
            # Move o jogador
            self.player.move()
            self.enemy.move()
            
            
            self.window.fill(BLACK)
            self.player.draw(self.window)
            self.enemy.draw(self.window)
            
            pygame.display.flip()
        
        return "menu"  # Volta ao menu quando sair do loop


