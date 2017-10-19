from Camion import Camion

# La cola de cada pala es FIFO.
class Pala(object):

    def __init__(self, nroPala):
        self.desocupado = True
        self.camionesLlegando = []
        # Para cada pala se asignan dos camiones de 20 tn y uno de 50 tn
        # En tiempo cero todos los camiones estan en sus respectivas palas con los camiones de 50 tn en primer lugar.
        self.colaDeCamiones = [Camion(50, nroPala), Camion(20, nroPala), Camion(20, nroPala)]  # Cola de camiones
        # Como tiene que empezar con un camion en carga
        self.camionCargando = self.colaDeCamiones.pop(0)

    def hayCamionesEnCola(self):
        return len(self.colaDeCamiones) > 0

    def hayCamionesLlegando(self):
        return len(self.camionesLlegando) > 0

    def pasarCamionACarga(self):
        self.camionCargando = self.colaDeCamiones.pop(0)
        self.camionCargando.tiempoLlegadaAlaPala = 99999999
        return self.camionCargando

    def addCamionllegando(self, camion):
        self.camionesLlegando.append(camion)
        # Ordenar llegada
        self.camionesLlegando = sorted(self.camionesLlegando, key=lambda camion: camion.tiempoLlegadaAlaPala)
        # Para saver cuando ocurre el primer arribo a la pala
        return self.camionesLlegando[0].tiempoLlegadaAlaPala

    def addCola(self):
        camion = self.camionesLlegando.pop(0)
        camion.tiempoLlegadaAlaPala = 99999999
        self.colaDeCamiones.append(camion)
        #self.ordenarColaMayorMenor()
        #self.ordenarColaMenorMayor()

    def ordenarColaMayorMenor(self):
        self.colaDeCamiones = sorted(self.colaDeCamiones, key = lambda camion: camion.toneladas, reverse = True)

    def ordenarColaMenorMayor(self):
        self.colaDeCamiones = sorted(self.colaDeCamiones, key = lambda camion: camion.toneladas)
