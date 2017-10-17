import numpy as np
import time
from collections import deque
import random
from array import *
import pandas as pd
import sys

class Simulator(object):
    def __init__(self):
        self.Reloj = 0.0
        self.EstadoAplastador = ""
        self.EstadoPala1 = ""
        self.EstadoPala2 = ""
        self.EstadoPala3 = ""
        self.tm20Carga = 5
        self.tm50Carga = 10
        self.tm20Descarga = 2
        self.tm50Descarga = 5
        self.tViajeIda20 = 2.5
        self.tViajeIda50 = 3
        self.tViajeVuelta20 = 1.5
        self.tViajeVuelta50 = 2
        self.materialProcesado = 0
        self.ProximoEvento = ""
        self.ListaDeEventos = list()
        self.ColaPala1 = list()
        self.ColaPala2 = list()
        self.ColaPala3 = list()
        self.EstadoCamionA1 = list()
        self.EstadoCamionB1 = list()
        self.EstadoCamionC1 = list()
        self.EstadoCamionA2 = list()
        self.EstadoCamionB2 = list()
        self.EstadoCamionC2 = list()
        self.EstadoCamionA3 = list()
        self.EstadoCamionB3 = list()
        self.EstadoCamionC3 = list()
        self.Iniciado = False

    def inicializar(self):
        self.Reloj = 0
        self.EstadoAplastador = 'D'
        self.EstadoPala1 = 'D'
        self.EstadoPala2 = 'D'
        self.EstadoPala3 = 'D'
        self.ListaDeEventos = list()
        self.ColaPala1 = list()
        self.ColaPala2 = list()
        self.ColaPala3 = list()
        self.matProcesadoDiario = 0
        self.EstadoCamionA1 = list()
        self.EstadoCamionB1 = list()
        self.EstadoCamionC1 = list()
        self.EstadoCamionA2 = list()
        self.EstadoCamionB2 = list()
        self.EstadoCamionC2 = list()
        self.EstadoCamionA3 = list()
        self.EstadoCamionB3 = list()
        self.EstadoCamionC3 = list()
        self.Iniciado = False

        # 'Calculo el tiempo de primer arribo a cada pala
        #TODO segun el enunciado ver como lo ponemos
        generarPrimerosArribos(self)





    def run(self):
        path = 'C:\\Users\\nico\\Desktop\\Python\\Simulacion\\'
        #TODO Ver si es necesario armar un df

        for x in range(2):  #30Dias
            print('\nDia nro',(x+1))
            self.inicializar()
            cont = 0
            while True:

                self.tiempos()
                cont = cont +1
                #self.ProximoEvento= "Arribo pala 1"
                if self.ProximoEvento == "Arribo pala 1":
                    self.arriboPala1()

              #  elif self.ProximoEvento == "Arribo pala 2":
              #      self.arriboPala2()

              #  elif self.ProximoEvento == "Arribo pala 3":
              #      self.arriboPala3()

          elif self.ProximoEvento == "Partida pala 1":
              self.partidaPala1()
              #  elif self.ProximoEvento == "Partida pala 2":
              #      self.partidaPala2()
               # elif self.ProximoEvento == "Partida pala 3":
                #    self.partidaPala3()
               # elif self.ProximoEvento == "Arribo aplastador":
               #     self.arriboAplastador()
               # elif self.ProximoEvento == "Partida aplastador":
               #     self.partidaAplastador() #TODO Aca podemos mostrar el material que se procesa por dia y luego sumar eso al mensual
                if cont==10:
                    break


            print("La Lista de Eventos quedo:",self.ListaDeEventos)

           # self.reportes(x)


    def arriboPala1(self):
        aux = 9999
        CamionConMenorTiempo = ''
        camion = 0

        CamionConMenorTiempo = camionConMenosTiempoPala1(self, aux)
        tmCarga = calcularTiempoDeCargaPala1(self, CamionConMenorTiempo)
        tCarga = valorExponencial(tmCarga)
        if self.EstadoPala1 == 'D':
            if CamionConMenorTiempo == 'Camion C1':
                self.EstadoCamionC1[0] = 'Cargando'
                print("Salio el C1")
            else:
                if CamionConMenorTiempo == 'Camion A1':
                    self.EstadoCamionA1[0] = 'Cargando'
                    print("Salio el A1")
                else:
                    self.EstadoCamionB1[0] = 'Cargando'
                    print("Salio el camion B1")
            # GeneroPartida
            self.ListaDeEventos[3] = self.Reloj + tCarga

            # ListaEventos[x] = Reloj + tCarga
            self.EstadoPala1 = 'O'
            print(self.ListaDeEventos,"\n", self.EstadoCamionA1,self.EstadoCamionB1,self.EstadoCamionC1)

        # Pala Ocupada
    else:
        print("Pala ocupada")
            print("aux=",aux)
            camion = camionConMenosTiempoPala1(self,aux)
            print("El camion que entra es el",camion)

            if camion == 'Camion C1':
                tCarga=valorExponencial(self.tm50Carga)
                self.EstadoCamionC1[0] = 'En cola pala'
                self.EstadoCamionC1[1]+=tCarga
                print(self.EstadoCamionC1)
            else:
                tCarga = valorExponencial(self.tm20Carga)
                if camion == 'Camion A1':
                    print("Camion A1:",self.EstadoCamionA1)
                    self.EstadoCamionA1[0]='En cola pala'
                    self.EstadoCamionA1[1]+=tCarga
                elif camion == 'Camion B1':
                    print("Camion B1:", self.EstadoCamionB1)
                    self.EstadoCamionB1[0] = 'En cola pala'
                    self.EstadoCamionB1[1]+=tCarga
                print(tCarga)
            self.ColaPala1.append(self.Reloj)
            print("La cola quedo:",self.ColaPala1,"\n",self.EstadoCamionA1,self.EstadoCamionB1,self.EstadoCamionC1)
            #Cuando el camion entra a la cola, modifico el reloj o el tiempo del evento Arribo a la pala 1?

        SegundoCamion = camionConMenosTiempoPala1(self, aux)
        menor = segundoCamionPala1(self, SegundoCamion)
        # Un arribo genera un nuevo arribo
        print("Un arribo genera otro")
        self.ListaDeEventos[0] = menor
        print("El nuevo arribo es en el tiempo", menor)
