from ahorcado import *

def test_cargar_palabras(fichero):
    print("Testeando cargar_palabras()... ")
    palabras = cargar_palabras(fichero)
    print(f"Palabras cargadas: {len(palabras)}")
    print("Primeras 3 palabras:", palabras[:3])
    print("Últimas 3 palabras:", palabras[-3:])


def test_elegir_palabra(palabras):
    palabra = elegir_palabra(palabras)
    print(f"Palabra elegida: {palabra}")


def test_enmascarar_palabra(palabra, letras_probadas):
    print(f"Testeando enmascarar_palabra() con la palabra '{palabra}' y las letras ({','.join(letras_probadas)})... ")
    resultado = enmascarar_palabra(palabra, letras_probadas)
    print(f"Palabra enmascarada: {resultado}")
    print()


def test_pedir_letra(letras_probadas):
    print(f"Testeando pedir_letra() con las letras ({','.join(letras_probadas)})... ")
    letra = pedir_letra(letras_probadas)
    print(f"Letra introducida: {letra}")


def test_comprobar_letra(palabra_secreta, letra):
    print(f"Testeando comprobar_letra() con la palabra '{palabra_secreta}' y la letra '{letra}'... ")
    acierto = comprobar_letra(palabra_secreta, letra)
    print(f"Resultado: {'Acierto' if acierto else 'Fallo'}")
    print()


def test_compobar_palabra_completa(palabra_secreta, letras_probadas):
    print(f"Testeando enmascarar_palabra() con la palabra '{palabra_secreta}' y las letras ({', '.join(letras_probadas)})... ")
    resultado = comprobar_palabra_completa(palabra_secreta, letras_probadas)
    print(f"Resultado: {'Completa' if resultado else 'Incompleta'}")
    print()


def test_ejecutar_turno(palabra_secreta, letras_probadas):
    print(f"Testeando ejecutar_turno() con la palabra '{palabra_secreta}' y las letras ({','.join(letras_probadas)})... ")
    acierto = ejecutar_turno(palabra_secreta, letras_probadas)
    print(f"Resultado: {'Acierto' if acierto else 'Fallo'}")
    print()





if __name__ == '__main__':
    #test_cargar_palabras('data\palabras_ahorcado.txt')
    #palabras = cargar_palabras('data\palabras_ahorcado.txt')
    #test_elegir_palabra(palabras)
    #test_enmascarar_palabra("python", set()) #conjunto vacío para que no se repitan las letras
    #test_enmascarar_palabra("python", {'p', 'y', 'o', 't', 'h', 'n'})
    #test_enmascarar_palabra("python", {'e', 'b', 'd', 'a', 'c'})
    #test_enmascarar_palabra("python", {'e', 'u', 'o', 'i', 'a'})
    #test_pedir_letra({'a', 'b', 'c'}) 
    #test_comprobar_letra("python","s")
    #test_compobar_palabra_completa('python', {'p', 'y', 't', 'h', 'o', 'n'})
    #test_compobar_palabra_completa('python', {'a', 'b', 'c', 'd', 'e'})
    #test_compobar_palabra_completa('python', {})
    test_ejecutar_turno("python", {"y","o","h","t","p"})