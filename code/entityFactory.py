#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.player import Player
from code.enemy import Enemy
from code.background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT

class EntityFactory:
    @staticmethod
    def get_entity(entity_type, position=None):
        
        if entity_type == "player":
            x = WIN_WIDTH // 2 - 25
            y = WIN_HEIGHT - 70
            return Player(x, y)
        
        elif entity_type == "enemy":
            if position:
                x, y = position
            else:
                x = WIN_WIDTH // 2 - 25
                y = 50
            return Enemy(x, y)
        
        elif entity_type == "background":
            return Background()
        
        return None