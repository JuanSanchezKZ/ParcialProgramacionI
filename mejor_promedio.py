from cargar_matriz_notas import cargar_matriz_notas

"""
Calcula el promedio de cada alumno y
determina cuál tiene el mejor promedio. Retorna el índice del alumno y
el valor del promedio.
"""



def mejor_promedio():

    alumnosMatriz = cargar_matriz_notas() # cargo la matriz
    
    
    promedios = [] # Inicializo array de promedios
    for alumnos in alumnosMatriz: # primera iteracion sobre matriz
        totalNotas = 0 # variable de acumulador de notas
        for notas in alumnos: # iteracion sobre notas
            totalNotas = totalNotas + notas # acumulación de notas
            
    
        promedios.append(totalNotas / len(alumnos)) # cálculo de promedios
    promedioMaximoActual = promedios[0] # Asumo que el promedio máximo es el indice 0

    indiceAlumno = 0 # Para encontrar el indice inicializo una variable para guardar el indice actual
    indiceActual = 0 # Y un acumulador para guardar el indice fuera del if
    for prom in promedios: # iteración sobre promedios para calcular el máximo
        if prom > promedioMaximoActual: # sí el promedio siguiente es mayor que el anterior entonces
            promedioMaximoActual = prom # actualizo la variable
            indiceAlumno = indiceActual # sumo si encontró un promedio mas alto nuevo
        indiceActual += 1 # sumo al indice de cualquier manera
                
        
    return [promedioMaximoActual, indiceAlumno]

    


    

 
