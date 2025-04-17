#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGTH
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self):
        while True:
            pygame.mixer_music.load('asset/musica.mp3')
            pygame.mixer_music.play(-1)
            menu = Menu(self.window)
            menu.run()
            pass



      #      for event in pygame.event.get():
     #           if event.type == pygame.QUIT:
      #              pygame.quit()
       #             quit()




