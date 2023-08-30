import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    
    while True:
        eleccion_usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
        
        if eleccion_usuario == 'salir':
            print("¡Gracias por jugar!")
            break
        
        if eleccion_usuario not in opciones:
            print("Esa no es una opción válida. Por favor, elige piedra, papel o tijera.")
            continue
        
        eleccion_computadora = random.choice(opciones)
        
        print(f"Tú elegiste: {eleccion_usuario}")
        print(f"La computadora eligió: {eleccion_computadora}")
        
        if eleccion_usuario == eleccion_computadora:
            print("¡Es un empate!")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("¡Tú ganas!")
        else:
            print("¡La computadora gana!")

jugar()