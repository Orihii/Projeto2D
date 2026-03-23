#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random
from code.Const import WIN_WIDTH, WIN_HEIGHT, BLACK, WHITE, RED, YELLOW
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        
        # Player
        self.player = EntityFactory.get_entity("player")
        
        # Inimigos
        self.enemies = []
        for i in range(4):
            x = random.randint(50, WIN_WIDTH - 50)
            y = random.randint(50, WIN_HEIGHT - 150)
            enemy = EntityFactory.get_entity("enemy", (x, y))
            self.enemies.append(enemy)
        
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        self.game_over = False
        self.game_over_timer = 0

    def run(self):
        running = True 
        while running:
            self.clock.tick(60)
            
            # ========== EVENTOS ==========
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if self.game_over and event.key == pygame.K_r:
                        running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.game_over and self.player.is_alive:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        self.player.shoot(mouse_x, mouse_y)
            
            if not self.game_over and self.player.is_alive:
                # ========== ATUALIZA ==========
                self.player.move()
                self.player.update()
                
                for enemy in self.enemies:
                    enemy.move()
                    # Passa a posição do player para o inimigo atirar
                    enemy.update(self.player.rect.centerx, self.player.rect.centery)
                
                # ========== COLISÃO TIROS DO PLAYER x INIMIGOS ==========
                for bullet in self.player.bullets[:]:
                    for enemy in self.enemies[:]:
                        if bullet.check_collision(enemy):
                            enemy_died = enemy.take_damage(1)
                            bullet.is_alive = False
                            
                            if enemy_died:
                                self.enemies.remove(enemy)
                                self.score += 10
                                
                                x = random.randint(50, WIN_WIDTH - 50)
                                y = random.randint(50, WIN_HEIGHT - 150)
                                new_enemy = EntityFactory.get_entity("enemy", (x, y))
                                self.enemies.append(new_enemy)
                            break
                
                # ========== COLISÃO TIROS DOS INIMIGOS x PLAYER ==========
                for enemy in self.enemies:
                    for bullet in enemy.bullets[:]:
                        if bullet.check_collision(self.player):
                            player_died = self.player.take_damage(1)
                            bullet.is_alive = False
                            
                            if player_died:
                                self.game_over = True
                                self.game_over_timer = 120
                            break
                
                # ========== COLISÃO PLAYER x INIMIGOS ==========
                for enemy in self.enemies[:]:
                    if self.player.check_collision(enemy):
                        player_died = self.player.take_damage(1)
                        self.enemies.remove(enemy)
                        
                        x = random.randint(50, WIN_WIDTH - 50)
                        y = random.randint(50, WIN_HEIGHT - 150)
                        new_enemy = EntityFactory.get_entity("enemy", (x, y))
                        self.enemies.append(new_enemy)
                        
                        if player_died:
                            self.game_over = True
                            self.game_over_timer = 120
                        break
                
                # ========== COLISÃO ENTRE INIMIGOS ==========
                for i in range(len(self.enemies)):
                    for j in range(i + 1, len(self.enemies)):
                        if self.enemies[i].check_collision(self.enemies[j]):
                            self.enemies[i].bounce(self.enemies[j])
            
            # ========== DESENHA ==========
            self.window.fill(BLACK)
            
            for enemy in self.enemies:
                enemy.draw(self.window)
            
            self.player.draw(self.window)
            
            # ========== INTERFACE ==========
            self.draw_hearts()
            
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.window.blit(score_text, (10, 10))
            
            enemies_text = self.font.render(f"Enemies: {len(self.enemies)}", True, WHITE)
            self.window.blit(enemies_text, (10, 50))
            
            controls_text = self.font.render("Mouse: Aim & Shoot | Arrow Keys: Move", True, WHITE)
            self.window.blit(controls_text, (10, WIN_HEIGHT - 30))
            
            if self.player.is_invincible() and not self.game_over:
                inv_text = self.font.render("INVINCIBLE", True, YELLOW)
                self.window.blit(inv_text, (WIN_WIDTH // 2 - inv_text.get_width() // 2, 20))
            
            # ========== GAME OVER ==========
            if self.game_over:
                overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
                overlay.set_alpha(180)
                overlay.fill(BLACK)
                self.window.blit(overlay, (0, 0))
                
                game_over_text = self.big_font.render("GAME OVER", True, RED)
                self.window.blit(game_over_text, (WIN_WIDTH // 2 - game_over_text.get_width() // 2, WIN_HEIGHT // 2 - 60))
                
                final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
                self.window.blit(final_score_text, (WIN_WIDTH // 2 - final_score_text.get_width() // 2, WIN_HEIGHT // 2))
                
                restart_text = self.font.render("Press R to return to menu", True, WHITE)
                self.window.blit(restart_text, (WIN_WIDTH // 2 - restart_text.get_width() // 2, WIN_HEIGHT // 2 + 40))
                
                self.game_over_timer -= 1
                if self.game_over_timer <= 0:
                    return "menu"
            
            pygame.display.flip()
        
        return "menu"
    
    def draw_hearts(self):
        """Desenha os corações"""
        heart_size = 25
        spacing = 8
        start_x = WIN_WIDTH - (heart_size * self.player.max_health + spacing * (self.player.max_health - 1)) - 15
        y = 15
        
        for i in range(self.player.max_health):
            x = start_x + i * (heart_size + spacing)
            if i < self.player.health:
                self.draw_heart(x, y, heart_size, RED)
            else:
                self.draw_heart(x, y, heart_size, RED, outline=True)
    
    def draw_heart(self, x, y, size, color, outline=False):
        """Desenha um coração"""
        points = [
            (x + size // 2, y + size // 4),
            (x + size // 4, y),
            (x, y + size // 4),
            (x + size // 2, y + size),
            (x + size, y + size // 4),
            (x + size * 3 // 4, y)
        ]
        if outline:
            pygame.draw.polygon(self.window, color, points, 2)
        else:
            pygame.draw.polygon(self.window, color, points)