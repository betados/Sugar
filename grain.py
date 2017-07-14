import pygame
import random

class Grain:
    def __init__(self, screen):
        self.pos = [400, 0]
        self.vel = [0, 0.04]
        self.accel = [0, 0]
        self.screen = screen
        self.color = 150, 155, 155
        self.side = 3

    def draw(self, t):
        self.actualize(t)
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.side, self.side), 2)

    def actualize(self, t):
        # movement equations
        for i in range(2):
            self.vel[i] += self.accel[i] * t
            self.pos[i] += self.vel[i] * t + 0.5 * self.accel[i] * t * t

        # random horizontal drift
        self.vel[0] += random.randrange(-10, 10)/25000

        # TODO ¿rozamiento viscoso?

    def getRadio(self):
        return self.side/2
