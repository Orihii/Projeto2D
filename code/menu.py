#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image

class Menu:
    def __init__(self, window):
        self.window = window
        self.surt = pygame.image.load("asset/gio.png")
        self.rect = self.surt.get_rect(left=0, top=0)

    def run(self, ):
        self.window.blit(self.surt, self.rect)
        pygame.display.flip()

        pass
