import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("images/For_TirGame2.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("images/apple.png")
target_width = 100
target_height = 100
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0,255), random.randint)

running = True
while running:
    pass

pygame.quit()