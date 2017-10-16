# simulacion-tp-integrador-2017
trabajo preactico integrador

## Modelo algorítmico:
### Arribo a la pala j
  Si EstadoPala j = ‘D’
      Calcular tCarga
      Generar Partida camión ij
      Poner EstadoPala j = ‘O’
  Si no
      Agregar camión ij en la cola j

### Partida desde la pala j
  Si hay camiones en cola
      Generar partida desde la pala j
      Quitar camión de la cola j
  Si no
      Poner EstadoPala j = ‘D’
  Calcular tiempoIda
  Generar Arribo al aplastador

### Arribo al aplastador
  Si EstadoAplastador = ‘D’
      Generar tiempoDescarga
      Generar partida desde el aplastador
      Poner EstadoAplastador = ‘O’
  Si no
      Almacenar tiempo llegada del camión ij
      Poner camión ij en la cola

### Partida desde el aplastador
  Si hay camiones en cola
      Generar nueva partida
      Quitar camión de la cola
  Si no
      EstadoAplastador = ‘D’
  Calcular tiempoVuelta
  Generar arribo a la pala j
  Calcular y actualizar el material procesado

