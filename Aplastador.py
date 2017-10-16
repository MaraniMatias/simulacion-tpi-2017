#  La cola del aplastador está ordenada en forma decreciente por tamaño de camión. En caso de que existan varios camiones con iguales características, la cola es FIFO.
class Aplastador(Object):

    def __init__(self):
        self.Cola = array('f')
        self.NroDeCamionesEnCola = 0
        self.AreaQDeT = 0.0
        self.CompletaronDemora = 0
        self.DemoraAcumulada = 0.0
