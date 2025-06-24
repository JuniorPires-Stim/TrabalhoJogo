#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, size: tuple = (6, 6)):
        super().__init__(name, position)
        self.image = pygame.image.load(f"/asset/Player1.png")
        self.image = pygame.transform.scale(self.image, size)

    def move(self, ):
        pass