#TODO lo mismo que esta en arriboPala2 ponerlo en los otros arribos
    def arriboPala2(self):
        CamionConMenorTiempo = ''
        aux = 9999
        # Rutina de arribo a la pala j
        if self.EstadoPala2 == 'D':
            CamionConMenorTiempo =camionConMenosTiempoPala2(self,aux)

            # Calculo tiempo de carga
            tmCarga = calcularTiempoDeCargaPala2(self, CamionConMenorTiempo)

            tCarga = valorExponencial(tmCarga)
            SegundoCamion=camionConMenosTiempoPala2(self, aux)
            print(SegundoCamion)
            menor = segundoCamionPala2(self, SegundoCamion)
            print(self.EstadoCamionA2, self.EstadoCamionB2, self.EstadoCamionC2)
            self.ListaDeEventos[1] = menor
            # GeneroPartida
            self.ListaDeEventos[4] = self.Reloj + tCarga
            # ListaEventos[x] = Reloj + tCarga
            self.EstadoPala2 = 'O'



        else:  # Pala Ocupada
            #En la partida comparo el tiempo de la cola con el tiempo de cada Camion, si es que esta en pala
            self.ColaPala2.append(self.Reloj)

    def arriboPala3(self):
        aux = 9999
        CamionConMenorTiempo = ''
        # Rutina de arribo a la pala j
        if self.EstadoPala3 == 'D':
            CamionConMenorTiempo =camionConMenosTiempoPala3(self,aux)

            # Calculo tiempo de carga
            tmCarga=calcularTiempoDeCargaPala3(self,CamionConMenorTiempo)


            tCarga = valorExponencial(tmCarga)
            SegundoCamion =camionConMenosTiempoPala3(self, aux)
            print(SegundoCamion)
            menor = segundoCamionPala3(self, SegundoCamion)
            self.ListaDeEventos[2] = menor
            # GeneroPartida
            self.ListaDeEventos[5] = self.Reloj + tCarga
            # ListaEventos[x] = Reloj + tCarga
            self.EstadoPala3 = 'O'



        else:  # Pala Ocupada
            # Creo que almacenar el tiempo de llegada en este caso es al pedo, si nos serviria con la cola del aplastador
            # tLLegada = Reloj
            self.ColaPala3.append(self.Reloj)

    def partidaPala1(self):
        if len(self.ColaPala1) > 0:
            print("hay cola")

    def partidaPala2(self):
        if len(self.ColaPala2) > 0:
            print("hay cola")

    def partidaPala3(self):
        if len(self.ColaPala3) > 0:
            print("hay cola")


    def tiempos(self):
        self.TiempoUltimoEvento = self.Reloj
        if self.ListaDeEventos.index(min(self.ListaDeEventos)) == 0:
            self.Reloj = self.ListaDeEventos[0]
            print("Reloj",self.Reloj)
            print("Antes de ingresar al arribo:",self.EstadoCamionA1, self.EstadoCamionB1,self.EstadoCamionC1)
            self.ProximoEvento = "Arribo pala 1"

        elif self.ListaDeEventos.index(min(self.ListaDeEventos)) == 1:
            self.Reloj = self.ListaDeEventos[1]
            self.ProximoEvento = "Arribo pala 2"

        elif self.ListaDeEventos.index(min(self.ListaDeEventos)) == 2:
            self.Reloj = self.ListaDeEventos[2]
            self.ProximoEvento = "Arribo pala 3"

        elif self.ListaDeEventos.index(min(self.ListaDeEventos)) == 3:
            self.Reloj = self.ListaDeEventos[3]
            self.ProximoEvento = "Partida pala 1"

        elif self.ListaDeEventos.index(min(self.ListaDeEventos)) == 4:
            self.Reloj = self.ListaDeEventos[4]
            self.ProximoEvento = "Partida pala 2"

        elif self.ListaDeEventos.index(min(self.ListaDeEventos)) == 5:
            self.Reloj = self.ListaDeEventos[5]
            self.ProximoEvento = "Partida pala 3"

        elif self.ListaDeEventos.index(min(self.ListaDeEventos)) == 6:
            self.Reloj = self.ListaDeEventos[6]
            self.ProximoEvento = "Arribo aplastador"

        elif self.ListaDeEventos.index(min(self.ListaDeEventos)) == 7:
            self.Reloj = self.ListaDeEventos[7]
            self.ProximoEvento = "Partida aplastador"
        print(self.ProximoEvento)


    def reportes(self, x):
        #Todo solo agregar la de material procesado en el mes
        print("El material procesado en el mes es de", self.materialProcesado, ' toneladas')


        #self.df.loc[(x+1), 'Nro Promedio Clientes En Cola']=var1



