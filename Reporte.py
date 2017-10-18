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

    def __init__(self):
        self.outputfile = "./lote"

    def pathToSeva(self):
        print colors.LightBlue + "Guardado en: %s" % (self.outputfile) + colors.NC

    def toCsv(self, observacion, materialProcesado):
        newRow = "%s,%s\n" % (observacion, materialProcesado)
        if observacion <= 1:
            # Escribo la cabecera
            with open(self.outputfile + '.csv', 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter = ';', quotechar = ';', quoting = csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Observaciones', 'Material procesado'])
        # agrego una linea
        with open(self.outputfile + '.csv', 'a') as csvfile:
            csvfile.write(newRow.encode('utf8'))

