#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from grain import Grain
from interaction import Interaction

pygame.init()
clock = pygame.time.Clock()
resolution = (800, 600)
pygame.display.set_caption('Sugar')
screen = pygame.display.set_mode(resolution)
done = False

creationPeriod = 500
grainQuantity = 50

interaction = Interaction(resolution)
grainList = []
pygame.time.set_timer(USEREVENT+1, creationPeriod)

# --- MAIN LOOP
while not done:

    screen.fill((0, 0, 0))
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == USEREVENT + 1:
            if len(grainList) < grainQuantity:
                grainList.append(Grain(screen))

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
    if keys[pygame.K_f]:
        print(grainList[0].lastForceList)
    #     avance = avance[0], avance[1]-1

    # exit
    if keys[pygame.K_ESCAPE]:
        done = True
    t = clock.get_time()
    # print(t)
    # print(tTotal)


    try:
        interaction.check(grainList)
    except Exception as e:
            # FIXME arreglar los overflows que dan algunos granos
            print("Al interactuar: "+str(e))


    # print(grainList[0].force)

    # --- DRAW CODE
    for grain in grainList:
        try:
            grain.draw(t)
        except Exception as e:
            # FIXME arreglar los overflows que dan algunos granos
            print("Al pintar: "+str(e))
    # print(t)
    pygame.display.flip()

    # --- (frames per second)
    clock.tick(25)

# close
pygame.quit()