# ---------------------------------------------
# Funciones
# ---------------------------------------------
def valorExponencial(media):
    return np.random.exponential(media)

def verCamionesPala1(self,tCarga, num, camion):
    if camion == '50':
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionC1.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionA1.append(SegundoCamion)
        tCarga = valorExponencial(self.tm20Carga)
        self.EstadoCamionB1.append(SegundoCamion + tCarga)
    elif camion == '20' and num == 1:
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionA1.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionB1.append(SegundoCamion)
        tCarga = valorExponencial(self.tm50Carga)
        self.EstadoCamionC1.append(SegundoCamion + tCarga)
    elif camion == '20' and num == 2:
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionB1.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionA1.append(SegundoCamion)
        tCarga = valorExponencial(self.tm50Carga)
        self.EstadoCamionC1.append(SegundoCamion + tCarga)

def verCamionesPala2(self,tCarga, num, camion):
    if camion == '50':
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionC2.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionA2.append(SegundoCamion)
        tCarga = valorExponencial(self.tm20Carga)
        self.EstadoCamionB2.append(SegundoCamion + tCarga)
    elif camion == '20' and num == 1:
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionA2.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionB2.append(SegundoCamion)
        tCarga = valorExponencial(self.tm50Carga)
        self.EstadoCamionC2.append(SegundoCamion + tCarga)
    elif camion == '20' and num == 2:
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionB2.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionA2.append(SegundoCamion)
        tCarga = valorExponencial(self.tm50Carga)
        self.EstadoCamionC2.append(SegundoCamion + tCarga)

