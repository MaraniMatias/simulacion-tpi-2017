import sys
# Print iterations progress
def update_progress(progress, status = '', corrida = '', totalCorridas=''):
    barLength = 25
    if isinstance(progress, int):
        progress = float(progress)
    if progress < 0:
        progress = 0
        status = "Esperando...\r\n"
    if progress >= 1:
        progress = 1
        status = "\n"
    block = int(round(barLength * progress))
    sys.stdout.write(str(colors.LightGreen + "\rCorridas: " + colors.NC + "{0}/{1} [{2}] {3}%" + colors.NC + " {4} ").format(corrida, totalCorridas, str(colors.LightGray + ("#" * block)) + str(colors.DarkGray + "." * (barLength - block) + colors.NC), round(progress * 100, 1), status))
    sys.stdout.flush()

from Reporte import colors
from Simulator import Simulator

class Programa(object):

    def __init__(self):
        self.observacion = 1023 #  filas maximas en calc 1023
        self.corridas = 30
        self.progresbar = True
        self.buscarLote = False

if __name__ == "__main__":
    print(colors.Yellow + 'Simulacion Camiones y Aplastadora' + colors.NC)
    programa = Programa()

    ## setup toolbar
    if programa.progresbar: update_progress(0)

    materialProcesado = 0
    for corrida in range(1, programa.corridas + 1):
        sim = Simulator(720)
        sim.inicializar()

        for obs in range(1, programa.observacion + 1):
            if not(programa.progresbar): print(colors.Yellow + 'Corrida: ' + str(corrida) + colors.LightGreen + ' Observacion: ' + colors.NC + str(obs))

            # Corre simulacion
            materialProcesado = materialProcesado + sim.run(obs)

            if not(programa.progresbar): print(colors.LightCyan + "Material procesado: " + colors.NC + str(materialProcesado))
            ## tick toolbar
            if programa.progresbar: update_progress((float(corrida + obs) / (programa.corridas + programa.observacion)), colors.LightCyan + " Media del Material: " + colors.NC + str(materialProcesado / ((programa.observacion + 1) * corrida)), corrida, programa.corridas)

        # Crea el reporte
        sim.reporte.toCsv(corrida)
