import pygame
import random
import math


class Grain:
    g = 0.00002

    def __init__(self, screen):
        self.pos = [400, 0]
        self.vel = [0, 0.00]
        self.accel = [0, 0]
        self.screen = screen
        self.color = 150, 155, 155
        self.side = 40
        self.isInFloor = False
        self.forceList = []

        self.mass = self.side * self.side
        self.force = [0, 0]



    def draw(self, t):
        self.actualize(t)
        pygame.draw.rect(self.screen, self.color, (self.pos[0]-self.side/2, self.pos[1]-self.side/2, self.side, self.side), 2)
        for force in self.lastForceList:
            pygame.draw.aaline(self.screen, self.color, self.pos, [self.pos[0]+force[0]*1000,self.pos[1]+force[1]*1000 ] )

    def actualize(self, t):

        self.forceList.append([0, self.mass * Grain.g])
        self.forceList.append(self.rozamientoViscoso())

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
            pass
            # self.vel[0]=0
        else:
            # random horizontal drift
            self.vel[0] += random.randrange(-10, 10)/25000

        # TODO ¿rozamiento viscoso?

        # rest force List
        self.lastForceList= self.forceList
        self.forceList = []

    def rozamientoViscoso(self):
        mult = 10

        return [math.pow(self.vel[0],2)*mult,-math.pow(self.vel[1],2)*mult]


    def getRadio(self):
        return self.side/2

    def setFloorTouch(self, trueFloor):
        # FIXME este if ya no tiene sentido
        if trueFloor:
            # FIXME esto es un apaño que frena el grrasno cuando este toca el suelo
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
