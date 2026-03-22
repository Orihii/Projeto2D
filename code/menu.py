#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
from code.Const import WHITE, WIN_WIDTH, WIN_HEIGHT, ORANGE, BLACK, MAGENTA

class Menu:
    def __init__(self, window):
        self.window = window
        self.surt = pygame.image.load("assets/images/gio.png")
        self.rect = self.surt.get_rect(left=0, top=0)
        self.font = pygame.font.SysFont("Impact", 40)
        self.small_font = pygame.font.SysFont("Impact", 32) 

        # Opções do menu
        self.options = ["START", "QUIT", "WIP"]
        self.selected = 0  # 0 = START, 1 = QUIT, 2 = WIP


    def run(self, ):
        
        running = True
        while running:
           # print("Menu is running")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("Quitting game...")  # Para teste
                    quit()
                    # print("Quitting")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                         running = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        print("Quitting game...")  # Para teste
                        quit()   

                if event.type == pygame.KEYDOWN:
                    # Navegação com setas e wasd
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.selected = (self.selected - 1) % len(self.options)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.selected = (self.selected + 1) % len(self.options)

                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        if self.selected == 0:  # START
                            print("Starting game...")  # Para teste
                                

                            return "start"                           
                        
                        elif self.selected == 1:  # QUIT
                            pygame.quit()
                            print("Quitting game...")  # Para teste
                            quit()
                            
                        elif self.selected == 2:  # WIP                           
                            print("WIP option selected")  # Para teste
                            return "wip"

        # Desenha o fundo do menu    
            self.window.fill(BLACK)                
            self.window.blit(self.surt, self.rect)

        # Texto do menu
            title = self.font.render("HOP ON SHOOTER", True, MAGENTA)
            
            self.window.blit(title, (WIN_WIDTH//2 - title.get_width()//2, 100))

# Desenha as opções do menu
            for i, option in enumerate(self.options):
                # Define a cor da opcao selecionada
                color = ORANGE if i == self.selected else WHITE
                
                # Renderiza o texto
                text = self.small_font.render(option, True, color)
                
                # posição do texto
                x = WIN_WIDTH//2 - text.get_width()//2
                y = WIN_HEIGHT//2 + i * 60 + 50
                
                self.window.blit(text, (x, y))
                
                # indicador ">" na opcão selecionada
                if i == self.selected:
                    indicator = self.small_font.render(">", True, ORANGE)
                    self.window.blit(indicator, (x - 40, y))
                    indicator2 = self.small_font.render("<", True, ORANGE)
                    self.window.blit(indicator2, (x + text.get_width() + 20, y))


            pygame.display.flip()

        
