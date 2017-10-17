from colors import colors
from Simulator import Simulator

class Programa(object):

    def __init__(self):
        self.observacion = 0
        self.corridas = 1
        self.silencio = False
        self.progresbar = False
        self.buscarLote = False

if __name__ == "__main__":
    print colors.Cyan+'~~~~~~~~~~~~~~~~Simulacion Camiones y Aplastadora~~~~~~~~~~~~~~~~'+ colors.NC

    programa = Programa()
    sim = Simulator()

    if program.progresbar:
    #TODO progres bar

    for x in range(programa.corridas):
        programa.observacion += 1
        sim.run()

        if programa.progresbar:
            #TODO progres bar

    if programa.progresbar:
        #TODO progres bar
