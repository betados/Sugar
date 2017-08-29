import pygame
import random
import math


class Grain:
    g = 0.0002

    def __init__(self, screen):
        self.pos = [400, 0]
        self.vel = [0, 0.00]
        self.accel = [0, 0]
        self.screen = screen
        self.color = 77, 77, 77
        self.side = 8
        self.isInFloor = False
        self.wasInFloor = False
        self.isTouching = False
        self.forceList = []

        self.mass = self.side * self.side
        self.force = [0, 0]



    def draw(self, t):
        self.actualize(t)

        # chapuza para evitar los overflows
        if self.pos[0] >9999 or self.pos[1]>9999\
            or self.pos[0] <-9999 or self.pos[1]<-9999:
            self.pos = [-self.side, -self.side]
            self.vel = [-self.side, -self.side]
            self.accel = [-self.side, -self.side]


        pygame.draw.rect(self.screen, self.color, (self.pos[0]-self.side/2, self.pos[1]-self.side/2, self.side, self.side), 2)
        # for force in self.forceList:
        #     pygame.draw.aaline(self.screen, self.color, self.pos, [self.pos[0]+force[0]*1000,self.pos[1]+force[1]*1000 ] )
        self.forceList = []

    def actualize(self, t):
        self.forceList.append([0, self.mass * Grain.g])
        # print("gravedad "+str(self.mass * Grain.g))
        self.checkFloor()
        self.forceList.append(self.rozamientoViscoso())

        if not self.isInFloor:
            # random horizontal drift
            self.forceList.append( [random.randrange(-10, 10)/25000, 0] )

        for i in range(2):
            # force sum
            self.force = [0, 0]
            for force in self.forceList:
                self.force[i] += force[i]


            self.accel[i] = self.force[i]/self.mass
            # movement equations
            self.vel[i] += self.accel[i] * t
            self.pos[i] += self.vel[i] * t + 0.5 * self.accel[i] * t * t




        # rest force List
        # self.lastForceList= self.forceList
        # self.forceList = []
    #
    def rozamientoViscoso(self):
        mult = [10, 10]
        for i in range(2):
            if self.vel[i] >= 0:
                mult[i] = mult[i] * -1
            if self.isTouching:
                mult[i] = mult[i] * 50
            else:
                if self.isInFloor:
                    mult[i] = mult[i] * 5

        return [math.pow(self.vel[0], 2)*mult[0], math.pow(self.vel[1], 2)*mult[1]]


    def getRadio(self):
        return self.side/2

    def checkFloor(self):
        if self.isInFloor and not self.wasInFloor:
            # FIXME esto es un apaño que frena el grano cuando este toca el suelo
            self.vel[1] = 0
            self.wasInFloor = True
        if self.isInFloor:
            self.vel[1] = 0
            self.forceList.append([0, -self.mass * Grain.g])

    def setFloorTouch(self):
        self.isInFloor = True

    def setNotFloor(self):
        self.isInFloor = False
        self.wasInFloor = False

    def getVel(self):
        return self.vel

    def setVel(self, v):
        self.vel = v

    def getPos(self):
        return self.pos

    def setPos(self, p):
        self.pos = p
