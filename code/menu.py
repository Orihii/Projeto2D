#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
from code.Const import WHITE, WIN_WIDTH, WIN_HEIGHT

class Menu:
    def __init__(self, window):
        self.window = window
        self.surt = pygame.image.load("assets/images/gio.png")
        self.rect = self.surt.get_rect(left=0, top=0)
        self.font = pygame.font.Font(None, 36)


    def run(self, ):
        
        running = True
        while running:
            #print("Menu is running")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    #print("Quitting")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                         running = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()               
            self.window.blit(self.surt, self.rect)

        # Texto do menu
            title = self.font.render("SPACE SHOOTER", True, WHITE)
            start = self.font.render("Press SPACE to Start", True, WHITE)
            
            self.window.blit(title, (WIN_WIDTH//2 - title.get_width()//2, 100))
            self.window.blit(start, (WIN_WIDTH//2 - start.get_width()//2, WIN_HEIGHT - 100))


            pygame.display.flip()

        
