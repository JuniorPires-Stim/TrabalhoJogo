#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('asset/PNG/War2/Bright/War2.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        self.window.blit(self.surf, self.rect)
        pygame.display.flip()
        pass
