#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.level import Level
from code.menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        
        # 
        pygame.mixer.init()
        
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Hop On Shooter")
        
        try:
            pygame.mixer.music.load("assets/audio/EveryDay.mp3")
            # Loop infinito da música
            pygame.mixer.music.set_volume(0.1)  # Volume de 0.0 a 1.0
        except:
            print("Arquivo de música não encontrado")
    
    def run(self):
        pygame.mixer.music.play(-1)
        
        while True:
            menu = Menu(self.window)
            choice = menu.run()  # Recebe "start", "quit" ou "wip"
            
            if choice == "start":
                print("Starting game...")
                level = Level(self.window)
                level.run()  # Quando terminar, volta ao menu
            elif choice == "quit":
                print("Quitting game...")
                break
        
        pygame.quit()