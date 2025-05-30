from cargar_matriz_notas import cargar_matriz_notas


def buscar_nota():

    flag = True
    while flag:
        notaABuscar = input("Por favor ingrese una nota del 1 al 10:")

        if notaABuscar.isdigit():
            notaABuscar = int(notaABuscar)
            

            if notaABuscar >= 1 and notaABuscar <= 10:
                print("Carga de nota exitosa.")
                flag = False
            else:
                print("Por favor ingrese un número válido del 1 al 10")
        else:
            print("Por favor ingrese un número.")    



    alumnosMatriz = cargar_matriz_notas()
    notasPosicionesEncontradas = []
    fila = 0
    
    for alumnos in alumnosMatriz:
        columna = 0
       
        for notas in alumnos:
            if notaABuscar == notas:
                notasPosicionesEncontradas.append(fila)
                notasPosicionesEncontradas.append(columna)
            columna += 1        
        fila += 1
        

    return notasPosicionesEncontradas

            