# Tarea 0: Star Avanced :school_satchel:

***


## Consideraciones Generales

* El código se basa en la programación orientada a objetos, ya que simplifica el entendimiento de éste y además es más rápido en comparación a usar listas de listas, en el caso de la función print_tablero(tablero, uft-8)

Código Utilizado

```go
   def print_celdas(self):
      print("Estado Actual del Tablero:")
      lista_casillas = [[celda.info for celda in row] for row in self.casillas]
      print_tablero_con_utf8(lista_casillas)
```


En este caso, utilizar un objeto, fue más simple que una lista de listas
### Cosas implementadas y no implementadas 

* **Parte Civilizaciones**:
    * **Parte Recursos**: Hecha completa
    * **Parte Personas**: Hecha completa
* **Parte Funcionalidades**:

## Ejecución
El módulo principal de la tarea a ejecutar es  ```main.py```.

## Librerías
### Librerías externas utilizadas
La lista de librerías externas que utilicé fueron las siguientes:

1. ```random```: ```randit()```, ```choice()```
2. ```os```: ```listdir()``` 
3. ```math``` : ```ceil()```
4. ```string```: ```ascii_lowercase()```
4. ```tablero```: ```print_tablero_con_utf8()```


### [Estilo de Texto](https://github.com/markdown-it/markdown-it-deflist)

   Idioma
Lenguaje : Castellano

### Archivo de Estensión .txt
las partidas se guardan dentro de la carpeta partidas.
Cada rchivo .txt posee el siguiente formato:
* Estado partida (completo o incompleto)
* Nombre usuario
* Puntaje
* Alto del tablero
* Ancho del tablero
* Casillas
La cantidad de lineas en casillas depende del alto del tablero y son los estados de las casillas al 
momento de guardar, separados por una coma






