# Asuma que en tiempo cero todos los camiones están en sus respectivas palas con los camiones de 50 tn en primer lugar.
from array import *
import math
import Pala

class Simulator(Object):

    def __init__(self):
        self.Reloj = 0.0
        self.EstadoServidor = ""
        self.ProximoEvento = ""
        self.ListaDeEventos = array('f')
        self.TSAcumulado = 0.0
        self.TiempoUltimoEvento = 0.0
        self.Paso = 0
        self.TMEntreArribos = 7.0
        self.TMDeServicio = 9.0
        self.Iniciado = False

        self.arryPalas = [Pala() for i in range(3)]

    def inicializar(self):
        self.Reloj = 0
        self.EstadoServidor = "D"
        self.ProximoEvento = ""
        self.TSAcumulado = 0
        self.DemoraAcumulada = 0
        self.NroDeClientesEnCola = 0
        self.AreaQDeT = 0
        self.TiempoUltimoEvento = 0
        self.CompletaronDemora = 0

        # Calculo el tiempo de primer arribo
        self.ListaDeEventos.append(self.gen.valor("arribo",self.TMEntreArribos))

        # Fuerza a que el primer evento no sea una partida
        self.ListaDeEventos.append(999999.0)
        self.Paso = 0
        self.Iniciado = False
        #self.toString() # al solo efecto de ver como evolucionan los valores de las variables

    # Sub Principal()
    def run(self):
        # Llamo a la rutina de inicializacion
        self.inicializar()
        # Loop, la simulacion, reloj es el finde la simulacion, en este caso 8 tick
        while not(self.Reloj >= 8 and self.NroDeClientesEnCola == 0 and self.EstadoServidor == "D"):
            self.tiempos() # llamada a la rutina de tiempos
            # llamada a la rutina correspondiente en funcion del tipo de evento, Select ProximoEvento
            if self.ProximoEvento == "ARRIBOS":
                self.arribos()
            else:
                self.partidas()
            # Para ver valores intermedios
            self.toString()
        # Al salir del while es el fin de la simulacion, emitir reporte
        self.reportes()

    def arribos(self):
        # Todo arribo desencadena un nuevo arribo
        self.ListaDeEventos[0] = self.Reloj + self.gen.valor("arribo",self.TMEntreArribos)
        # Pregunto si el servidor esta desocupado
        if self.EstadoServidor == "D":
            # Cambio el estado del servidor a "Ocupado"
            self.EstadoServidor = "O"
            # Programo el proximo evento partida
            self.ListaDeEventos[1] = self.Reloj + self.gen.valor("servicio",self.TMDeServicio)
            # Acumulo el tiempo de servicio
            self.TSAcumulado += (self.ListaDeEventos[1] - self.Reloj)
            # Actualizo la cantidad de clientes que completaron la demora
            self.CompletaronDemora += 1
        else:
            # Calculo el area bajo Q(t) desde el momento actual del reloj hacia atras (TiempoUltimoEvento)
            self.AreaQDeT += (self.NroDeClientesEnCola * (self.Reloj - self.TiempoUltimoEvento))
            # Incremento la cantidad de clientes en cola en uno (1)
            self.NroDeClientesEnCola += 1
            # Guardo el valor del reloj en la posicionn "NroDeClientesEnCola" para saber cuando llegar el cliente a la cola y mas adelante calcular la demora.
            self.addClienteEnCola()

    def partidas(self):

    def tiempos(self):

    def addClienteEnCola(self):


    # Para ver valores por consola, suele ser util
    def toString(self):
        if not(Programa.Silencio):
            print "Valor de la simulacion: "
            print colors.LightCyan+"Relo\t"+colors.NC+str(self.Reloj)+colors.NC
            print colors.LightCyan+"EstadoServidor\t"+colors.Yellow+str(self.EstadoServidor)+colors.NC
            print colors.LightCyan+"ProximoEvento\t"+colors.Yellow+str(self.ProximoEvento)+colors.NC
            if len(self.ListaDeEventos) <= 15:
                print colors.LightCyan+"ListaDeEventos\t"+colors.Purple+str(np.array(self.ListaDeEventos))+colors.NC
            else:
                print colors.LightCyan+"ListaDeEventos de logitud\t"+colors.Red+str(len(self.ListaDeEventos))+colors.NC
            if len(self.Cola) <= 15:
                print colors.LightCyan+"Cola\t"+colors.Purple+str(np.array(self.Cola))+colors.NC
            else:
                print colors.LightCyan+"Cola de longitud\t"+colors.Red+str(len(self.Cola))+colors.NC

            print colors.LightCyan+"TSAcumulado\t"+colors.NC+str(self.TSAcumulado)+colors.NC
            print colors.LightCyan+"DemoraAcumulada\t"+colors.NC+str(self.DemoraAcumulada)+colors.NC
            print colors.LightCyan+"NroDeClientesEnCola\t"+colors.NC+str(self.NroDeClientesEnCola)+colors.NC
            print colors.LightCyan+"AreaQDeT\t"+colors.NC+str(self.AreaQDeT)+colors.NC
            print colors.LightCyan+"TiempoUltimoEvento\t"+colors.NC+str(self.TiempoUltimoEvento)+colors.NC
            print colors.LightCyan+"CompletaronDemora\t"+colors.NC+str(self.CompletaronDemora)+colors.NC
            print colors.LightCyan+"Paso\t"+colors.NC+str(self.Paso)+colors.NC
            print colors.LightCyan+"TMEntreArribos\t"+colors.NC+str(self.TMEntreArribos)+colors.NC
            print colors.LightCyan+"TMDeServicio\t"+colors.NC+str(self.TMDeServicio)+colors.NC
            print colors.LightCyan+"Iniciado\t"+colors.BrownOrange+str(self.Iniciado)+colors.NC

            print colors.LightCyan+"Distribucion para la variable tiempo entre arribos: "+colors.NC+Simulator.DistribucionVariableTiempoEntreArribos
            print colors.LightCyan+"Distribucion para la variable tiempo servicio: "+colors.NC+Simulator.DistribucionVariableTiempoServicio
            print colors.NC+"\n"