def verCamionesPala3(self,tCarga, num, camion):
    if camion == '50':
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionC3.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionA3.append(SegundoCamion)
        tCarga = valorExponencial(self.tm20Carga)
        self.EstadoCamionB3.append(SegundoCamion + tCarga)
    elif camion == '20' and num == 1:
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionA3.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionB3.append(SegundoCamion)
        tCarga = valorExponencial(self.tm50Carga)
        self.EstadoCamionC3.append(SegundoCamion + tCarga)
    elif camion == '20' and num == 2:
        PrimerCamion = self.Reloj + tCarga
        self.EstadoCamionB3.append(PrimerCamion)
        tCarga = valorExponencial(self.tm20Carga)
        SegundoCamion = PrimerCamion + tCarga
        self.EstadoCamionA3.append(SegundoCamion)
        tCarga = valorExponencial(self.tm50Carga)
        self.EstadoCamionC3.append(SegundoCamion + tCarga)

def camionConMenosTiempoPala1(self,aux):
    CamionConMenorTiempo = ''
    auxi = aux
    if self.EstadoCamionA1[0] == 'En pala':
        camion = self.EstadoCamionA1[1]
        if camion <= auxi:
            CamionConMenorTiempo = 'Camion A1'
            auxi = self.EstadoCamionA1[1]
    if self.EstadoCamionB1[0] == 'En pala':
        camion = self.EstadoCamionB1[1]
        if camion <= auxi:
            CamionConMenorTiempo = 'Camion B1'
            auxi = self.EstadoCamionB1[1]
    if self.EstadoCamionC1[0] == 'En pala':
        camion = self.EstadoCamionC1[1]
        if camion <= auxi:
            CamionConMenorTiempo = 'Camion C1'
            auxi = self.EstadoCamionC1[1]
    return CamionConMenorTiempo
def camionConMenosTiempoPala2(self,aux):
    if self.EstadoCamionA2[0] == 'En pala':
        camion = self.EstadoCamionA2[1]
        if camion <= aux:
            CamionConMenorTiempo = 'Camion A2'
            aux = self.EstadoCamionA2[1]
    if self.EstadoCamionB2[0] == 'En pala':
        camion = self.EstadoCamionB2[1]
        if camion <= aux:
            CamionConMenorTiempo = 'Camion B2'
            aux = self.EstadoCamionB2[1]
    if self.EstadoCamionC2[0] == 'En pala':
        camion = self.EstadoCamionC2[1]
        if camion <= aux:
            CamionConMenorTiempo = 'Camion C2'
            aux = self.EstadoCamionC2[1]
    return CamionConMenorTiempo
def camionConMenosTiempoPala3(self,aux):
    if self.EstadoCamionA3[0] == 'En pala':
        camion = self.EstadoCamionA3[1]
        if camion <= aux:
            CamionConMenorTiempo = 'Camion A3'
            aux = self.EstadoCamionA3[1]
    if self.EstadoCamionB3[0] == 'En pala':
        camion = self.EstadoCamionB3[1]
        if camion <= aux:
            CamionConMenorTiempo = 'Camion B3'
            aux = self.EstadoCamionB1[1]
    if self.EstadoCamionC3[0] == 'En pala':
        camion = self.EstadoCamionC3[1]
        if camion <= aux:
            CamionConMenorTiempo = 'Camion C3'
            aux = self.EstadoCamionC3[1]
    return CamionConMenorTiempo

