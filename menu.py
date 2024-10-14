from biblioteca import * 

# Variables
numero_ingresado = None
lista_letras = []
dimensiones = None
matriz_aleatoria = None


menu = """
Seleccione una opción:
A - Solicitar número entero (entre 3 y 15)
B - Generar lista de letras mayúsculas
C - Mostrar la lista generada
D - Buscar una letra en la lista generada
E - Ordenar la lista por ASC O DESC
F - Escribir fila y columna de la matriz
G - Generar Matriz Aleatoria
H - Mostrar Matriz Aleatoria
I - Salir
"""

respuesta = "N"

while respuesta == "N":
    opcion_seleccionada = input(menu)
    
    match opcion_seleccionada:
        case "A":
            numero_ingresado = solicitar_numero_entero("Ingresa un número entre 3 y 15: ", 3, 15)
        
        case "B":
            #Generar y mostrar la lista de letras mayusculas
            if numero_ingresado != None:  # Verificamos si la variable "numero_ingresado" tiene un valor valido (número ingresado)
                lista_letras = generar_lista_letras_mayusculas(numero_ingresado)
            else:
                print("Primero ingresa el numero en la opción A")
        
        case "C":
            if not lista_letras:
                print("Genera una lista en la opción B antes de mostrarla.")
            else:
                mostrar_lista(lista_letras)  # Mostrar la lista 
    
        
        case "D":
            if not lista_letras:
                print("Genera una lista en la opción B antes de buscar una letra.")
            else:
                print("Opción D: Buscar una letra en la lista")
                letra = solicitar_letra_mayuscula("Ingresa una letra mayúscula entre 'A' y 'Z': ")
                buscar_letra_en_lista(lista_letras, letra) 
        
        case "E":
            if not lista_letras:
                print("Genera una lista en la opción B antes de ordenar.")
            else:
                criterio = solicitar_criterio("Ingresa el criterio de ordenamiento (ASC o DESC): ")
                lista_ordenada = ordenar_lista(lista_letras, criterio)
                mostrar_lista(lista_ordenada)  # Mostrar la lista

        case "F":
            dimensiones = solicitar_dos_numeros_enteros("Ingresa la cantidad de filas (entre 3 y 10): ", 
                                                 "Ingresa la cantidad de columnas (entre 3 y 10): ", 
                                                 3, 10)   
            
        case "G":
            if dimensiones == None:
                print("Escribí la cantidad de filas y columnas en el punto F.")
            else:  
                filas = obtener_filas(dimensiones)     # Obtener filas y columnas de las dimensiones
                columnas = obtener_columnas(dimensiones)

                matriz_aleatoria = generar_matriz_aleatoria(filas, columnas)  # Generar matriz aleatoria

        case "H":
            if not matriz_aleatoria:  # Verifica si la matriz esta vacia
                print("Genera primero la matriz en la opción G antes de mostrarla.")
            else:
                mostrar_matriz(matriz_aleatoria)  # Mostrar la matriz generada 

        case "I":
            respuesta = input("¿Desea salir y terminar el programa? S/N: ")
            if respuesta != "S":
                respuesta = "N"  # Si no elige salir, continua el ciclo
        
        case _:
            print("La opción ingresada no es correcta.")


