# simulacion-tp-integrador-2017
trabajo practico integrador

## Modelo algorítmico:

### Arribo a la pala j
Si la pala j esta DESOCUPADA
  Calcular tiempo de carga
  Generar partida del camión i de la pala j
  Poner la pala j em OCUPADO
Si no
  Agregar camión i de la pala j en la cola j

### Partida desde la pala j
Si hay camiones en cola
  Generar partida desde la pala j __para el camion i+1__
  Quitar camión i de la cola j
  Generar Arribo al aplastador
Si no
  Poner la pala j em DESOCUPADA

### Arribo al aplastador
Si el aplastador esta DESOCUPADO
  Generar de partida del camion i del aplastador
  Poner al aplastador en OCUPADO
Si no
  Almacenar tiempo llegada del camión i de la pala j
  Poner camión i de la pala j en cola del aplastador

### Partida desde el aplastador
Si hay camiones en cola
  Generar nueva partida
  Quitar camión de la cola
  Generar arribo a la pala j
Si no
  Poner al aplastador en DESOCUPADO
Calcular y actualizar el material procesado

