import time  # Importación para agregar pausas en la ejecución y que tenga comienzo en tiempo
import random  # Importación para seleccionar palabras al azar

class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra.lower()  # Palabra que se tiene que adivinar.
        self.errores = 0  # Contador de errores
        self.max_errores = 6  # Se dejó el número máximo de errores en 6.
        self.progreso = ["_"] * len(palabra)  # Estado actual de las letras adivinadas.
        self.letras_usadas = []  # Letras que ya intentó el jugador
        self.ahorcado_dibujos = [  # Dibujos del ahorcado conforme se va equivocando el jugador.
            '''
  ____   
  |      |  
  |      
  |      
  |      
  |      
  |      
-----     
''',
            '''
  ____   
  |      |  
  |      O
  |      
  |      
  |      
  |      
  |      
-----     
''',
            '''
  ____   
  |      |  
  |      O
  |      |
  |      
  |      
  |      
-----     
''',
            '''
  ____   
  |      |  
  |      O
  |     /|
  |      
  |      
  |      
-----     
''',
            '''
  ____   
  |      |  
  |      O
  |     /|\\
  |      
  |      
  |      
-----     
''',
            '''
  ____   
  |      |  
  |      O
  |     /|\\
  |     / 
  |      
  |      
-----     
''',
            '''
  ____   
  |      |  
  |      O
  |     /|\\
  |     / \\
  |      
  |      
-----     
'''
        ]  # Cierra la lista de dibujos del ahorcado.

    def mostrar_estado(self):  # Es el que ve el avance del juego, tanto letras usadas como el progreso que se tiene.
        print(self.ahorcado_dibujos[self.errores])
        print("Progreso:", " ".join(self.progreso))
        print("Letras usadas:", ", ".join(self.letras_usadas))

    def adivinar_letra(self, letra):  # Procesa una letra adivinada por el usuario.
        letra = letra.lower()

        if len(letra) != 1 or not letra.isalpha():  # Validar si la letra es válida.
            print("Por favor, introduce una sola letra válida.")
            return False

        if letra in self.letras_usadas:  # Validar si la letra ya se ha ingresado o no
            print("Esta letra ya la has usado. Intenta con otra.")
            return False

        self.letras_usadas.append(letra)  # Agregar letra a las usadas

        if letra in self.palabra:  # Procesar letra
            for i in range(len(self.palabra)):
                if self.palabra[i] == letra:
                    self.progreso[i] = letra
            print("¡Acertaste!")  # Si la letra sí se encuentra en la palabra se arroja este mensaje
        else:
            self.errores += 1
            print("Letra incorrecta.")  # Si no se arroja este mensaje

        return True

    def juego_terminado(self):  # Comprueba si el juego ha terminado: victoria o derrota según sea el caso.
        if "".join(self.progreso) == self.palabra:
            print("¡Felicidades, ganaste! La palabra era:", self.palabra)  # Verifica si el progreso del juego es igual a la palabra a adivinar.
            return True
        if self.errores >= self.max_errores:
            print(self.ahorcado_dibujos[self.errores])
            print("GAME OVER. La palabra era:", self.palabra)  # Si el máximo de errores se supera arroja el mensaje de game over
            return True
        return False

    def jugar(self):  # Lógica principal para jugar el juego.
        while not self.juego_terminado():
            self.mostrar_estado()
            letra = input("Elige una letra: ")
            self.adivinar_letra(letra)

# Función login
def login():
    usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")

    if usuario == "Joshua" and contraseña == "12345":
        print("BIENVENIDO", usuario, "comencemos a jugar...")
    else:
        print("Usuario o contraseña incorrectos.")
        return False
    return True

if __name__ == "__main__":
    if not login():
        print("No eres el jugador indicado :D")
    else:
        print("Recuerda que tienes pocos intentos, así que piensa muy bien. Comienza a adivinar la palabra:")
        time.sleep(4)

        
        palabras = ["python", "programacion", "ahorcado", "juego", "codigo"]   # Lista de palabras posibles escogidas de manera aleatoria. 
        palabra = random.choice(palabras)  # Elegir una palabra al azar
        juego = Ahorcado(palabra)
        juego.jugar()
