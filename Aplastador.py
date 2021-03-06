import sys
#  La cola del aplastador esta ordenada en forma decreciente por tamanio de camion. En caso de que existan varios camiones con iguales caracteristicas, la cola es FIFO.
class Aplastador(object):

    def __init__(self):
        self.desocupado = True
        self.camionDescargando = None
        self.colaDeCamiones = []  # cola de camiones
        self.camionesLlegando = []

    def hayCamionesEnCola(self):
        return len(self.colaDeCamiones) > 0

    def hayCamionesLlegando(self):
        return len(self.camionesLlegando) > 0

    def pasarCamionADescarga(self):
        self.camionDescargando = self.colaDeCamiones.pop(0)
        self.camionDescargando.tiempoLlegadaAlAplastador = sys.maxint
        return self.camionDescargando

    def addCamionllegando(self, camion):
        self.camionesLlegando.append(camion)
        # Ordenar llegada
        self.camionesLlegando = sorted(self.camionesLlegando, key=lambda camion: camion.tiempoLlegadaAlAplastador)
        # Para saver cuando ocurre el primer arribo al aplatador
        return self.camionesLlegando[0].tiempoLlegadaAlAplastador

    def addCola(self):
        camion = self.camionesLlegando.pop(0)
        camion.tiempoLlegadaAlAplastador = sys.maxint
        self.colaDeCamiones.append(camion)
        #self.ordenarColaMenorMayor()
        self.ordenarColaPorPrioridadFIFO()

    def ordenarColaPorPrioridadFIFO(self):
        self.colaDeCamiones = sorted(self.colaDeCamiones, key = lambda camion: camion.toneladas, reverse = True)

    def ordenarColaMenorMayor(self):
        self.colaDeCamiones = sorted(self.colaDeCamiones, key = lambda camion: camion.toneladas)
