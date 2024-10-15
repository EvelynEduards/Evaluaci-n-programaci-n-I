#A) Solicitar al usuario el ingreso de un número entero por consola, validando su tipo de dato (mediante código ASCII) y su pertenencia al rango de 3 y 15, ambos inclusive.

def solicitar_numero_entero(mensaje:str, minimo:int, maximo:int) -> int:
    """
    Esta función verifica si un numero ingresado por el usuario es un entero dentro de un rango entre otros dos numeros enteros.
        Recibe:
            mensaje (str): representa el mensaje a mostrar para el usuario al ingresar el numero
            minimo (int): representa el minimo del rango en el cual se analiza el numero
            maximo (int): representa el maximo del rango en el cual se analiza el numero
        Devuelve:
            numero (int): representa ingresado ya validado
    """

    bandera = False # La inicializamos en False para forzarla a entrar en el siguiente While

    while bandera == False:
        numero = input(mensaje)
        bandera = verificar_digito(numero) # Función para verificar si se puede castear a entero, devuelve True si se puede

    numero = int(numero) # Se castea luego de verificar

    while validar_numero_entero_en_rango(numero, minimo, maximo) != True:
        bandera = False
        while bandera == False:
            numero = input(mensaje)
            bandera = verificar_digito(numero) 

        numero = int(numero) # Se castea luego de verificar
        

    return numero


def verificar_digito(string:str) -> bool:
    """
    Esta funcion verifica si todos los digitos de una cadena son numeros enteros
        Recibe:
            cadena (str): Cadena que se va a iterar para validar sus caracteres.
        Retorna:
            retorno (bool):
                True: Si toda la cadena son digitos del 0 al 9
                False: Si la cadena tiene un caracter que no sea numerico.
    """
    retorno = True
    for digito in string:
        if ord(digito) < 48 or ord(digito) > 57:
            retorno = False
            break

    return retorno



def validar_numero_entero_en_rango(numero:int, minimo:int, maximo:int) -> bool:
    """
    La funcion determina si un numero se encuentra dentro de un rango determinado por dos enteros.
        Recibe:
            numero (int): representa el numero a analizar
            minimo (int): representa el minimo del rango en el cual se analiza el numero
            maximo (int): representa el maximo del rango en el cual se analiza el numero
        Devuelve:
            retorno (bool): True si el numero se encuentra dentro del rango analizado, False en caso de que no y None si alguno de los parametros no son enteros (int)
    """
    retorno = None
    
    if type(numero) == int and type(minimo) == int and type(maximo) == int: # Validacion
        if numero >= minimo and numero <= maximo: # Si numero esta dentro del rango de minimo y maximo
            retorno = True
        
        else:
            retorno = False

    return retorno

#------------------------------------------------------------------------------------------------

#B) Generar una lista de letras mayúsculas aleatorias (utilizar el código ASCII), con una longitud igual al número ingresado en la opción A (no se debe poder generar la lista si el número aún no fue ingresado).

import random

def generar_lista_letras_mayusculas(numero:int) -> list:
    """
    Genera una lista de letras mayúsculas aleatorias con una longitud igual al número ingresado.
        Recibe:
            numero (int): número que indica cuántas letras mayúsculas aleatorias se deben generar
        Devuelve:
            lista_letras (list): lista que contiene las letras mayúsculas generadas
    """
    lista_letras = []  # Inicializamos una lista vacia
    
    for _ in range(numero):  # Usamos el numero directamente en el rango
        letra = chr(random.randint(65, 90))  # Genera una letra mayuscula aleatoria
        lista_letras += [letra]  # Concatenamos la letra generada a la lista
    
    return lista_letras

#C) Mostrar la lista generada, formateada de manera que sea entendible para el usuario (no se debe poder mostrar la lista si ésta aún no ha sido generada).

def mostrar_lista(lista: list) -> None:
    """
    Esta funcion imprime cada elemento de una lista en una nueva linea con su indice
        Recibe:
        lista (list): La lista cuyos elementos se desean imprimir.
        Devuelve:
        None: La funcion imprime los valores de la lista.
    """
    for i in range(len(lista)):
        print(f"Letra {i + 1}: {lista[i]}")


#-----------------------------------------------------------------------------------------

