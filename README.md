# simulacion-tp-integrador-2017
trabajo practico integrador

## Modelo algorítmico:

### Arribo a la pala j
- Si la pala j esta DESOCUPADA
  - Calcular tiempo de carga
  - Generar partida del camión i de la pala j
  - Poner la pala j em OCUPADO
- Si no
  - Agregar camión i a la cola de la pala j

### Partida desde la pala j
- Si hay camiones en cola
  - Generar partida desde la pala j para el camion i
  - Quitar camión i de la cola j
  - Generar Arribo al aplastador
- Si no
  - Poner la pala j em DESOCUPADA

### Arribo al aplastador
- Si el aplastador esta DESOCUPADO
  - Poner al aplastador en OCUPADO
  - Generar de partida del camion i del aplastador
- Si no
  - Poner camión i de la pala j en cola del aplastador
  - Ordenar la cola por prioridades y FIFO en caso de igual tamaño

### Partida desde el aplastador
- Calcular y actualizar el material procesado
- Si hay camiones en cola
  - Quitar camión i de la cola
  - Generar nueva partida, para el camion i + 1
  - Generar arribo del camion i a la pala j
- Si no
  - Poner al aplastador en DESOCUPADO
- Generar el arribo del camion i ala pala j