def segundoCamionPala1(self, CamionConMenorTiempo):
    if CamionConMenorTiempo == 'Camion C1':
        menor = self.EstadoCamionC1[1]

    else:
        if CamionConMenorTiempo == 'Camion A1':
            menor = self.EstadoCamionA1[1]
        else:
            menor = self.EstadoCamionB1[1]
    return menor

def segundoCamionPala2(self, CamionConMenorTiempo):
    if CamionConMenorTiempo == 'Camion C2':
        menor = self.EstadoCamionC2[1]

    else:
        if CamionConMenorTiempo == 'Camion A2':
            menor = self.EstadoCamionA2[1]
        else:
            menor = self.EstadoCamionB2[1]
    return menor
def segundoCamionPala3(self, CamionConMenorTiempo):
    if CamionConMenorTiempo == 'Camion C3':
        menor = self.EstadoCamionC3[1]

    else:
        if CamionConMenorTiempo == 'Camion A3':
            menor = self.EstadoCamionA3[1]
        else:
            menor = self.EstadoCamionB3[1]
    return menor
def calcularTiempoDeCargaPala1(self,CamionConMenorTiempo):
    if CamionConMenorTiempo == 'Camion C1':
        tmCarga = self.tm50Carga
       print("Salio el C1")
   else:
       if CamionConMenorTiempo == 'Camion A1':
           print("Salio el A1")
       else:
           print("Salio el camion B1")
        tmCarga = self.tm20Carga
    return tmCarga
def calcularTiempoDeCargaPala2(self,CamionConMenorTiempo):
    if CamionConMenorTiempo == 'Camion C2':
        tmCarga = self.tm50Carga
        self.EstadoCamionC2[0] = 'Cargando'
        print("Salio el C2")


    else:
        if CamionConMenorTiempo == 'Camion A2':
            self.EstadoCamionA2[0] = 'Cargando'
            print("Salio el A2")
        else:
            self.EstadoCamionB2[0] = 'Cargando'
            print("Salio el camion B2")
        tmCarga = self.tm20Carga
    return tmCarga
def calcularTiempoDeCargaPala3(self, CamionConMenorTiempo):
    if CamionConMenorTiempo == 'Camion C3':
        tmCarga = self.tm50Carga
        self.EstadoCamionC3[0] = 'Cargando'
        print("Salio el C3")


    else:
        if CamionConMenorTiempo == 'Camion A3':
            self.EstadoCamionA3[0] = 'Cargando'
            print("Salio el A3")
        else:
            self.EstadoCamionB3[0] = 'Cargando'
            print("Salio el camion B3")
        tmCarga = self.tm20Carga
    return tmCarga
def generarPrimerosArribos(self):
    self.EstadoCamionA1 = ['En pala']
    self.EstadoCamionB1 = ['En pala']
    self.EstadoCamionC1 = ['En pala']
    self.EstadoCamionA2 = ['En pala']
    self.EstadoCamionB2 = ['En pala']
    self.EstadoCamionC2 = ['En pala']
    self.EstadoCamionA3 = ['En pala']
    self.EstadoCamionB3 = ['En pala']
    self.EstadoCamionC3 = ['En pala']

    for x in range(3):
        camion = ''
        num = random.randint(1, 3)
        # Que camion sale primero
        if num == 3:
            tCarga = valorExponencial(self.tm50Carga)
            camion = '50'
        else:
            tCarga = valorExponencial(self.tm20Carga)
            camion = '20'

        # Que camion sale primero segun que pala
        if x == 0:
            verCamionesPala1(self,tCarga, num, camion)
        elif x == 1:
            verCamionesPala2(self,tCarga, num, camion)
        elif x == 2:
            verCamionesPala3(self,tCarga, num, camion)
        self.ListaDeEventos.append(self.Reloj + tCarga)

    for x in range(3, 8):
        # listaEventos[x]=9999
        self.ListaDeEventos.append(9999)
# ---------------------------------------------
# Ejecución del modelo
# ---------------------------------------------

sys.stdout.flush()
sim1 = Simulator()
sim1.run()

