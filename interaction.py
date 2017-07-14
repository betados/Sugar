import math

class Interaction:
    def __init__(self, resolution):
        self.floor = resolution[1]/3
    def check(self, grainList):

        for grain1 in grainList:

            # Between grains
            for grain2 in grainList:
                if grain1 == grain2:
                    continue
                if self.touching(grain1,grain2):
                    grain1.color = 255, 0, 0

            # With the floor
            if grain1.pos[1] >= self.floor:
                grain1.vel[1] = 0

    def touching(self, g1, g2):
        if self.distance(g1, g2) <= (g1.getRadio()+g2.getRadio() )*0.5:
            return True
        else:
            return False

    def distance(self, g1, g2):
        return math.sqrt(math.pow(g2.pos[0]-g1.pos[0], 2) +  math.pow(g2.pos[1]-g1.pos[1], 2) )