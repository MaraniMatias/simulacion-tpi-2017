# Para Debug
# import pdb
# pdb.set_trace()

# Asuma que en tiempo cero todos los camiones estan en sus respectivas palas con los camiones de 50 tn en primer lugar.
from array import *
from Pala import Pala
from Aplastador import Aplastador
from Reporte import *

class Simulator(object):

    def __init__(self):
        self.showReportesIntermedios = True
        self.reporte = Reporte()
        self.proximoEvento = ""  # No es necesaria para la simulacion, solo muestra

        self.reloj = 0.0
        self.materialProcesado = 0
        self.listaDeEventos = array('f')
        self.arrayPalas = [Pala(i) for i in range(3)]
        self.arrayAplastadores = [Aplastador()]  # alternativa usa otro aplastador

    # Sub Principal()
    def run(self):
        self.inicializar()
        # Loop, la simulacion, reloj es el finde la simulacion
        while (self.reloj <= 2000):
            # la rutina tiempo llama directamente a los eventos
            index = self.tiempos()
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
        self.reporte.toCsv(1, self.materialProcesado)

    def inicializar(self):
        # 0 - ARRIBOS_PALA_1
        # 1 - ARRIBOS_PALA_2
        # 2 - ARRIBOS_PALA_3
        # 3 - PARTIDAS_PALA_1
        # 4 - PARTIDAS_PALA_2
        # 5 - PARTIDAS_PALA_3
        # 6 - ARRIBOS_APLASTADOR
        # 7 - PARTIDAS_APLASTADOR

        # forzar que no ocurran eventos
        for x in range(8):
            self.listaDeEventos.append(9999999)

        # como se asume que en el tiempo cero todos los camiones estan en su pala.
        # Por eso tenemos que calcular las partidas
        # Calculo el tiempo de la primera partida
        # Tengo que generarlo con el primer camion de todas las palas
        self.partidasPala(1)
        self.partidasPala(2)
        self.partidasPala(3)
        # self.toString() # al solo efecto de ver como evolucionan los valores de las variables

    def tiempos(self):
        self.tiempoUltimoEvento = self.reloj
        # Para buscar el proximo evento,
        self.reloj = min(self.listaDeEventos)
        return self.listaDeEventos.index(self.reloj)

    def arribosPala(self, nroPala):
        nroPala = nroPala - 1  # Para pasarlo a index
        if self.arrayPalas[nroPala].desocupado:
            self.arrayPalas[nroPala].desocupado = False
            self.listaDeEventos[nroPala] = 9999999
            self.arrayPalas[nroPala].addCola()  # Pasa el camion que llega, ala cola
            self.listaDeEventos[nroPala + 3] = self.reloj + self.arrayPalas[nroPala].pasarCamionACarga().getTiempoCarga()
        else:
            #  Agregar camion i de la pala j en la cola j
            self.arrayPalas[nroPala].addCola()  # Pasa el camion que llega, ala cola
            # Como llego un camion tengo que programar la proximo arribo
            if  self.arrayPalas[nroPala].hayCamionesLlegando():
                # acomodar arribos al pala j, al estar ordena es el primero
                self.listaDeEventos[nroPala] = self.arrayPalas[nroPala].camionesLlegando[0].tiempoLlegadaAlaPala
            else:
                # al no llegar camiones fuerso a que este evento no suseda
                self.listaDeEventos[nroPala] = 9999999

    def partidasPala(self, nroPala):
        nroPala = nroPala - 1  # Para pasarlo a index

        # Parte el camion y  calculo tiempo de arribo al aplastador
        camion = self.arrayPalas[nroPala].camionCargando
        camion.tiempoLlegadaAlAplastador = self.reloj + camion.getArriboAlAplastador()
        # Guardar una cola de camiones llegando y el primero en llegar seria el proximo evento
        self.listaDeEventos[6] = self.arrayAplastadores[0].addCamionllegando(camion)

        if self.arrayPalas[nroPala].hayCamionesEnCola():
            # Otro Camion empieza a llenarse, Genera la proxima partida
            self.listaDeEventos[nroPala + 3] = self.reloj + self.arrayPalas[nroPala].pasarCamionACarga().getTiempoCarga()
        else:
            self.arrayPalas[nroPala].desocupado = True
            self.arrayPalas[nroPala].camionCargando = None
            # Forzar, limpiar partias desde esta pala
            self.listaDeEventos[nroPala + 3] =  9999999

    def arribosAplastador(self, nroAplastador):
        nroAplastador = nroAplastador - 1  # Para pasarlo a index
        if self.arrayAplastadores[nroAplastador].desocupado:
            # sacar el camion que llego de  camionesLlegando,
            self.arrayAplastadores[nroAplastador].addCola() # Pasa el camion que llega, ala cola
            camion = self.arrayAplastadores[nroAplastador].pasarCamionADescarga()
            # Generar de partida del camion i del aplastador
            # Tiempo de descarga de ese camion
            self.listaDeEventos[7] = self.reloj + camion.getTiempoDescarga()
            # Poner al aplastador en OCUPADO
            self.arrayAplastadores[nroAplastador].desocupado = False

            if self.arrayAplastadores[0].hayCamionesLlegando():
                # acomodar arribos al Aplastador, al estar ordena es el primero
                self.listaDeEventos[6] = self.arrayAplastadores[0].camionesLlegando[0].tiempoLlegadaAlAplastador
            else:
                self.listaDeEventos[6] = 9999999
        else:
            # Almacenar tiempo llegada del camion i de la pala j, lo tendo en el camion
            # Poner camion i de la pala j en cola del aplastador
            self.arrayAplastadores[nroAplastador].addCola()  # El aplastador sabe que camion llego
            # Como llego un camion tengo que programar la proximo arribo
            if  self.arrayAplastadores[0].hayCamionesLlegando():
                # acomodar arribos al Aplastador, al estar ordena es el primero
                self.listaDeEventos[6] = self.arrayAplastadores[0].camionesLlegando[0].tiempoLlegadaAlAplastador
            else:
                # al no llegar camiones fuerso a que este evento no suseda
                self.listaDeEventos[6] = 9999999

    def partidasAplastador(self, nroAplastador):
        nroAplastador = nroAplastador - 1  # Para pasarlo a index

        # Quitar camion de la cola y el que se esta descargando
        camion = self.arrayAplastadores[nroAplastador].camionDescargando
        camion.tiempoLlegadaAlaPala = self.reloj + camion.getArriboAPala()
        # Calcular y actualizar el material procesado
        self.materialProcesado += camion.toneladas
        # Generar arribo a la pala j del camion que salio del aplastador
        self.listaDeEventos[camion.palaAsignada] = self.arrayPalas[camion.palaAsignada].addCamionllegando(camion)

        if self.arrayAplastadores[nroAplastador].hayCamionesEnCola():
            # Otro Camion empieza a Descargarse, Genera la proxima partida
            self.listaDeEventos[7] = self.reloj + self.arrayAplastadores[nroAplastador].pasarCamionADescarga().getTiempoDescarga()
        else:
            self.arrayAplastadores[nroAplastador].desocupado = True
            self.listaDeEventos[7] = 9999999
            self.arrayAplastadores[nroAplastador].camionDescargando = None

    # Para ver valores por consola, suele ser util
    def toString(self):
        if self.showReportesIntermedios:
            print "Valor de la simulacion: "
            print colors.LightCyan + "Relo\t" + colors.NC + str(self.reloj) + colors.NC
            print colors.LightCyan + "Evento\t" + colors.NC + str(self.proximoEvento) + colors.NC
            print colors.LightCyan + "Material Procesado\t" + colors.NC + str(self.materialProcesado) + colors.NC
            print colors.LightBlue + "Lista de Eventos:" + colors.NC
            for i in range(len(self.listaDeEventos)):
                print colors.LightBlue + "Evento: " + colors.NC + str(i) + colors.Yellow + " Tiempo " + colors.NC + str(self.listaDeEventos[i])
            for i in range(len(self.arrayPalas)):
                print colors.LightPurple + "Pala: "+ str(i) + colors.NC
                print colors.LightPurple + "\tCamion en carga: " + colors.NC + str(self.arrayPalas[i].camionCargando)
                print colors.LightPurple + "\tLong de cola: " + colors.NC + str(len(self.arrayPalas[i].colaDeCamiones))
                print colors.LightPurple + "\tCamiones llegando: " + colors.NC + str(len(self.arrayPalas[i].camionesLlegando))
            for i in range(len(self.arrayAplastadores)):
                print colors.LightGreen + "Aplastador: "+ str(i) + colors.NC
                print colors.LightGreen + "\tCamion en descarga: " + colors.NC + str(self.arrayAplastadores[i].camionDescargando)
                print colors.LightGreen + "\tLong de cola: " + colors.NC + str(len(self.arrayAplastadores[i].colaDeCamiones))
                print colors.LightGreen + "\tCamiones llegando: " + colors.NC + str(len(self.arrayAplastadores[i].camionesLlegando))
            print colors.NC + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
