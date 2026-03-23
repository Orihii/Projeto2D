#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random
from code.entity import Entity
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.name = "enemy"
        
        # ========== VIDA ==========
        self.health = 1
        self.max_health = 1
        self.is_alive = True
        self.invincible_timer = 0
        self.invincible_duration = 30
        
        # ========== VISUAL ==========
        self.surf = pygame.image.load("assets/images/ff.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf = self.add_red_border(self.surf)
        self.rect = self.surf.get_rect(center=(x + 25, y + 25))
        
        # ========== MOVIMENTO ==========
        self.speed_x = random.choice([-3, -2, 2, 3])
        self.speed_y = random.choice([-2, -1, 1, 2])
        self.change_direction_timer = 0
        self.change_direction_delay = random.randint(30, 90)

    def add_red_border(self, image):
        """Adiciona uma borda vermelha ao redor da imagem"""
        width, height = image.get_size()
        border_size = 3
        new_width = width + (border_size * 2)
        new_height = height + (border_size * 2)
        
        bordered_image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)
        pygame.draw.rect(bordered_image, (255, 0, 0), (0, 0, new_width, new_height))
        bordered_image.blit(image, (border_size, border_size))
        
        return bordered_image

    def move(self):
        """Move o inimigo aleatoriamente"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Muda direção aleatoriamente
        self.change_direction_timer += 1
        if self.change_direction_timer >= self.change_direction_delay:
            self.change_direction_timer = 0
            self.change_direction_delay = random.randint(30, 90)
            self.speed_x = random.choice([-3, -2, 2, 3])
            self.speed_y = random.choice([-2, -1, 1, 2])
        
        # Limites da tela
        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed_x = abs(self.speed_x)
        if self.rect.right >= WIN_WIDTH:
            self.rect.right = WIN_WIDTH
            self.speed_x = -abs(self.speed_x)
        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed_y = abs(self.speed_y)
        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            self.speed_y = -abs(self.speed_y)

    def bounce(self, other_enemy):
        """Ricocheteia quando colide com outro inimigo"""
        # Troca as velocidades
        self.speed_x, other_enemy.speed_x = other_enemy.speed_x, self.speed_x
        self.speed_y, other_enemy.speed_y = other_enemy.speed_y, self.speed_y
        
        # Separa para não ficar preso
        if self.rect.centerx < other_enemy.rect.centerx:
            self.rect.x -= 5
            other_enemy.rect.x += 5
        else:
            self.rect.x += 5
            other_enemy.rect.x -= 5
        
        if self.rect.centery < other_enemy.rect.centery:
            self.rect.y -= 5
            other_enemy.rect.y += 5
        else:
            self.rect.y += 5
            other_enemy.rect.y -= 5

    def update(self):
        """Atualiza timers do inimigo"""
        self.update_invincible()
    
    def take_damage(self, damage=1):
        """Recebe dano e retorna True se morreu"""
        if self.invincible_timer <= 0 and self.is_alive:
            self.health -= damage
            self.invincible_timer = self.invincible_duration
            
            if self.health <= 0:
                self.is_alive = False
                return True
        return False

    def draw(self, window):
        """Desenha o inimigo"""
        if self.is_alive:
            window.blit(self.surf, self.rect)