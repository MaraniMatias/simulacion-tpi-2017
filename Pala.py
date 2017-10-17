from array import *
from Camion import Camion

# La cola de cada pala es FIFO.
class Pala(object):

    def __init__(self,nroPala):
        self.cola = array('f')
        self.nroDeCamionesEnCola = 0
        self.areaQDeT = 0.0
        self.completaronDemora = 0
        self.demoraAcumulada = 0.0
        #self.estado = "D"
        self.desocupado = True

        # Para cada pala se asignan dos camiones de 20 tn y uno de 50 tn
        # En tiempo cero todos los camiones estan en sus respectivas palas con los camiones de 50 tn en primer lugar.
        self.arryCamiones = [Camion(50, nroPala), Camion(20, nroPala), Camion(20, nroPala)] # Cola de camiones
        self.camionesLlegando = []
        self.camionCargando = None

    def calcularTimpoCarga(self):
        #Cola FIFO, calcular para el primer camion
        self.camionCargan = self.arryCamiones[0]
        return self.arryCamiones[0].getNewTiempoCarga()

    def hayCamionesEnCola(self):
        return len(self.arryCamiones) > 0

    def partidaDeCamion(self):
        # calculo tiempo de viaje del camion que se va
        return self.arryCamiones.pop(0)

    def addCamionllegando(self,camion):
        self.camionesLlegando.append(camion)
        # Ordenar llegada
        self.camionesLlegando = sorted(self.camionesLlegando, key=lambda camion: camoin.tiempoLlegadaAlAplastador)
        # Para saver cuando ocurre el primer arribo al aplatador
        return self.camionesLlegando[0].tiempoLlegadaAlAplastador

    def addCola(self):
        if len(self.camionesLlegando) > 0:
            camion = self.camionesLlegando.pop(0)
            self.arryCamiones.append(camion)

