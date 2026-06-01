import random
import time
import os
from colorama import Fore, Style, init, Back
 
# inicia la libreria colorama
init(autoreset=True)  # después de cada print vuelve al color original
 
# diccionario - opciones de colores
colores_dict = {
    'rojo': Fore.RED,
    'verde': Fore.GREEN,
    'azul': Fore.BLUE,
    'amarillo': Fore.YELLOW,
    'morado': Fore.MAGENTA,
    'celeste': Fore.CYAN
}
 
 
# mostrar reglas
def mostrar_reglas():
    print(Style.BRIGHT + Fore.MAGENTA + "=== SECUENCIA DE COLORES ===" + Style.RESET_ALL)
    reglas = [
        "1) Se te mostrará una secuencia de colores",
        "2) Tienes 3 segundos para memorizarla",
        "3) La secuencia se borrara despues de los 3 segundos",
        "4) Después de 3 rondas se aúmentara la dificultad",
        "5) Si fallas 3 veces se acaba el juego"
    ]
    for regla in reglas:
        print(Fore.CYAN + regla + Style.RESET_ALL)
    input(Fore.RED + "Presiona Enter para continuar..." + Style.RESET_ALL)
 
 
def cuenta_regresiva():
    print('\n' * 30)
    print(Back.RED + Style.BRIGHT + '    3    ')
    time.sleep(1)
    print('\n' * 30)
    print(Back.RED + Style.BRIGHT + '    2    ')
    time.sleep(1)
    print('\n' * 20)
    print(Back.RED + Style.BRIGHT + '    1    ')
    time.sleep(1)
    print('\n' * 20)
    print(Back.GREEN + Style.BRIGHT + '    GO    ')
    time.sleep(1)
    print('\n' * 20)
 
 
# FIX 3: inicializa el archivo de scores si no existe
def inicializar_scores():
    if not os.path.exists("scores.txt"):
        open("scores.txt", "w").close()
 
 
# tabla de scores
def tabla_scores(nombre, score):
    # FIX 1: no guardar si el nombre esta vacio
    if not nombre.strip():
        print(Fore.YELLOW + "Nombre vacío, puntaje no guardado." + Style.RESET_ALL)
        return
 
    with open("scores.txt", "a") as file:  # a = añade texto sin borrar lo anterior
        file.write(f"{score}:{nombre}\n")  # escribe una linea nueva con el formato score:nombre
 
    all_scores = []
    with open('scores.txt', 'r') as file:  # r = lee, with cierra el archivo cuando acaba
        lines = file.readlines()  # leen todas las líneas
 
    for line in lines:
        try:
            parts = line.strip().split(':')  # elimina espacios y divide en dos partes
            score_value = int(parts[0].strip())  # antes del : convierte a entero
            name = parts[1].strip()  # toma dps del :
            all_scores.append((score_value, name))  # añade la tupla
        except (IndexError, ValueError):
            continue
 
    # lambda: forma corta de definir una función
    all_scores.sort(key=lambda x: x[0], reverse=True)  # ordena de mayor a menor
    top_five = all_scores[0:5]
 
    print(Style.BRIGHT + Fore.MAGENTA + "\n=== TOP 5 MEJORES PUNTAJES ===" + Style.RESET_ALL)
    for i, (s, n) in enumerate(top_five):
        print(Fore.CYAN + f"{i + 1}. {n}: {s}" + Style.RESET_ALL)
 
 
# juego
def secuencia(lista):
    ronda = 0
    intentos = 3
    score = 0
    nombre = ''
 
    while intentos > 0:
        # longitud de secuencia y bonus por ronda
        # FIX 2: bonus como enteros para evitar floats en el score
        if ronda <= 3:
            longitud = 3
            bonus = 100
            tiempo = 3
        elif ronda <= 6:
            longitud = 4
            bonus = 150
            tiempo = 3
        elif ronda <= 10:
            longitud = 5
            bonus = 200
            tiempo = 2
        elif ronda <= 15:
            longitud = 6
            bonus = 300
            tiempo = 2
        else:
            longitud = 6
            bonus = 400
            tiempo = 1.5
 
        # FIX 4: shuffle sobre una copia nueva cada ronda para no mutar la lista original
        lista_colores = lista[:]
        random.shuffle(lista_colores)
        lista_memoria = lista_colores[:longitud]
 
        # muestra secuencia con colores
        secuencia_con_colores = []
        for nombre_color in lista_memoria:
            # obtiene el color y si no existe devuelve blanco
            codigo_color = colores_dict.get(nombre_color, Fore.WHITE)
            secuencia_con_colores.append(f"{codigo_color}{nombre_color}")
        secuencia_final = ', '.join(secuencia_con_colores)
 
        print(f'ronda {ronda + 1}')
        print(f"score: {score}")
        print(f"intentos restantes: {intentos}")
        time.sleep(2)
        cuenta_regresiva()
        print(secuencia_final)
        time.sleep(tiempo)
        print('\n' * 30)
 
        # respuesta del usuario
        respuesta = input("Escribe la secuencia completa con comas: ").lower().replace(" ", "")
        secuencia_usuario = respuesta.split(",")
 
        # verificar respuesta
        if secuencia_usuario == lista_memoria:
            print(Fore.GREEN + "CORRECTO! --> siguiente ronda")
            ronda += 1
            time.sleep(2)
            score += bonus  # FIX 2: score siempre es entero
        else:
            print(Fore.RED + "INCORRECTO")
            print("La secuencia correcta es: " + ",".join(lista_memoria))
            intentos -= 1
            print(Fore.BLACK + f"Te quedan {intentos} intentos.\n")
            time.sleep(3)
 
        # fin del juego - perdiste
        if intentos <= 0:
            print(Back.BLACK + Style.BRIGHT + Fore.RED + "JUEGO TERMINADO" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Tu puntaje final es: {score}" + Style.RESET_ALL)
            nombre = input("Ingresa tu nombre para guardar tu puntaje: ")
            break
 
        # fin del juego - ganaste
        if ronda == 10:
            print(Back.BLACK + Style.BRIGHT + Fore.GREEN + "FELICIDADES, GANASTE!" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Tu puntaje final es: {score}" + Style.RESET_ALL)
            endless = input('Quieres jugar en endless mode? (S/N): ').upper()
            if endless == 'S':
                ronda += 1
            else:
                nombre = input("Ingresa tu nombre para guardar tu puntaje: ")
                break
 
    return nombre, score  # FIX 2: ya no necesita int() porque score siempre fue entero
 
 
def main():
    inicializar_scores()  # FIX 3: asegura que scores.txt existe antes de leerlo
    mostrar_reglas()
    lista = list(colores_dict.keys())  # devuelve las claves
    nombre_jugador, puntaje = secuencia(lista)
    tabla_scores(nombre_jugador, puntaje)
 
 