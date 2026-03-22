#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity



class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.name = "enemy"
        self.rect = pygame.Rect(x, y, 30, 30)
        self.speed = 3
        self.direction = 1
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 0, 0))  # Red

    def move(self):
        self.rect.x += self.speed * self.direction
        
        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction = 1
        if self.rect.right >= 400:  # 
            self.rect.right = 400
            self.direction = -1
    
    def draw(self, window):
        window.blit(self.surf, self.rect)