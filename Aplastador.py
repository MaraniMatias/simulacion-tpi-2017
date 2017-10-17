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
        self.arryCamiones = []
        self.camionesLlegando = []

    def hayCamionesEnCola(self):
        return len(self.arryCamiones) > 0

    def partidaDeCamion(self):
        # calculo tiempo de viaje del camion que se va
        return self.arryCamiones.pop(0)

    def addCola(self,proximoCamion):
        self.arryCamiones.append(proximoCamion)
