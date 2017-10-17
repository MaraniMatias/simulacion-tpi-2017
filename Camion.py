import numpy as np

"""#import datetime
# Public toneladas 20|50
# Public lamdaDestribucionCarga para la funcion exponential de carga 5|10
# Public lamdaDestribucionDescarga para la funcion exponential de carga 2|5
# Public tiempo de viaje en horas 2.5|3
# Public tiempo de regreso en horas 1.5|2
"""
class Camion(Object):

    def __init__(self, tipo, nroPala):
        self.palaAsignada = nroPala
        self.tiempoLlegadaAlAplastador = 99999999
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
