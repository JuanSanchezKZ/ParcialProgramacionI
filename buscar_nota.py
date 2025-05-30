from cargar_matriz_notas import cargar_matriz_notas


def buscar_nota():

    flag = True # bandera para cortar el while
    
    while flag:
        notaABuscar = input("Por favor ingrese una nota del 1 al 10:") # pido al usuario una nota

        if notaABuscar.isdigit(): # verifico que sea numero
            notaABuscar = int(notaABuscar) # convierto a int si es asi
            

            if notaABuscar >= 1 and notaABuscar <= 10: # verifico que sea del 1 al 10
                print("Carga de nota exitosa.") # aviso de carga exitosa
                flag = False # corto el while si la carga fue exitosa
            else:
                print("Por favor ingrese un número válido del 1 al 10")
        else:
            print("Por favor ingrese un número.")    



    alumnosMatriz = cargar_matriz_notas() # cargo la matriz
    notasPosicionesEncontradas = [] # inicializo lista vacia de indices
    fila = 0 # indice de filas a encontrar
    
    for alumnos in alumnosMatriz: # recorro la matriz
        columna = 0 # indice de columnas a encontrar que se reiniciara en cada iteracion de filas
       
        for notas in alumnos: # itero notas
            if notaABuscar == notas: # si la nota es igual a la pedida entonces
                notasPosicionesEncontradas.append(fila) # agrego los indices 
                notasPosicionesEncontradas.append(columna)
            columna += 1 # sumo para saber donde estoy parado        
        fila += 1
        

    return notasPosicionesEncontradas # retorno los indices

            