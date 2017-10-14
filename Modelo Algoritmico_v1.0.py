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
        self.ListaDeEventos = array('f')
        self.Cola = array('f')
        self.EstadoCamionA1 = ''
        self.EstadoCamionB1 = ''
        self.EstadoCamionA2 = ''
        self.EstadoCamionB2 = ''
        self.EstadoCamionA3 = ''
        self.EstadoCamionB3 = ''



    def inicializar(self):
        self.Reloj = 0
        self.EstadoAplastador = 'D'
        self.EstadoPala1 = 'D'
        self.EstadoPala2 = 'D'
        self.EstadoPala3 = 'D'
        self.ListaDeEventos = array('f')
        self.Cola = array('f')
        self.matProcesadoDiario = 0
        self.EstadoCamionA1 = 'En pala'
        self.EstadoCamionB1 = 'En pala'
        self.EstadoCamionA2 = 'En pala'
        self.EstadoCamionB2 = 'En pala'
        self.EstadoCamionA3 = 'En pala'
        self.EstadoCamionB3 = 'En pala'
        #Incluyo estado camion porque no se me ocurre otra forma para discernir entre los tiempos de cada camion
        #Mi propuesta son  estados: "En pala" (aca podria ser tanto para que recien llega desde el aplastador y tambien por si tiene que estar esperando su turno)
        #                           "Cargando"
        #                           "En viaje ida"
        #                           "En aplastador" (aca podria ser tanto para que recien llega desde la pala y tambien por si tiene que estar esperando su turno)
        #                           "Descargando"
        #                           "En viaje vuelta"

        # 'Calculo el tiempo de primer arribo
        #TODO segun el enunciado ver como lo ponemos
        tm = 'primer arribo'
        self.ListaDeEventos.append(tm)
        self.ListaDeEventos.append(99999.0)





    def run(self):
        path = 'C:\\Users\\nico\\Desktop\\Python\\Simulacion\\'
        #TODO Ver si es necesario armar un df
        self.df = generarDataFrame()

        for x in range(29):  #30Dias
            print('\nDia nro',(x+1))
            self.inicializar()
            while True:
                self.tiempos()
                if self.ProximoEvento == "Arribo a la pala 1":
                    self.arriboALaPala1()
                elif self.ProximoEvento == "Arribo a la pala 2":
                    self.arriboALaPala2()
                elif self.ProximoEvento == "Arribo a la pala 3":
                    self.arriboALaPala3()
                elif self.ProximoEvento == "Partida desde la pala 1":
                    self.partidaDesdeLaPala1()
                elif self.ProximoEvento == "Partida desde la pala 2":
                    self.partidaDesdeLaPala2()
                elif self.ProximoEvento == "Partida desde la pala 3":
                    self.partidaDesdeLaPala3()
                elif self.ProximoEvento == "Arribo al aplastador":
                    self.arriboAlAplastador()
                elif self.ProximoEvento == "Partida desde el aplastador":
                    self.partidaDesdeElAplastador() #TODO Aca podemos mostrar el material que se procesa por dia y luego sumar eso al mensual


                #if self.Reloj >= 8 and self.NroDeClientesEnCola == 0 and self.EstadoServidor == "D":
                  #  break
            self.reportes(x)

        #self.df.loc[(0), 'Tiempo de servicio'] = self.TMDeServicio
       # self.df.loc[(0), 'Tiempo entre Arribos'] = self.TMEntreArribos
       # self.df.index.name = 'Observaciones'
       # self.df.to_csv(path + "Salida Punto 7.csv", index=True, encoding='Latin-1')

    def arriboPala1(self):
        # Rutina de arribo a la pala j

        # Usamos estadoPala j, generamos el tiempo de carga sabiendo el valor de la media y generamos el evento partida camion (ListaEventos[x]= reloj + tCarga)
        # Al haber 2 camiones no creo q sea necesario comparar sus tiempos de llegada. Pues cuando uno llega puede pasar que este ocupada la pala y entra a la cola, pero como
        # solamente hay 2 camiones es al pedo, no se que opinan
        if self.EstadoPala1 == 'D':
            if self.EstadoCamionA1 == 'En pala':
                tmCarga = self.tm20Carga
                self.EstadoCamionA1 = 'En viajeIda'

            else:
                tmCarga = self.tm50Carga
                self.EstadoCamionB1 = 'En viajeIda'

            tCarga = genTiempoCarga(tmCarga)
            ListaEventos = self.Reloj + tCarga
            # ListaEventos[x] = Reloj + tCarga
            self.EstadoPala1 = 'O'


        else:  # Pala Ocupada
            # Creo que almacenar el tiempo de llegada en este caso es al pedo, si nos serviria con la cola del aplastador
            # tLLegada = Reloj
            self.Cola.append(self.Reloj)

    def arriboPala2(self):
        if self.EstadoPala2 == 'D':
            if self.EstadoCamionA2 == 'En pala':
                tmCarga = self.tm20Carga
                self.EstadoCamionA2 = 'En viajeIda'

            else:
                tmCarga = self.tm50Carga
                self.EstadoCamionB2 = 'En viajeIda'

            tCarga = genTiempoCarga(tmCarga)
            ListaEventos = self.Reloj + tCarga
            # ListaEventos[x] = Reloj + tCarga
            self.EstadoPala2 = 'O'


        else:  # Pala Ocupada
            # Creo que almacenar el tiempo de llegada en este caso es al pedo, si nos serviria con la cola del aplastador
            # tLLegada = Reloj
            self.Cola.append(self.Reloj)

    def arriboPala3(self):
        if self.EstadoPala3 == 'D':
            if self.EstadoCamionA3 == 'En pala':
                tmCarga = self.tm20Carga
                self.EstadoCamionA3 = 'En viajeIda'

            else:
                tmCarga = self.tm50Carga
                self.EstadoCamionB3 = 'En viajeIda'

            tCarga = genTiempoCarga(tmCarga)
            ListaEventos = self.Reloj + tCarga
            # ListaEventos[x] = Reloj + tCarga
            self.EstadoPala3 = 'O'


        else:  # Pala Ocupada
            # Creo que almacenar el tiempo de llegada en este caso es al pedo, si nos serviria con la cola del aplastador
            # tLLegada = Reloj
            self.Cola.append(self.Reloj)

    def partidas(self):
        # ' Pregunto si hay clientes en cola
        if self.NroDeClientesEnCola > 0:
            #-------------Punto 4-----------------
            minIndex, minNro, self.Zo = menorTiempoEstimado(self.Cola, self.TMDeServicio, self.a, self.b, self.Zo)
            self.ListaDeEventos[1] = minNro
            #*************************************
            self.DemoraAcumulada += self.Reloj - self.Cola[minIndex]
            self.CompletaronDemora += 1
            self.TSAcumulado += (self.ListaDeEventos[1] - self.Reloj)
            self.AreaQDeT += (self.NroDeClientesEnCola * (self.Reloj - self.TiempoUltimoEvento))
            self.NroDeClientesEnCola -= 1
            #----------Punto 4------------
            self.Cola.pop(minIndex)
            #*****************************

        else:
            self.EstadoServidor = "D"
            self.ListaDeEventos[1] = 99999.0

    def tiempos(self):
        #Todo buscar el algoritmo que nos dio el profe y plasmarlo aca
        self.TiempoUltimoEvento = self.Reloj
        if self.ListaDeEventos[0] <= self.ListaDeEventos[1]:
            self.Reloj = self.ListaDeEventos[0]
            self.ProximoEvento = "ARRIBOS"

        else:
            self.Reloj = self.ListaDeEventos[1]
            self.ProximoEvento = "PARTIDAS"


    def reportes(self, x):
        #Todo solo agregar la de material procesado en el mes
        print("El material procesado en el mes es de", self.materialProcesado, ' toneladas')


        #self.df.loc[(x+1), 'Nro Promedio Clientes En Cola']=var1



