#!/usr/bin/python
# -*- coding: utf-8 -*-

from code import Entity


class Level:
    def __init__(self, window, nome, game_mode):
        self.window = window
        self.name = nome
        self.game_mode = game_mode
        self.entity_lis = list[Entity] = []

    def run(self, ):
        pass
