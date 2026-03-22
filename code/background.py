#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity  


class Background(Entity):
    def __init__(self):
        super().__init__()
        self.name = "background"

    def move(self):
        pass