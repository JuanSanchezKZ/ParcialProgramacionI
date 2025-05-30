from cargar_matriz_notas import cargar_matriz_notas
from porcentaje_aprobados import porcentaje_aprobados
from mejor_promedio import mejor_promedio
from buscar_nota import buscar_nota

print("##### MENU DE OPCIONES ELIJA EL NUMERO DE LA OPCION #####")
print("##### 1) CARGAR NOTA DE EXAMENES DE ALUMNOS #####")
print("##### 2) CALCULAR PORCENTAJE EXAMENES APROBADOS POR CADA ALUMNO #####")
print("##### 3) CALCULAR EL MEJOR PROMEDIO DE TODOS LOS ALUMNOS #####")
print("##### 4) BUSCAR UNA NOTA EN LA TABLA DE ALUMNOS Y EXAMENES #####") # Menu descriptivo

flag = True # bandera para cortar el while

while flag:

    opcion = input("Por favor elija una opción:") # input de usuario para elegir opcion

    if opcion.isdigit():

        opcion = int(opcion) # convierto a int si es un digito el input

        if opcion >= 1 and opcion <= 4: # si la opcion esta entre los numeros validos cortamos el while
            flag = False
        else:
            print("Por favor ingrese una opción válida del 1 al 4.") # si no le pedimos que ingrese de vuelta un numero valido   
    else:
        print("Por favor ingrese un número")

if opcion == 1: #elif de selccion de funcion dependiendo de la opcion
    cargar_matriz_notas()
elif opcion == 2:
    porcentaje_aprobados()
elif opcion == 3:
    valor = mejor_promedio()
    print(f"El alumno con mejor promedio tiene el índice de {valor[1]} y un promedio de {valor[0]}") # ya que mejor_promedio devuelve un array usamos sus valores [1] y [0] en ese orden
else:
    valor = buscar_nota()
    print (f"Las índices de la nota buscada son {valor}") # printeamos el valor que devuelve buscar_nota