import numpy as np
from Reporte import colors

class Camion(object):

    def __init__(self, tipo, nroPala):
        self.palaAsignada = nroPala
        self.tiempoLlegadaAlAplastador = 99999999
        self.tiempoLlegadaAlaPala = 99999999
        if tipo == 20:
            self.toneladas = 20
            self.lamdaDestribucionCarga = 5
            self.lamdaDestribucionDescarga = 2
            self.viaje = 2.5
            self.regreso = 1.5
        else:
            self.toneladas = 50
            self.lamdaDestribucionCarga = 10
            self.lamdaDestribucionDescarga = 5
            self.viaje = 3.0
            self.regreso = 2.0

    def getNewTiempoCarga(self):
        return np.random.exponential(self.lamdaDestribucionCarga)

    def getNewTiempoDescarga(self):
        return np.random.exponential(self.lamdaDestribucionDescarga)

    def getArriboAlAplastador(self):
        return self.viaje

    def getArriboAPala(self):
        return self.regreso

    """
    def toString(self):
        print "palaAsignada " + str(self.palaAsignada)
        print "tiempoLlegadaAlAplastador " + str(self.tiempoLlegadaAlAplastador)
        print "tiempoLlegadaAlaPala " + str(self.tiempoLlegadaAlaPala)
        print "toneladas " + str(self.toneladas)
        print "lamdaDestribucionCarga " + str(self.lamdaDestribucionCarga)
        print "lamdaDestribucionDescarga " + str(self.lamdaDestribucionDescarga)
        print "viaje " + str(self.viaje)
        print "regreso " + str(self.regreso)
    """
