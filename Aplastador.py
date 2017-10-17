# import pdb

#  La cola del aplastador esta ordenada en forma decreciente por tamanio de camion. En caso de que existan varios camiones con iguales caracteristicas, la cola es FIFO.
class Aplastador(object):

    def __init__(self):
        self.desocupado = True
        self.arrayCamiones = []  # cola de camiones
        self.camionesLlegando = []

    def hayCamionesEnCola(self):
        return len(self.arrayCamiones) > 0

    def hayCamionesLlegando(self):
        return len(self.camionesLlegando) > 0

    def partidaDeCamion(self):
        # calculo tiempo de viaje del camion que se va
        return self.arrayCamiones.pop(0)

    def addCamionllegando(self, camion):
        self.camionesLlegando.append(camion)
        # Ordenar llegada
        self.camionesLlegando = sorted(self.camionesLlegando, key=lambda camion: camion.tiempoLlegadaAlAplastador)
        # Para saver cuando ocurre el primer arribo al aplatador
        return self.camionesLlegando[0].tiempoLlegadaAlAplastador

    def sacarCamionesLlegando(self):
        camion = self.camionesLlegando.pop(0)
        camion.tiempoLlegadaAlAplastador = 99999999
        return camion

    def addCola(self):
        camion = self.camionesLlegando.pop(0)
        self.arrayCamiones.append(camion)
        self.ordenarColaPorPrioridadFIFO()

    def calcularTimpoDescarga(self):
        # la cola debe estar ordenada
        self.camionCargan = self.arrayCamiones[0]
        self.arrayCamiones[0].getNewTiempoDescarga()

    def ordenarColaPorPrioridadFIFO(self):
        # TODO pensar bien, capas que asi quede bien, pero no lo se
        self.arrayCamiones = sorted(self.arrayCamiones, key=lambda camion: camion.toneladas)
