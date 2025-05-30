from cargar_matriz_notas import cargar_matriz_notas



def porcentaje_aprobados():
    
    alumnosMatriz = cargar_matriz_notas()
    indice = 0
    for notas_alumnos in alumnosMatriz:
        indice = indice + 1 # Creo una variable indice para poder mostrar en que alumno estamos parados mas claramente
        totalNotas = 0 # inicializo el total de notas
        notasAprobadas = 0 #inicializo el total de notas aprobadas por cada alumno
        promedio = 0 # inicializo variable promedio
        porcentajeAprobadas = 0
        for nota in notas_alumnos: # recorro las notas de cada alumno
            totalNotas += nota # acumulo las notas 
            promedio = totalNotas / len(notas_alumnos)
            if nota >= 6:
                notasAprobadas = notasAprobadas + 1 # si esta aprobada se cuenta + 1 a la variable para luego hacer un porcentaje contra la cantidad de examenes
                porcentajeAprobadas = (notasAprobadas / len(notas_alumnos)) * 100 # Calculo el el porcentaje
        
        
         # printeo el informe
        print(f"El alumno {indice} tiene un promedio de {promedio}. ") 
        print (f"El alumno {indice} tiene un porcentaje de {porcentajeAprobadas}% examenes aprobados.")
