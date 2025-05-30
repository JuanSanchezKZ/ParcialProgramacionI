from cargar_matriz_notas import cargar_matriz_notas
from porcentaje_aprobados import porcentaje_aprobados
from mejor_promedio import mejor_promedio
from buscar_nota import buscar_nota

print("##### MENU DE OPCIONES ELIJA EL NUMERO DE LA OPCION #####")
print("##### 1) CARGAR NOTA DE EXAMENES DE ALUMNOS #####")
print("##### 2) CALCULAR PORCENTAJE EXAMENES APROBADOS POR CADA ALUMNO #####")
print("##### 3) CALCULAR EL MEJOR PROMEDIO DE TODOS LOS ALUMNOS #####")
print("##### 4) BUSCAR UNA NOTA EN LA TABLA DE ALUMNOS Y EXAMENES #####")
flag = True
while flag:
    opcion = int(input("Por favor elija una opción:"))

    if opcion >= 1 and opcion <= 4:
        flag = False
    else:
        print("Por favor ingrese una opción válida del 1 al 4.")      

if opcion == 1:
    cargar_matriz_notas()
elif opcion == 2:
    porcentaje_aprobados()
elif opcion == 3:
    valor = mejor_promedio()
    print(f"El alumno con mejor promedio tiene el índice de {valor[1]} y un promedio de {valor[0]}")
else:
    valor = buscar_nota()
    print (f"Las índices de la nota buscada son {valor}")