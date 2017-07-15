import pygame
import random


class Grain:
    g = 0.00002

    def __init__(self, screen):
        self.pos = [400, 0]
        self.vel = [0, 0.00]
        self.accel = [0, 0]
        self.screen = screen
        self.color = 150, 155, 155
        self.side = 7
        self.isInFloor = False
        self.forceList = []

        self.mass = self.side * self. side
        self.force = [0, 0]

        self.forceList.append([0, self.mass * Grain.g])

    def draw(self, t):
        self.actualize(t)
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.side, self.side), 2)

    def actualize(self, t):


        for i in range(2):
            # force sum
            self.force = [0, 0]
            for force in self.forceList:
                self.force[i] += force[i]


            self.accel[i] = self.force[i]/self.mass
            # movement equations
            self.vel[i] += self.accel[i] * t
            self.pos[i] += self.vel[i] * t + 0.5 * self.accel[i] * t * t

        if self.isInFloor:
            self.vel[0]=0
        else:
            # random horizontal drift
            self.vel[0] += random.randrange(-10, 10)/25000

        # TODO ¿rozamiento viscoso?

    def getRadio(self):
        return self.side/2

    def setFloorTouch(self):
        if not self.isInFloor:
            self.vel[1] = 0
            # self.force[1] = 0
            self.isInFloor = True
            self.forceList.append([0, -self.mass * Grain.g])

    def getVel(self):
        return self.vel

    def setVel(self, v):
        self.vel = v

    def getPos(self):
        return self.pos

    def setPos(self, p):
        self.pos = p
