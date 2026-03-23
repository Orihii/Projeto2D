#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.bullet import Bullet

class BulletFactory:
    @staticmethod
    def get_bullet(x, y, target_x, target_y, color=(255, 255, 0), shooter="player"):
        """Cria um novo projétil"""
        return Bullet(x, y, target_x, target_y, color, shooter)