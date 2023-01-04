import os
#Interfaz
INTERFAZ_ANCHO = 500
INTERFAZ_ALTO = 500
INTERFAZ_MARGEN_PRINCIPAL = 200
# Teclas
TECLA_DERECHA = "a"
TECLA_IZQUIERDA = "d"
TECLA_CHEATCODE_KO = "k"

# Ventana juego
LIMITE_IZQUIERDA = 0
LIMITE_DERECHA = 800
LIMITE_ARRIBA = 161
LIMITE_ABAJO = 750
LIMITE_VIDA = 740

# Plataforma
ANCHO_PLATAFORMA = 181
ALTO_PLATAFORMA = 31
POS_INICIAL_X_PLATAFORMA = 310
POS_INICIAL_Y_PLATAFORMA = 650
VELOCIDAD_PLATAFORMA = 15

#dimensiones labels
ANCHO_PLANTA = 40
ALTO_PLANTA = 50
POSICIONES_JARDIN = ((310, 120, 800, 240))

# Rutas
# sprites
RUTA_LOGO = os.path.join('sprites', 'Elementos de juego', 'logo.png')
RUTA_GAMEOVER = os.path.join('sprites', 'Elementos de juego', 'textoFinal')
RUTA_FONDO = os.path.join('sprites', 'Fondos', 'fondoMenu.png')

#ventana juego
#plantas
RUTA_PLANTA_GIRASOL = os.path.join('sprites', 'Plantas', 'girasol_1.png')
RUTA_PLANTA_CLASICA = os.path.join('sprites', 'Plantas', 'lanzaguisantes_1.png')
RUTA_PLANTA_AZUL = os.path.join('sprites', 'Plantas', 'lanzaguisantesHielo_1.png')
RUTA_PLANTA_PAPA = os.path.join('sprites', 'Plantas', 'papa_1.png')
#zombies
RUTA_ZOMBIE_CLASICO = os.path.join('sprites', 'Zombies', 'Caminando', 'zombieNicoWalker_1.png')
RUTA_ZOMBIE_RAPIDO = os.path.join('sprites', 'Zombies','Caminando',  'zombieHernanRunner_1.png')
RUTA_GUISANTE = os.path.join('sprites', 'Elementos de juego', 'guisante_1.png')
#ventana ranking
RUTA_ICONO_SOL = os.path.join('sprites', 'Elementos de juego', 'sol.png')

# escenas
RUTA_FONDO_ABUELA = os.path.join('sprites', 'Fondos', 'jardinAbuela.png')
RUTA_FONDO_NOCTURNO = os.path.join('sprites', 'Fondos', 'salidaNocturna.png')

# ui files
RUTA_UI_VENTANA_INICIO= os.path.join(
    'frontend', 'assets', 'ui files', 'ventana_inicio.ui'
)
RUTA_UI_VENTANA_PRINCIPAL = os.path.join(
    'frontend', 'assets', 'ui files', 'ventana_principal.ui'
)

RUTA_UI_VENTANA_JUEGO = os.path.join(
    'frontend', 'assets', 'ui files', 'ventana_juego.ui'
)
RUTA_UI_VENTANA_RANKING= os.path.join(
    'frontend', 'assets', 'ui files', 'ventana_ranking.ui'
)
RUTA_UI_VENTANA_POST_RONDA= os.path.join(
    'frontend', 'assets', 'ui files', 'ventana_post_ronda.ui'
)

POS_SOL_HIDE = 0, 0
# Los intervalos están en milisegundos
INTERVALO_APARICION_SOLES = 2000
INTERVALO_DISPARO = 2000 
INTERVALO_SOLES_GIRASOL = 20000
INTERVALO_TIEMPO_MORDIDA = 5000
RANGO_APARICION_SOL = 200
# El daño y la vida tienen las mismas medidas
DANO_PROYECTIL = 5
DANO_MORDIDA = 5
VIDA_PLANTA = 100
VIDA_ZOMBIE = 80
# Número de zombies por carril
N_ZOMBIES = 7
# Porcentaje de ralentización
RALENTIZAR_ZOMBIE = 0.25
# Soles iniciales por ronda
SOLES_INICIALES = 250
# Número de soles generados por planta
CANTIDAD_SOLES = 2
# Número de soles agregados a la cuenta por recolección
SOLES_POR_RECOLECCION = 50
# Número de soles agregados a la cuenta por Cheatcode
SOLES_EXTRA = 25
# Ponderadores de escenarios
PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9
# La velocidad del zombie en milisegundos
VELOCIDAD_ZOMBIE = 5000
# Puntaje por eliminar zombie
PUNTAJE_ZOMBIE_DIURNO = 50
PUNTAJE_ZOMBIE_NOCTURNO = 100
# Costo por avanzar de ronda
COSTO_AVANZAR = 500
# Costo tiendas
COSTO_LANZAGUISANTE = 50
COSTO_LANZAGUISANTE_HIELO = 100
COSTO_GIRASOL = 50
COSTO_PAPA = 75
# Caracteres de nombre usuario
MIN_CARACTERES = 3
MAX_CARACTERES = 15

POSICION_PLANTAS = 310, 120, 800, 120