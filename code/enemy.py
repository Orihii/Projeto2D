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
        
        # Carrega a mesma imagem do player
        self.surf = pygame.image.load("assets/images/ff.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        
        # Cria uma cópia da imagem para adicionar a borda vermelha
        self.surf = self.add_red_border(self.surf)
        
        self.rect = self.surf.get_rect(center=(x + 25, y + 25))
        
        # Velocidade aleatória
        self.speed_x = random.choice([-3, -2, 2, 3])
        self.speed_y = random.choice([-2, -1, 1, 2])
        
        # Timer para mudar direção
        self.change_direction_timer = 0
        self.change_direction_delay = random.randint(30, 90)

    def add_red_border(self, image):
        """Adiciona uma borda vermelha ao redor da imagem"""
        # Obtém o tamanho da imagem
        width, height = image.get_size()
        
        # Cria uma superfície maior para a borda
        border_size = 3  # Espessura da borda
        new_width = width + (border_size * 2)
        new_height = height + (border_size * 2)
        
        # Cria uma superfície com fundo transparente
        bordered_image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)
        
        # Desenha o retângulo vermelho (borda)
        pygame.draw.rect(bordered_image, (255, 0, 0), (0, 0, new_width, new_height))
        
        # Desenha o retângulo preto (opcional - para dar contraste)
        # pygame.draw.rect(bordered_image, (0, 0, 0), (border_size, border_size, width, height))
        
        # Coloca a imagem original no centro
        bordered_image.blit(image, (border_size, border_size))
        
        return bordered_image

    def move(self):
        # Move o inimigo
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Controle de direção - muda aleatoriamente após um tempo
        self.change_direction_timer += 1
        if self.change_direction_timer >= self.change_direction_delay:
            self.change_direction_timer = 0
            self.change_direction_delay = random.randint(30, 90)
            
            # Muda direção aleatoriamente
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
    
    def draw(self, window):
        window.blit(self.surf, self.rect)