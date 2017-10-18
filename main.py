import time
import sys

from Reporte import colors
from Simulator import Simulator

class Programa(object):

    def __init__(self):
        self.observacion = 40
        self.corridas = 80
        self.silencio = False
        self.progresbar = False
        self.buscarLote = False

if __name__ == "__main__":
    print colors.Yellow + 'Simulacion Camiones y Aplastadora' + colors.NC
    ## setup toolbar
    #sys.stdout.write("[%s]" % (" " * 80))
    #sys.stdout.flush()
    #sys.stdout.write("\b" * (80+1))

    programa = Programa()
    for corrida in range(1,programa.corridas+1):
        sim = Simulator(720)
        sim.inicializar()
        #sys.stdout.flush()
        for obs in range(1,programa.observacion+1):
            print colors.Yellow + 'Corrida: ' + str(corrida) + colors.LightGreen + ' Observacion: ' + colors.NC + str(obs)
            sim.run()
        sim.reporte.toCsv(corrida)
    #sys.stdout.write("\n")
