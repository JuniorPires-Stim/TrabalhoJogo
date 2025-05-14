from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        original_image = pygame.image.load('asset/' + name + '.png')

        resized_image = pygame.transform.scale(original_image, (720, 480))

        self.surf = resized_image
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
