#!/usr/bin/python
# -*- coding: utf-8 -*-

# class EntityFactory:
#     def __init__(self):
#         pass

    #!/usr/bin/python
# -*- coding: utf-8 -*-

from code.player import Player
from code.enemy import Enemy
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT

class EntityFactory:
    @staticmethod
    def get_entity(entity_type, position=None):
        
        if entity_type == "player":
            # Posição padrão
            x = WIN_WIDTH // 2 - 15
            y = WIN_HEIGHT - 60
            return Player(x, y)
        
        elif entity_type == "enemy":
            if position:
                x, y = position
            else:
                x = WIN_WIDTH // 2 - 15
                y = 50
            return Enemy(x, y)
        
        elif entity_type == "background":
            return Background()
        
        return None