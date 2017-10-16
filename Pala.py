import Camiones

# La cola de cada pala es FIFO.
class Pala(Object):

    def __init__(self):
        self.Cola = array('f')
        self.NroDeCamionesEnCola = 0
        self.AreaQDeT = 0.0
        self.CompletaronDemora = 0
        self.DemoraAcumulada = 0.0

        self.arryPalas = [Camion()]
