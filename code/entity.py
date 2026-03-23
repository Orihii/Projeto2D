#!/usr/bin/python
# -*- coding: utf-8 -*-

class Entity:
    def __init__(self):
        self.name = None
        self.surf = None
        self.rect = None
        self.health = 1
        self.max_health = 1
        self.is_alive = True
        self.invincible_timer = 0
        self.invincible_duration = 60  # 1 segundo a 60 FPS

    def move(self):
        pass

    def take_damage(self, damage=1):
        if self.invincible_timer <= 0 and self.is_alive:
            self.health -= damage
            self.invincible_timer = self.invincible_duration
            
            if self.health <= 0:
                self.is_alive = False
                return True  # Morreu
        return False  # Não morreu

    def update_invincible(self):
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

    def is_invincible(self):
        return self.invincible_timer > 0

    def check_collision(self, other_entity):
        if self.rect and other_entity.rect:
            return self.rect.colliderect(other_entity.rect)
        return False

    def draw(self, window):
        if self.surf and self.rect:
            window.blit(self.surf, self.rect)