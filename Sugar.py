#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame
from grain import Grain
from interaction import Interaction

pygame.init()
clock = pygame.time.Clock()
resolution = (800, 600)
pygame.display.set_caption('Sugar')
screen = pygame.display.set_mode(resolution)
done = False

interaction = Interaction(resolution)
grainList = []

while not done:

    screen.fill((0, 0, 0))
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    # --- MAIN LOOP
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    # --- GAME LOGIC
    keys = pygame.key.get_pressed()

    # if keys[pygame.K_w]:
    #     # x=x+0.2
    #     avance = avance[0]+1, avance[1]
    # if keys[pygame.K_a]:
    #     # y=y+0.2
    #     avance = avance[0], avance[1]+1
    # if keys[pygame.K_s]:
    #     # x=x-0.2
    #     avance = avance[0]-1, avance[1]
    # if keys[pygame.K_d]:
    #     # y=y-0.2
    #     avance = avance[0], avance[1]-1

    # exit
    if keys[pygame.K_ESCAPE]:
        done = True

    if len(grainList) < 50:
        grainList.append(Grain(screen))
    t = clock.get_time()
    interaction.check(grainList)

    print(grainList[0].force)

    # --- DRAW CODE
    for grain in grainList:
        grain.draw(t)
    # print(t)
    pygame.display.flip()

    # --- (frames per second)
    clock.tick(15)

# close
pygame.quit()
