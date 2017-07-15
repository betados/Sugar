import math


class Interaction:
    def __init__(self, resolution):
        self.floor = 2*resolution[1]/3

    def check(self, grainList):

        for grain1 in grainList:

            # Between grains
            for grain2 in grainList:
                if grain1 == grain2:
                    continue
                if self.touching(grain1, grain2):
                    higher = self.theHigherOne(grain1, grain2)
                    if higher[1].isInFloor:
                        # grain1.color = 100, 0, 0
                        # grain2.color = 100, 0, 0
                        higher[0].setFloorTouch()

            # With the floor
            if grain1.pos[1] >= self.floor:
                grain1.setFloorTouch()

    def touching(self, g1, g2):
        if self.distance(g1, g2) <= (g1.getRadio()+g2.getRadio() ):
            return True
        else:
            return False

    def theHigherOne(self, g1, g2):
        if g1.getPos()[1] < g2.getPos()[1]:
            return [g1, g2]
        else:
            return [g2, g1]

    @staticmethod
    def distance(g1, g2):
        return math.sqrt(math.pow(g2.pos[0]-g1.pos[0], 2) + math.pow(g2.pos[1]-g1.pos[1], 2))
