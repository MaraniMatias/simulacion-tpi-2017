import csv

# Utilidades para terminal
class colors(object):
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

class Reporte(object):
    #TODO Aca podemos hacer para mostrar las graficas

    def __init__(self, limitReloj):
        self.outputfile = "reporte-cada-"+str(limitReloj)+"hs"
        self.outputfileCola = "camiones-en-cola-aplastador-"+str(limitReloj)+"hs"
        self.dataSetCola = list()
        self.dataSet = list() # muestras por mes

    def guardarObservacion(self, materialProcesado, cola):
        self.dataSetCola.append(cola)
        self.dataSet.append(materialProcesado)

    def pathToSeva(self):
        print(colors.LightBlue + "Guardado en: %s" % (self.outputfile) + colors.NC)

    def toCsv(self, corrida = 1):
        self.colaToCsv(corrida)
        # fila
        newRow = str(corrida)
        for obs in self.dataSet:
            newRow += ',' + str(obs)
        newRow += '\n'

        if corrida <= 1:
            # Escribo la cabecera
            heard = ['Corrida']
            for mes in range(len(self.dataSet)):
                heard.append('obs ' + str(mes + 1))
            with open(self.outputfile + '.csv', 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter = ';', quotechar = ';', quoting = csv.QUOTE_MINIMAL)
                spamwriter.writerow(heard)
        # agrego una linea
        with open(self.outputfile + '.csv', 'a') as csvfile:
            csvfile.write(newRow.encode('utf8'))

        # Limpiar
        self.dataSet = [] # muestras por mes

    def colaToCsv(self, corrida = 1):
        # fila
        newRow = str(corrida)
        for obs in self.dataSetCola:
            newRow += ',' + str(obs)
        newRow += '\n'

        if corrida <= 1:
            # Escribo la cabecera
            heard = ['Corrida']
            for mes in range(len(self.dataSet)):
                heard.append('obs ' + str(mes + 1))
            with open(self.outputfileCola + '.csv', 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter = ';', quotechar = ';', quoting = csv.QUOTE_MINIMAL)
                spamwriter.writerow(heard)
        # agrego una linea
        with open(self.outputfileCola + '.csv', 'a') as csvfile:
            csvfile.write(newRow.encode('utf8'))

        # limpiar
        self.dataSetCola = [] # muestras por mes
