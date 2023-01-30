import pygame
class Player:

        def __init__(self):
            self.x=400
            self.y=400
            self.width = 30
            self.height=30
            self.color=(255,0,0)

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))