import math


class Interaction:
    def __init__(self, resolution):
        self.floor = 1*resolution[1]/3

    def check(self, grainList):

        for grain1 in grainList:

            # Between grains
            for grain2 in grainList:
                if grain1 == grain2:
                    continue
                if self.touching(grain1, grain2):
                    higher, lower = self.theHigherOne(grain1, grain2)
                    # if lower is in the floor:
                    if lower.isInFloor:
                        # grain1.color = 100, 0, 0
                        # grain2.color = 100, 0, 0
                        # pass
                        # FIXME esto debería ser una funcion que calculase la fuerza entre las dos bolas
                        # self.setForces(higher=higher, lower=lower)
                        pass
                    # FIXME solo afectan los de abajo para arriba, abria que hacerlo bidireccional
                    higher.forceList.append(self.unitVector(higher, lower))
                    # lower.forceList.append(self.unitVector(lower, higher))
                    grain1.isTouching = True
                    grain2.isTouching = True
                else:
                    grain1.isTouching = False
                    grain2.isTouching = False

            # With the floor
            if grain1.pos[1] >= self.floor:
                grain1.setFloorTouch()
            else:
                grain1.setNotFloor()

    def touching(self, g1, g2):
        if self.distance(g1, g2) <= (g1.getRadio()+g2.getRadio() ):
            return True
        else:
            return False

    def theHigherOne(self, g1, g2):
        if g1.getPos()[1] < g2.getPos()[1]:
            return g1, g2
        else:
            return g2, g1

    def unitVector(self, higher, lower):
        vector = [higher.getPos()[0] - lower.getPos()[0], higher.getPos()[1] - lower.getPos()[1]]
        # angle = math.atan2(vector[1], vector[0])
        # print(vector)
        # TODO lo de los angulos se puede meter en una clase nueva para reutilizar
        modulo = math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))
        if modulo != 0:
            unitVector= [vector[0] / modulo, vector[1] / modulo]
            deformacion = higher.getRadio()*2 - self.distance(higher, lower)
            deformacion = deformacion *0.05
            if deformacion < 0:
                deformacion = deformacion*-1
            fuerza = [unitVector[0] * deformacion, unitVector[1] * deformacion]

            return fuerza
        else:
            return [0, 0]

    @staticmethod
    def distance(g1, g2):
        return math.sqrt(math.pow(g2.pos[0]-g1.pos[0], 2) + math.pow(g2.pos[1]-g1.pos[1], 2))

    # def setForces(self, higher, lower):
    #     vector = higher.getPos()[0]-lower.getPos()[0], higher.getPos()[1]-lower.getPos()[1]
    #     angle = math.atan2(vector[0], vector[1])
    #     mult = 0.0001
    #     higher.forceList.append([vector[0]*-math.sin(angle)*mult, vector[1]*-math.sin(angle)*mult])
    #     print("toque "+str(vector[0]*-math.sin(angle)*mult))

