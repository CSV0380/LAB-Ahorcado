import random

#EJERCICIO 1:

#apartado a

def cargar_palabras(fichero):
    with open(fichero, encoding= 'utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res

#apartado b

def elegir_palabra(palabras):
    return random.choice(palabras)


#apartado c

def enmascarar_palabra(palabra, letras_probadas):
    res = []
    
    for letra in palabra:
        if letra in letras_probadas: # Verificar si la letra está en el conjunto
            res.append(letra)
        else:
            res.append('_')
    return ' '.join(res)


#apartado d

def pedir_letra(letras_probadas):
    while True:
        siguiente_letra = input("Adivina una letra: ").lower()  # Usamos lower() para hacer la letra en minúsculas
        if siguiente_letra in letras_probadas:
            print("Ya has probado con esa letra. Intenta con otra.")
        else:
            return siguiente_letra  # Devolvemos la letra si no ha sido probada antes



#apartado e

def comprobar_letra(palabra_secreta, letra):
    if letra in palabra_secreta:
        print(f"¡Bien hecho! Esa letra está en la palabra.")
        return True
    else:
        print(f"Lo siento, esa letra no está en la palabra.")
        return False



#apartado f

def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    for letra in palabra_secreta:
        if letra not in letras_probadas:
            return False
    return True 


#apartado g

def ejecutar_turno(palabra_secreta, letras_probadas):
    print(f"Palabra: {enmascarar_palabra(palabra_secreta, letras_probadas)}")
    letra = pedir_letra(letras_probadas)
    acierto = comprobar_letra(palabra_secreta, letra)
    letras_probadas.add(letra)
    return acierto








#EJERCICIO 2:

#apartado a

def jugar(palabras):
    print("Bienveido al juego del Ahorcado!!!!") #🎂🎂🎂🎂
    palabra_secreta = elegir_palabra(palabras)
    
    #Cuando te piden inicializar las variables hay que hacer esto:
    letras_probadas = set()
    intentos_fallidos = 0
    
    max_intentos = int(input("Dime el número de intentos que quieres jugar: "))
    
    while intentos_fallidos < max_intentos:
        print(f"\nIntentos fallidos: {intentos_fallidos}/{max_intentos}")
       
        acierto = ejecutar_turno(palabra_secreta, letras_probadas)
        if not acierto:
            intentos_fallidos += 1

        if comprobar_palabra_completa(palabra_secreta, letras_probadas):
            print(f"¡Felicidades! Has adivinado la palabra '{palabra_secreta}' correctamente.")
            break  #ROMPER EL BUCLE💣💣💣💣💣🧨🧨🧨🧨

        if intentos_fallidos >= max_intentos:
            print(f"¡Has perdido! La palabra secreta era '{palabra_secreta}'.")
            break  #ROMPER EL BUCLE💣💣💣💣💣🧨🧨🧨🧨


if __name__ == "__main__":
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(palabras)