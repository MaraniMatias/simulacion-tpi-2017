# Asuma que en tiempo cero todos los camiones estan en sus respectivas palas con los camiones de 50 tn en primer lugar.
from array import *
from Pala import Pala
from Aplastador import Aplastador
from Reporte import *

class Simulator(object):

    def __init__(self):
        self.showReportesIntermedios = False
        self.reloj = 0.0
        self.proximoEvento = ""
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
        while (self.reloj <= 3):
            # la rutina tiempo llama directamente a los eventos
            index = self.tiempos() # -> NO tiene sentido separar en dos, Pero el profesor lo pide asi :/, demas la separa y compara dos vesces lo mismo, string con estring una perdida de recursos
            # encontre una forma de cumplir con lo del profesor y con mejor rendimiento
            if index == 0:
                self.proximoEvento = 'ARRIBOS_PALA_1'
                self.arribosPala(1)
            elif index == 1:
                self.proximoEvento = 'ARRIBOS_PALA_2'
                self.arribosPala(2)
            elif index == 2:
                self.proximoEvento = 'ARRIBOS_PALA_3'
                self.arribosPala(3)
            elif index == 3:
                self.proximoEvento = 'PARTIDAS_PALA_1'
                self.partidasPala(1)
            elif index == 4:
                self.proximoEvento = 'PARTIDAS_PALA_2'
                self.partidasPala(2)
            elif index == 5:
                self.proximoEvento = 'PARTIDAS_PALA_3'
                self.partidasPala(3)
            elif index == 6:
                self.proximoEvento = 'ARRIBOS_APLASTADOR'
                self.arribosAplastador(1)
            elif index == 7:
                self.proximoEvento = 'PARTIDAS_APLASTADOR'
                self.partidasAplastador(1)
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

        #forzar que no ocurran eventos
        for x in range(8):
            self.listaDeEventos.append(9999999)

        # como se asume que en el tiempo cero todos los camiones estan en su pala.
        # Por eso tenemos que calcular las partidas
        # Calculo el tiempo de la primera partida
        # Tengo que generarlo con el primer camion de todas las palas
        self.partidasPala(1)
        self.partidasPala(2)
        self.partidasPala(3)
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
            self.listaDeEventos[nroPala + 3] =  self.reloj + self.arryPalas[nroPala].calcularTimpoCarga()
        else:
            #  Agregar camion i de la pala j en la cola j
            self.arryPalas[nroPala].addCola() # Pasa el camion que llega, ala cola

    def partidasPala(self, nroPala):
        nroPala = nroPala - 1 # Para pasarlo a index
        if self.arryPalas[nroPala].hayCamionesEnCola():
            # Como se genero una partida, parte el camion y  calculo tiempo de arribo al aplastador
            camion = self.arryPalas[nroPala].partidaDeCamion()
            camion.tiempoLlegadaAlAplastador = self.reloj + camion.getArriboAlAplastador()
            # Guardar una cola de camiones llegando y el primero en llegar seria el proximo evento
            self.listaDeEventos[6] = self.arryAplastadores[0].addCamionllegando(camion)
            # Otro Camion empieza a llenarse
            self.listaDeEventos[nroPala + 3] =  self.reloj + self.arryPalas[nroPala].calcularTimpoCarga()
        else:
            self.arryPalas[nroPala].desocupado = True
            # Calcular el arribo al aplastador
            camion = self.arryPalas[nroPala].camionCargando
            camion.tiempoLlegadaAlAplastador = self.reloj + camion.getArriboAlAplastador()
            # Guardar una cola de camiones llegando y el primero en llegar seria el proximo evento
            self.listaDeEventos[6] = self.arryAplastadores[0].addCamionllegando(camion)
            self.arryPalas[nroPala].camionCargando = None
            # Forzar, limpiar partias desde esta pala
            self.listaDeEventos[nroPala + 3] =  9999999

    def arribosAplastador(self, nroAplastador):
        nroAplastador = nroAplastador - 1 #Para pasarlo a index
        if self.arryAplastadores[nroAplastador].desocupado:
            # sacar el camion que llego de  camionesLlegando,
            self.arryAplastadores[nroAplastador].sacarCamionesLlegando()
            # acomodar arribos al Aplastador, al estar ordena es el primero
            self.listaDeEventos[6] = self.arryAplastadores[0].camionesLlegando[0].tiempoLlegadaAlAplastador
            # Generar de partida del camion i del aplastador
            # Tiempo de descarga de ese camion
            self.listaDeEventos[7] =  self.reloj + self.proximoCamion.getNewTiempoDescarga()
            # Poner al aplastador en OCUPADO
            self.arryAplastadores[nroAplastador].desocupado = False
        else:
            # Almacenar tiempo llegada del camion i de la pala j, lo tendo en el camion
            # Poner camion i de la pala j en cola del aplastador
            self.arryAplastadores[nroAplastador].addCola() #El aplastador sabe que camion llego
            if  self.arryAplastadores[0].camionesLlegando[0].hayCamionesLlegando():
                # acomodar arribos al Aplastador, al estar ordena es el primero
                self.listaDeEventos[6] = self.arryAplastadores[0].camionesLlegando[0].tiempoLlegadaAlAplastador
            else:
                # al no llegar camiones fuerso a que este evento no suseda
                 self.listaDeEventos[6] = 9999999

    def partidasAplastador(self, nroAplastador):
        nroAplastador = nroAplastador - 1 #Para pasarlo a index
        if self.arryAplastadores[nroAplastador].hayCamionesEnCola():
            # Quitar camion de la cola y el que se esta descargando
            camion = self.arryAplastadores[nroAplastador].partidaDeCamion()
            camion.tiempoLlegadaAlaPala = self.reloj + camion.getArriboAPala()
            # Generar arribo a la pala j del camion que salio del aplastador
            self.listaDeEventos[camion.palaAsignada] = self.arryPalas[camion.palaAsignada].addCamionllegando(camion)
            # Otro Camion empieza a Descargarse
            self.listaDeEventos[7] =  self.reloj + self.arryAplastadores[nroAplastador].calcularTimpoDescarga()
        else:
            self.arryAplastadores[nroAplastador].desocupado = True
            # Calcular y actualizar el material procesado

    # Para ver valores por consola, suele ser util
    def toString(self):
        if not(self.showReportesIntermedios):
            print "Valor de la simulacion: "
            print colors.LightCyan+"Relo\t"+colors.NC+str(self.reloj)+colors.NC
            print colors.LightCyan+"Relo\t"+colors.NC+str(self.proximoEvento)+colors.NC
            print colors.NC+"\n"
