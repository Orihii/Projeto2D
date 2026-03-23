#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.bulletFactory import BulletFactory

class Player(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.name = "player"
        
        # Vidas do jogador 
        self.health = 3
        self.max_health = 3
        self.is_alive = True
        self.invincible_timer = 0
        self.invincible_duration = 60
        
        # Imagem do jogador 
        self.surf = pygame.image.load("assets/images/ff.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect(center=(x + 15, y + 15))
        self.speed = 6
        
        # Efeito de piscar quando invencível 
        self.blink_timer = 0
        
        # Tiros do jogador 
        self.shoot_cooldown = 0
        self.shoot_delay = 15
        self.bullets = []

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT

    def shoot(self, mouse_x, mouse_y):
        if self.shoot_cooldown <= 0 and self.is_alive:
            bullet = BulletFactory.get_bullet(
                self.rect.centerx, self.rect.centery, 
                mouse_x, mouse_y, 
                (255, 255, 0), "player"
            )
            self.bullets.append(bullet)
            self.shoot_cooldown = self.shoot_delay
            return True
        return False

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if not bullet.is_alive:
                self.bullets.remove(bullet)

    def take_damage(self, damage=1):
        if self.invincible_timer <= 0 and self.is_alive:
            self.health -= damage
            self.invincible_timer = self.invincible_duration
            self.blink_timer = self.invincible_duration
            
            if self.health <= 0:
                self.is_alive = False
                return True
        return False

    def update(self):
        self.update_invincible()
        if self.blink_timer > 0:
            self.blink_timer -= 1
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        self.update_bullets()

    def should_blink(self):
        return self.blink_timer > 0 and (self.blink_timer // 5) % 2 == 0

    def draw(self, window):
        if not self.is_alive:
            return
            
        if self.should_blink():
            temp_surf = self.surf.copy()
            temp_surf.set_alpha(128)
            window.blit(temp_surf, self.rect)
        else:
            window.blit(self.surf, self.rect)
        
        for bullet in self.bullets:
            bullet.draw(window)