#D) Solicitar al usuario el ingreso de una letra mayúscula por consola, validando que sea una única letra entre la ‘A’ y la ‘Z’. Una vez validada, buscar la letra en la lista generada en la opción B e informar si existe o no. En caso de que exista, también informar en qué posiciones/índices se encuentran. No se debe poder acceder a esta opción si la lista aún no ha sido generada.

def solicitar_letra_mayuscula(mensaje: str) -> str:
    """
    Solicita al usuario ingresar una letra mayuscula y valida su entrada utilizando codigo ASCII.
        Recibe:
            mensaje (str): El mensaje a mostrar al usuario.
                            el string ingresado por el usuario
        Devuelve:
            letra (str): La letra mayuscula ingresada y validada.
    """
    bandera = False
    while bandera == False:
        letra = input(mensaje)
        if len(letra) == 1 and 65 <= ord(letra) <= 90:  # Validamos mayuscula con ASCII
            bandera = True
        else:
            print("Por favor, ingresa una única letra mayuscula entre 'A' y 'Z'.")
    
    return letra


def buscar_letra_en_lista(lista: list, letra: str) -> list:
    """
    Busca una letra en la lista generada y devuelve las posiciones donde se encuentra.
        Recibe:
            lista (list): La lista en la que se busca la letra.
            letra (str): La letra a buscar en la lista.
        Devuelve:
            list: Una lista con las posiciones (indices) donde la letra aparece en la lista original
                  Si no se encuentra la letra, devuelve un mensaje de error
    """
    posiciones = []  # Inicializamos una lista vacía para almacenar posiciones

    for i in range(len(lista)):
        if lista[i] == letra:
            posiciones += [i+1]  # Concatenamos la posición encontrada a la lista


    # Verificamos si hay posiciones encontradas y las mostramos
    if posiciones:
        cadena_posiciones = ""
        primer_elemento = True  # Entra al if 

        for pos in posiciones:
            if primer_elemento:
                cadena_posiciones += str(pos)  # Agrega la primera posicion sin coma, hay que pasarlo a STR para que no tire error
                primer_elemento = False  # Cambia la variable a False después de la primera
            else:
                cadena_posiciones += ", " + str(pos)  # Agrega las posiciones siguientes con coma

        print(f"La letra '{letra}' está en la posicion: {cadena_posiciones}.")
    else:
        print(f"La letra '{letra}' no está en la lista.")


# E) Solicitar al usuario el ingreso de una cadena de caracteres “ASC” o “DESC” por consola y validarla.Luego, ordenar una COPIA de la lista generada en la opción B según el criterio ingresado por el usuario, y mostrarla. No se debe poder acceder a esta opción si la lista aún no ha sido generada y la lista original no debe ser modificada.

def solicitar_criterio(mensaje: str) -> str:
    """
    Solicita al usuario ingresar un criterio de ordenamiento (ASC o DESC) y valida la entrada.
        Recibe:
            mensaje (str): El mensaje a mostrar al usuario.
        Devuelve:
            criterio (str): El criterio ingresado y validado.
    """
    criterio = input(mensaje)
    while criterio != "ASC" and criterio != "DESC":
        print("Por favor, ingresa 'ASC' o 'DESC'.")
        criterio = input(mensaje)
    else:
        return criterio
            

def ordenar_lista(lista: list, criterio: str = "ASC") -> list:
    """
    Ordena una copia de la lista segun el criterio ingresado (ASC o DESC).
        Recibe:
            lista (list): La lista que se desea ordenar.
            criterio (str): El criterio de ordenamiento (ASC o DESC).
        Devuelve:
            list: Una nueva lista ordenada según el criterio especificado.
    """
    lista_ordenada = lista[:] # Hacemos una copia de la lista
   

    for i in range(len(lista_ordenada) - 1):
        for j in range(i + 1, len(lista_ordenada)):
            if (criterio == "ASC" and lista_ordenada[i] > lista_ordenada[j]) or (criterio == "DESC" and lista_ordenada[i] < lista_ordenada[j]):
                aux = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[j]
                lista_ordenada[j] = aux
                

    return lista_ordenada


#F) Solicitar al usuario el ingreso de dos (2) números enteros por consola, validando su tipo de dato (mediante código ASCII) y su pertenencia al rango de 3 a 10, ambos inclusive. El primer número representará la cantidad de filas, y el segundo, la cantidad de columnas.

