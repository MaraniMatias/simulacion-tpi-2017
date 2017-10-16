import csv

# Utilidades para terminal
class colors(Object):
    NC='\033[0m'
    Black='\033[0;30m'
    DarkGray='\033[1;30m'
    Red='\033[0;31m'
    LightRed='\033[1;31m'
    Green='\033[0;32m'
    LightGreen='\033[1;32m'
    BrownOrange='\033[0;33m'
    Yellow='\033[1;33m'
    Blue='\033[0;34m'
    LightBlue='\033[1;34m'
    Purple='\033[0;35m'
    LightPurple='\033[1;35m'
    Cyan='\033[0;36m'
    LightCyan='\033[1;36m'
    LightGray='\033[0;37m'

class Reporte(Object):

    def __init__(self):
        self.outputfile ="./reportes/lote"

        self.NroPromedioClientesEnCola = 0.0
        self.UtilizacionPromedioServidores = 0.0
        self.DemoraPromedioPorCliente = 0.0
        self.NroMaximoDeClientesEnCola = 0.0

        # Valores de entrada:
        self.TMDeServicio = 0.0
        self.TMEntreArribos = 0.0

    def pathToSeva(self):
        print colors.LightBlue+"Guardado en: %s" % (self.outputfile)+colors.NC


    def toCsv(self, observacion):
            newRow = "%s,%s,%s,%s,%s\n" % (Oubservacion,NroPromedioClientesEnCola,self.UtilizacionPromedioServidores,self.DemoraPromedioPorCliente,self.NroMaximoDeClientesEnCola)
            if observacion <= 1:
                # Escribo la cabecera
                with open(Reporte.outputfile+'.csv', 'wb') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(['Observaciones', 'Nro Promedio Clientes En Cola', 'Utilizacion Promedio Servidores', 'Demora Promedio Por Cliente', 'Cantidad Maxima de Clientes en Cola'])
            # agrego una linea
            with open(Reporte.outputfile+'.csv', 'a') as csvfile:
                csvfile.write(newRow.encode('utf8'))

    def show(self):
        if not program.progresbar:
            print colors.LightGreen+'~~~~~~~~~~~~~~~~~~~~~~Reporte~~~~~~~~~~ '+colors.BrownOrange +"Corrida: "+str(Programa.Observacion) +'/'+str(Programa.Corridas)+ colors.NC
            print colors.Yellow+"Variables de entrada:"+colors.NC
            print colors.LightCyan+"Tiempo medio de servicio: "+colors.NC+str(self.TMDeServicio)
            print colors.LightCyan+"Tiempo medio entre arribos: "+colors.NC+str(self.TMEntreArribos)
            print colors.LightCyan+"Distribucion para la variable tiempo entre arribos: "+colors.NC+Simulator.DistribucionVariableTiempoEntreArribos
            print colors.LightCyan+"Distribucion para la variable tiempo servicio: "+colors.NC+Simulator.DistribucionVariableTiempoServicio

            print colors.Yellow+"Variables de respuesta:"+colors.NC
            print colors.Green+'Nro Promedio Clientes En Cola: '+colors.NC+str(self.NroPromedioClientesEnCola)
            print colors.Green+'Utilizacion Promedio Servidores: ' +colors.NC+ str(self.UtilizacionPromedioServidores)
            print colors.Green+'Demora Promedio Por Cliente: '+colors.NC+ str(self.DemoraPromedioPorCliente)
            print colors.Green+'Cantidad Maxima de Clientes en Cola: '+colors.NC+ str(self.NroMaximoDeClientesEnCola)
            print colors.LightGreen+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'+colors.NC
