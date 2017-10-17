# Asuma que en tiempo cero todos los camiones están en sus respectivas palas con los camiones de 50 tn en primer lugar.
from array import *
from Pala import Pala
from Aplastador import Aplastador
from Reporte import Reporte

class Simulator(Object):

    def __init__(self):
        self.showReportesIntermedios = False
        self.reloj = 0.0
        #self.proximoEvento = ""
        self.listaDeEventos = array('f')
        self.TSAcumulado = 0.0
        self.tiempoUltimoEvento = 0
        self.TMEntreArribos = 7.0
        self.TMDeServicio = 9.0
        self.iniciado = False

        self.reporte = Reporte()
        self.arryPalas = [Pala(i) for i in range(3)]
        self.arryAplastadores = [Aplastador()] # alternativa usa otro aplastador

    # Sub Principal()
    def run(self):
        self.inicializar()
        # Loop, la simulacion, reloj es el finde la simulacion
        while (self.Reloj <= 8):
            # la rutina tiempo llama directamente a los eventos
            index = self.tiempos() # -> NO tiene sentido separar en dos, Pero el profesor lo pide asi :/, demas la separa y compara dos vesces lo mismo, string con estring una perdida de recursos
            # encontre una forma de cumplir con lo del profesor y con mejor rendimiento
            if index == 0:
                self.arribosPala(1) #self.proximoEvento = 'ARRIBOS_PALA_1'
            elif index == 1:
                self.arribosPala(2) #self.proximoEvento = 'ARRIBOS_PALA_2'
            elif index == 2:
                self.arribosPala(3) #self.proximoEvento = 'ARRIBOS_PALA_3'
            elif index == 3:
                self.partidasPala(1) #self.proximoEvento = 'PARTIDAS_PALA_1'
            elif index == 4:
                self.partidasPala(2) #self.proximoEvento = 'PARTIDAS_PALA_2'
            elif index == 5:
                self.partidasPala(3) #self.proximoEvento = 'PARTIDAS_PALA_3'
            elif index == 6:
                self.arribosAplastador(1) #self.proximoEvento = 'ARRIBOS_APLASTADOR'
            elif index == 7:
                self.partidasAplastador(1) #self.proximoEvento = 'PARTIDAS_APLASTADOR'
            # Para ver valores intermedios
            self.toString()
        # Al salir del while es el fin de la simulacion, emitir reporte
        #self.reporte

    def inicializar(self):
        # 0 - ARRIBOS_PALA_1
        # 1 - ARRIBOS_PALA_2
        # 2 - ARRIBOS_PALA_3
        # 3 - PARTIDAS_PALA_1
        # 4 - PARTIDAS_PALA_2
        # 5 - PARTIDAS_PALA_3
        # 6 - ARRIBOS_APLASTADOR
        # 7 - PARTIDAS_APLASTADOR
        # Tengo que generarlo con el primer camion de todas las palas
        # Calculo el tiempo de primer arribo
        for i in range(3):
            # como se asume que en el tiempo cero todos los camiones están en su pala.
            self.listaDeEventos.append( 0 )
        for j in range(4,8):
            self.listaDeEventos.append(9999999) #forzar que no ocurran otros eventos
        #self.toString() # al solo efecto de ver como evolucionan los valores de las variables

    def tiempos(self):
        self.tiempoUltimoEvento = self.reloj
        # Para buscar el proximo evento,
        self.reloj = min(self.listaDeEventos)
        return self.listaDeEventos.index(self.reloj)

    def arribosPala(self, nroPala):
        nroPala = nroPala - 1 # Para pasarlo a index
        if self.arryPalas[nroPala].desocupado:
            self.arryPalas[nroPala].desocupado = False
            self.listaDeEventos[nroPala + 3] =  self.Reloj + self.arryPalas[nroPala].calcularTimpoCarga()
        else:
            #  Agregar camión i de la pala j en la cola j
            #XXX Esta mal
            self.arryPalas[nroPala].addCola(self.proximoCamion)

    def partidasPala(self, nroPala):
        nroPala = nroPala - 1 # Para pasarlo a index
        if self.arryPalas[nroPala].hayCamionesEnCola():
            # Como se genero una partida, parte el camion y  calculo tiempo de arribo al aplastador
            camion = self.arryPalas[nroPala].partidaDeCamion()
            self.listaDeEventos[6] = self.Reloj + camion.getArriboAlAplastador()
            self.arryAplastadores[0].camionesLlegando.append(camion)
            # Otro Camion empieza a llenarse
            self.listaDeEventos[nroPala + 3] =  self.Reloj + self.arryPalas[nroPala].calcularTimpoCarga()
        else:
            self.arryPalas[nroPala].desocupado = True

    def arribosAplastador(self,nroAplastador):
        nroAplastador = nroAplastador - 1 #Para pasarlo a index
        if self.arryAplastadores[nroAplastador].desocupado:
            # Generar de partida del camion i del aplastador
            # Tiempo de descarga de ese camion
            self.listaDeEventos[7] =  self.Reloj + self.proximoCamion.getNewTiempoDescarga()
            # Poner al aplastador en OCUPADO
            self.arryAplastadores[nroAplastador].desocupado = False
        else:
            # Almacenar tiempo llegada del camión i de la pala j, lo tendo en el camion
            # Poner camión i de la pala j en cola del aplastador
            self.arryAplastadores[nroAplastador].addCola(self.proximoCamion)

    def partidasAplastador(self, nroAplastador):
        nroAplastador = nroAplastador - 1 #Para pasarlo a index
        if self.arryAplastadores[nroAplastador].hayCamionesEnCola():
            #Quitar camión de la cola
            camion = self.arryAplastadores[nroAplastador].partidaDeCamion()
            #Generar arribo a la pala j del camion que salio del aplastador
            self.listaDeEventos[camion.palaAsignada] =  self.Reloj + camion.getArriboAPala()
            #Generar nueva partida
            self.listaDeEventos[7] =  self.Reloj + self.arryPalas[nroPala].calcularTimpoCarga()
        else:
            self.arryAplastadores[nroAplastador].desocupado = True
            #Calcular y actualizar el material procesado

    # Para ver valores por consola, suele ser util
    def toString(self):
        if not(self.showReportesIntermedios):
            print "Valor de la simulacion: "
            print colors.LightCyan+"Relo\t"+colors.NC+str(self.Reloj)+colors.NC
            print colors.LightCyan+"ProximoEvento\t"+colors.Yellow+str(self.ProximoEvento)+colors.NC
            print colors.LightCyan+"TSAcumulado\t"+colors.NC+str(self.TSAcumulado)+colors.NC
            print colors.LightCyan+"TiempoUltimoEvento\t"+colors.NC+str(self.TiempoUltimoEvento)+colors.NC
            print colors.LightCyan+"Paso\t"+colors.NC+str(self.Paso)+colors.NC
            print colors.NC+"\n"