def solicitar_dos_numeros_enteros(mensaje_filas: str, mensaje_columnas: str, minimo: int, maximo: int) -> list:
    """
    Solicita al usuario el ingreso de dos numeros enteros por consola, validando su tipo de dato
    y su pertenencia al rango especificado.

    Recibe:
        mensaje_filas (str): Mensaje a mostrar al usuario para ingresar la cantidad de filas.
        mensaje_columnas (str): Mensaje a mostrar al usuario para ingresar la cantidad de columnas.
        minimo (int): Valor minimo del rango.
        maximo (int): Valor maximo del rango.

    Devuelve:
        list: Una lista con los dos numeros ingresados y validados [filas, columnas].
    """
    filas = solicitar_numero_entero(mensaje_filas, minimo, maximo)  # Se solicita el numero de filas
    columnas = solicitar_numero_entero(mensaje_columnas, minimo, maximo)  # Se solicita el numero de columnas
    
    return [filas, columnas]  # Devolvemos una lista con las filas y columnas

# G) Generar una matriz de números enteros aleatorios entre 1 y 9, utilizando los números ingresados en la opción F como cantidad de filas y columnas. No se debe poder acceder a esta opción si el usuario aún no ha ingresado la cantidad de filas y columnas.

def obtener_filas(filas_columnas: list) -> int:
    """
    Obtiene la cantidad de filas de la lista de filas y columnas.
    
    Recibe:
        filas_columnas (list): Lista que contiene las cantidades de filas y columnas.

    Devuelve:
        int: La cantidad de filas.
    """
    return filas_columnas[0]  # Retorna la primera parte (filas) de la lista

def obtener_columnas(filas_columnas: list) -> int:
    """
    Obtiene la cantidad de columnas de la lista de filas y columnas.
    
    Recibe:
        filas_columnas (list): Lista que contiene las cantidades de filas y columnas.

    Devuelve:
        int: La cantidad de columnas.
    """
    return filas_columnas[1]  # Retorna la segunda parte (columnas) de la lista

def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_inicial) -> list:
    """
    Crea una matriz de tamaño especificado y la inicializa con un valor dado previamente.

    Recibe:
    - cant_filas (int): Numero de filas de la matriz.
    - cant_columnas (int): Numero de columnas de la matriz.
    - valor_inicial: Valor con el que se inicializan todos los elementos de la matriz.

    Retorno:
    - list: La matriz inicializada.
    """
    matriz = []
    for _ in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz


def generar_matriz_aleatoria(cant_filas: int, cant_columnas: int) -> list:
    """
    Genera una matriz de números aleatorios entre 1 y 9.

    Recibe:
    - cant_filas (int): Numero de filas de la matriz.
    - cant_columnas (int): Numero de columnas de la matriz.

    Retorno:
    - list: Matriz generada con numeros aleatorios.
    """
    matriz = inicializar_matriz(cant_filas, cant_columnas, 0)  # Inicializamos la matriz con ceros
    
    # Rellenamos la matriz con numeros aleatorios
    for i in range(cant_filas):
        for j in range(cant_columnas):
            matriz[i][j] = random.randint(1, 9)  # Asignamos un número aleatorio a cada posición

    return matriz


#H) Mostrar la matriz generada en la opción G, separando las filas entre sí con guiones medios (“-”) y las columnas con barras verticales (“|”). No se debe poder acceder a esta opción si la matriz aún no ha sido generada.

def mostrar_matriz(matriz: list) -> None:
    """
    Imprime los elementos de una matriz fila por fila, 
    separando las filas con guiones y las columnas con barras.

    Recibe:
    - matriz (list): La matriz que se quiere mostrar.

    Retorno:
    - None: No devuelve ningun valor. Solo imprime la matriz.
    """
    for i in range(len(matriz)):  #len(matriz)=cant filas i= 0,1,2
        for j in range(len(matriz[i])): #Devuelve el total de las columnas j=indice columnas
            print(matriz[i][j], end="") #Se imprimen los elementos de la matriz, sin salto de linea
            if j < len(matriz[i]) - 1:  # Imprimir hasta el anteultimo elemento (cant elem -1)
                print(" | ", end="")  # Separador de columnas

        print("")  # Nueva línea al finalizar la fila
        
        if i < len(matriz) - 1:  # Imprimir hasta el anteultimo elemento
            print("-" * (len(matriz[i]) * 4 - 3))  # Separador de filas
