# this is the practice of Program of Python 

# Introduction of Python

import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 400, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

FPS = 60
GRAVITY = 0.5
PIPE_GAP = 150
PIPE_WIDTH = 80
PIPE_SPEED = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")


font = pygame.font.SysFont("Arial", 24)
bird_image = pygame.Surface((30, 30))
bird_image.fill(RED)

clock = pygame.time.Clock()

class Bird:
    def __init__(self, x, y):
    self.x = x
    self.y = y
    self.vel = 0
    self.width = 30
    self.height = 30

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))
        
        def update(self):
            self.vel += GRAVITY
            self.y += self.vel


game_loop()
