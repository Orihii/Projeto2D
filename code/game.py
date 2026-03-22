#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Hop On Shooter")
    def run(self):
        
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