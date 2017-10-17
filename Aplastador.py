#  La cola del aplastador está ordenada en forma decreciente por tamaño de camión. En caso de que existan varios camiones con iguales características, la cola es FIFO.
class Aplastador(Object):

    def __init__(self):
        self.cola = array('f')
        self.nroDeCamionesEnCola = 0
        self.areaQDeT = 0.0
        self.completaronDemora = 0
        self.demoraAcumulada = 0.0
        #self.estado = "D"
        self.desocupado = True
        self.arryCamiones = [] # cola de camiones
        self.camionesLlegando = []

    def hayCamionesEnCola(self):
        return len(self.arryCamiones) > 0

    def hayCamionesLlegando(self):
        return len(self.camionesLlegando) > 0

    def partidaDeCamion(self):
        # calculo tiempo de viaje del camion que se va
        return self.arryCamiones.pop(0)

    def addCamionllegando(self,camion):
        self.camionesLlegando.append(camion)
        # Ordenar llegada
        self.camionesLlegando = sorted(self.camionesLlegando, key=lambda camion: camoin.tiempoLlegadaAlAplastador)
        # Para saver cuando ocurre el primer arribo al aplatador
        return self.camionesLlegando[0].tiempoLlegadaAlAplastador

    def sacarCamionesLlegando(self):
        camion = self.camionesLlegando.pop(0)
        camion.tiempoLlegadaAlAplastador = 99999999

    def addCola(self):
        camion = self.camionesLlegando.pop(0)
        self.arryCamiones.append(camion)
        # TODO ordenar por prioridad y fifo , la cola
