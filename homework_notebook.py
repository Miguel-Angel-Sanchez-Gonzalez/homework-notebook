salir = False
cuaderno = []
print("Bienvenido a la libreta de tareas.\n")
while salir == False :
    print("Listado de opciones del cuaderno.")
    print("Opcion 1 - Agregar una tarea")
    print("Opcion 2 - Ver todas las tareas")
    print("Opcion 3 - Marcar una tarea como completada")
    print("Opcion 4 - Eliminar una tarea")
    print("Opcion 5 - Salir del programa")
    opcion = int(input("\nSeleccione una numero del 1 al 5: "))
    if opcion == 1 :
        print("\nSeleccionaste la opcion 1: Agregar una tarea")
        tarea = input("Ingresa el contenido de la tarea: ")
        cuaderno.append(tarea)
        print("Tarea agregada con exito! \n")  
    elif opcion == 2 :
        print("Seleccionaste la opcion 2: Ver todas las tareas")
    elif opcion == 3 :
        print("Seleccionaste la opcion 3: Marcar una tarea como completada")
    elif opcion == 4 :
        print("Seleccionaste la opcion 4: Eliminar una tarea")
    elif opcion == 5 :
        print("\nAdios, vuelva pronto!")
        salir = True
    
