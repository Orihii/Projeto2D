#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.level import Level
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT

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