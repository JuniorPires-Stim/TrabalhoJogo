#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH
from code.Const import COLOR_RED
from code.Const import COLOR_WHITE
from code.Const import MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        original_image = pygame.image.load('asset/PNG/War2/Bright/War2.png').convert_alpha()
        resized_image = pygame.transform.scale(original_image, (720, 480))
        self.surf = resized_image
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def run(self, ):
        pygame.mixer_music.load('asset/musica.wav')
        pygame.mixer_music.play(-1)

        menu_option = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=80, text='ZooBie', text_color=COLOR_RED, text_center_pos=(WIN_WIDTH / 2, 60))
            self.menu_text(text_size=80, text='Apocalipse', text_color=COLOR_RED, text_center_pos=(WIN_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=40, text=MENU_OPTION[i], text_color=COLOR_RED,
                                   text_center_pos=(WIN_WIDTH / 2, 210 + 60 * i))

                else:
                    self.menu_text(text_size=40, text=MENU_OPTION[i], text_color=COLOR_WHITE,
                                   text_center_pos=(WIN_WIDTH / 2, 220 + 60 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida sanz Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
