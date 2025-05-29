# CREAR UNA FUNCION AL USUARIO QUE INGRESE LAS NOTAS DE VARIOS DE ALUMNOS LAS NOTAS DEBEN ESTAR ENTRE EL 1 Y EL 10. PEDIR AL USUARIO CUANTOS LAUMNOS Y CUANTOS EXAMENES HIZO CADA ALUMNO.
# CREAR UNA TABLA N (CADA ALUMNO = FILA) (CADA EXAMEN = COLUMNA)
# VALIDAR QUE SEA DEL 1 AL 10 Y QUE SEA UN NUMERO (AMBOS CASOS)





def cargar_matriz_notas():

    cantidadAlumnos = int(input("Por favor ingrese la cantidad de alumnos:")) # Pregunto cantidad de alumnos y convierto a int

    cantidadExamenes = int(input("Por favor ingrese la cantidad de exámenes por alumno:")) # Pregunto cantidad cantidad de examenes y convierto a int

    alumnosMatriz = [] # Inicializo la matriz

    for i in range(cantidadAlumnos): # primera iteracion sobre la cantidad de alumnos (fila)
        fila_alumno = [] # cantidad de filas inicialización
        print(f" Ingresando notas para el alumno {i + 1}: ") # aviso de comienzo de ingreso de notas para e alumno X
      
        alumnosMatriz.append(fila_alumno) # inserción de filas
        for j in range(cantidadExamenes): # segunda iteracion sobre examenes
            nota = int(input(f"Por favor ingrese la nota {j + 1} del alumno {i + 1} ")) # le pido al usuario que ingrese la nota X del alumno Y

            if nota < 10 and nota >= 1:

                fila_alumno.append(nota) # Agrego la nota a la fila en el correspondiente lugar depende de que lugar en la interación estamos
            else:
                print("Por favor ingrese una nota correcta entre el 1 al 10.")
                break

    return alumnosMatriz



                  
                  
        
