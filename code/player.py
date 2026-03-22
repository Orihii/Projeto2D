#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Entity import Entity
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Player(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.name = "player"
        
        # Cria um retângulo
        self.rect = pygame.Rect(x, y, 30, 30)
        self.speed = 6
        
        
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 255, 255)) 

    def move(self):
        # Teclas de movimento
        keys = pygame.key.get_pressed()
        
        # Movimento horizontal
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        
        # Movimento vertical
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        
        # Limite da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
    
    def draw(self, window):
        # Desenha o jogador na tela
        window.blit(self.surf, self.rect)