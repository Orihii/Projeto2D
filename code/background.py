#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity
from code.Const import WIN_WIDTH, WIN_HEIGHT


class Background(Entity):
    def __init__(self):
        super().__init__()
        self.name = "background"
        
        # Carrega a imagem do espaço
        self.image = pygame.image.load("assets/images/space_background.png").convert_alpha()
        
        self.image = pygame.transform.scale(self.image, (WIN_WIDTH, WIN_HEIGHT))
        
        self.y1 = 0
        self.y2 = -WIN_HEIGHT
        
        # Velocidade da imagem
        self.speed = 2  

    def move(self): # Movimentando para cima
        self.y1 += self.speed
        self.y2 += self.speed
        
        # Reset 
        if self.y1 >= WIN_HEIGHT:
            self.y1 = -WIN_HEIGHT
        if self.y2 >= WIN_HEIGHT:
            self.y2 = -WIN_HEIGHT

    def draw(self, window):
        window.blit(self.image, (0, self.y1))
        window.blit(self.image, (0, self.y2))