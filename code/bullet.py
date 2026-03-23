#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Bullet(Entity):
    def __init__(self, x, y, target_x, target_y, color=(255, 255, 0), shooter="player"):
        super().__init__()
        self.name = "bullet"
        self.shooter = shooter  # "player" ou "enemy"
        
        # ========== VISUAL ==========
        self.surf = pygame.Surface((8, 8))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=(x, y))
        
        # ========== MOVIMENTO ==========
        # Calcula direção do tiro
        dx = target_x - x
        dy = target_y - y
        distance = max(1, (dx**2 + dy**2)**0.5)
        
        # Velocidade constante
        self.speed = 6 if shooter == "enemy" else 8
        self.vel_x = (dx / distance) * self.speed
        self.vel_y = (dy / distance) * self.speed
        
        # ========== VIDA ==========
        self.health = 1
        self.max_health = 1
        self.is_alive = True
        
        # Tempo de vida máximo (3 segundos para inimigos)
        self.life_timer = 0
        self.max_life = 180 if shooter == "enemy" else 300

    def move(self):
        """Move o projétil na direção calculada"""
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Atualiza timer de vida
        self.life_timer += 1
        
        # Remove se sair da tela ou se tempo de vida expirar
        if (self.rect.right < 0 or self.rect.left > WIN_WIDTH or
            self.rect.bottom < 0 or self.rect.top > WIN_HEIGHT or
            self.life_timer >= self.max_life):
            self.is_alive = False

    def draw(self, window):
        """Desenha o projétil"""
        if self.is_alive:
            if self.shooter == "player":
                # Efeito de brilho amarelo
                pygame.draw.circle(window, (255, 255, 0), self.rect.center, 6)
                pygame.draw.circle(window, (255, 200, 0), self.rect.center, 4)
                pygame.draw.circle(window, (255, 100, 0), self.rect.center, 2)
            else:
                # Efeito de brilho vermelho para inimigos
                pygame.draw.circle(window, (255, 0, 0), self.rect.center, 6)
                pygame.draw.circle(window, (200, 0, 0), self.rect.center, 4)
                pygame.draw.circle(window, (150, 0, 0), self.rect.center, 2)