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
                    # if lower is in the floor:
                    if higher[1].isInFloor:
                        # grain1.color = 100, 0, 0
                        # grain2.color = 100, 0, 0
                        # pass
                        # FIXME esto debería ser una funcion que calculase la fuerza entre las dos bolas
                        pass
                    grain1.forceList.append(self.unitVector(grain1, grain2))
                        # higher[0].setFloorTouch(False)

            # With the floor
            if grain1.pos[1] >= self.floor:
                # FIXME no debería recibir parametro
                grain1.setFloorTouch(True)

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

    def unitVector(self, g1, g2):
        vector = [g2.getPos()[0] - g1.getPos()[0], g2.getPos()[1] - g1.getPos()[1]]
        angle = math.atan2(vector[1],vector[0])
        # print(vector)
        # TODO lo de los angulos se puede meter en una clase nueva para reutilizar
        modulo = math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))
        if modulo != 0:
            return [(vector[0] / modulo) * math.sin(angle) * -g1.mass * g1.g, (vector[1] / modulo)* math.sin(angle) * -g1.mass * g1.g]
        else:
            return [999999, 999999]

    @staticmethod
    def distance(g1, g2):
        return math.sqrt(math.pow(g2.pos[0]-g1.pos[0], 2) + math.pow(g2.pos[1]-g1.pos[1], 2))
