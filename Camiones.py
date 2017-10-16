import numpy as np

"""#import datetime
# Public toneladas 20|50
# Public lamdaDestribucionCarga para la funcion exponential de carga 5|10
# Public lamdaDestribucionDescarga para la funcion exponential de carga 2|5
# Public tiempo de viaje en horas 2.5|3
# Public tiempo de regreso en horas 1.5|2
"""

class Camion(Object):

    def __init__(self, toneladas=20, lamdaDestribucionCarga=5,lamdaDestribucionDescarga=2,viaje=2.5,regreso=1.5):
        self.toneladas = toneladas
        self.lamdaDestribucionCarga = lamdaDestribucionCarga
        self.lamdaDestribucionDescarga = lamdaDestribucionDescarga
        self.viaje = viaje
        self.regreso = regreso

    def getNewTiempoCarga(self):
        return np.random.exponential(self.lamdaDestribucionCarga)

    def getNewTiempoDescarga(self):
        return np.random.exponential(self.lamdaDestribucionDescarga)
