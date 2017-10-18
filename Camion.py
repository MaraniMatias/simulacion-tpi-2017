import numpy as np

class Camion(object):

    def __init__(self, tipo, nroPala):
        self.palaAsignada = nroPala
        self.tiempoLlegadaAlAplastador = 99999999
        self.tiempoLlegadaAlaPala = 99999999

        self.toneladas = 20 if tipo == 20 else 50
        self.lamdaDestribucionCarga = 5 if tipo == 20 else 10
        self.lamdaDestribucionDescarga = 2 if tipo == 20 else 5
        self.viaje = 2.5 if tipo == 20 else 3.0
        self.regreso = 1.5 if tipo == 20 else 2.0

    def getTiempoCarga(self):
        return np.random.exponential(self.lamdaDestribucionCarga)

    def getTiempoDescarga(self):
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
