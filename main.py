import colors
import Simulator

#---------------------------------------------
# Progrma
#---------------------------------------------
class Programa(object):

    def __init__(self):
        self.observacion = 0
        self.corridas = 1
        self.silencio = False
        self.progresbar = False
        self.buscarLote = False

#---------------------------------------------
# Ejecucion del modelo
#---------------------------------------------
if __name__ == "__main__":
    print colors.Cyan+'~~~~~~~~~~~~~~~~Simulacion Camiones y Aplastadora~~~~~~~~~~~~~~~~'+ colors.NC

    program = Programa()
    sim = Simulator()

    if program.progresbar:
    #TODO progres bar

    for x in range(programa.corridas):
        programa.observacion += 1
        sim.inicializar()
        sim.run()

        if program.progresbar:
            #TODO progres bar

    if program.progresbar:
        #TODO progres bar
