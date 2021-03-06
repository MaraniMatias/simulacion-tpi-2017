import sys
import numpy as np
# import time
# import math

class Camion(object):
    # z0 = int(time.time())  # Solo para el numero ramdon

    def __init__(self, tipo, nroPala):
        self.palaAsignada = nroPala
        self.tiempoLlegadaAlAplastador = sys.maxint
        self.tiempoLlegadaAlaPala = sys.maxint

        if tipo != 100:
            self.toneladas = 20 if tipo == 20 else 50
            self.lamdaDestribucionCarga = 5 if tipo == 20 else 10
            self.lamdaDestribucionDescarga = 2 if tipo == 20 else 5
            self.viaje = 2.5 if tipo == 20 else 3.0
            self.regreso = 1.5 if tipo == 20 else 2.0
        else:
            self.toneladas = 100
            self.lamdaDestribucionCarga = 10
            self.lamdaDestribucionDescarga = 5
            self.viaje = 2.5
            self.regreso = 1.5

    def getTiempoCarga(self):
        return np.random.exponential(self.lamdaDestribucionCarga)
        # return self.valorExponencial(self.lamdaDestribucionCarga)

    def getTiempoDescarga(self):
        return np.random.exponential(self.lamdaDestribucionDescarga)
        # return self.valorExponencial(self.lamdaDestribucionDescarga)

    def getArriboAlAplastador(self):
        return self.viaje

    def getArriboAPala(self):
        return self.regreso

    """
    def getNumAleatorio(self):
        try:
            #a = math.pow(7,5)
            #m = math.pow(2,31) - 1
            a = math.pow(5,15)
            m = math.pow(2,35)
            c = 0
            zi = int( a * self.z0 +c ) %  m
            self.z0 = zi
            r = zi/m
            if r < 0 and 1 < r:
                raise ValueError('Rando mal generado. => ' + str(r))
            return r
        except ValueError:
            print(colors.Red + str(ValueError) + colors.NC)

    def valorExponencial(self, media):
        try:
            return -(1 / media) * np.log1p(self.getNumAleatorio())
        except ValueError:
            print(colors.Red + str(ValueError) + colors.NC)
    """

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