# ---------------------------------------------
# Funciones
# ---------------------------------------------
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def generarDataFrame():
    index = list(range(0 , 101))
    columns = ['Nro Promedio Clientes En Cola', 'Utilizacion Promedio Servidores',
            'Demora Promedio Por Cliente', 'Cantidad Maxima de Clientes en Cola']
    df = pd.DataFrame(index=index, columns=columns)
    df.index.name = 'Observaciones'
    df = df.fillna(0)
    return df

def genTiempoCarga(media):
    return np.random.exponential(media)

#Punto 4
def menorTiempoEstimado(cola, TMDeServicio, a, b, Zo):
    aux =list(cola)
    for x in range(0, len(cola)):
        tServicio, Zo = generarTiempoDeServicio(TMDeServicio, a, b, Zo)
        aux[x] += tServicio
    #print("Index del menor tiempo: ", aux.index(min(aux)), "Tiempo: ",min(aux)
    minIndex = aux.index(min(aux))
    minNro = min(aux)

    return minIndex,minNro,Zo

#Punto 5
def generadorCongruencialLineal(Zo):
    a=314159269
    c=0
    m=pow(2,31)
    Ui=0
    Zi=(a*Zo + c) % m
    Ui = Zi/m
    Zo = Zi
    return Ui,Zo

#Punto 6 Aca no necesito devolver lo que vale Zo
def generarTiempoEntreArribos(media,desvio, K, Zo):
    suma=0
    for x in range(0,12):
        r,Zo =generadorCongruencialLineal(Zo)
        suma += r
    x = desvio * ((12/K) **(1/2)) * (suma - K/2) + media
    return x, Zo

#Punto 7 Aca si tengo que devolver lo que vale Zo
def generarTiempoDeServicio(mediaTServ, a, b, Zo):
    r, Zo= generadorCongruencialLineal(Zo)
    x= a+(b-a)*r
    return x, Zo


# ---------------------------------------------
# Ejecución del modelo
# ---------------------------------------------

sys.stdout.flush()
sim1 = Simulator()
sim1.run()




