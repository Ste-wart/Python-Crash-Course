import pygame, sys
from pygame.locals import *


# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World')
#
# while True:  # main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         pygame.display.update()

spam = pygame.Rect(10, 20, 200, 300)
print(spam == (10, 20, 200, 300))
print(spam.right)
print(spam.left)
print(spam.midbottom)
print(spam.bottomright)
print(spam.bottomleft)