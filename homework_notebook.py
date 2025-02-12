salir = False
cuaderno = []
control_tareas = []
tareas = {}
print("Bienvenido a la libreta de tareas.\n")
while salir == False :
    print("\nListado de opciones del cuaderno.")
    print("Opcion 1 - Agregar una tarea")
    print("Opcion 2 - Ver todas las tareas")
    print("Opcion 3 - Marcar una tarea como completada")
    print("Opcion 4 - Eliminar una tarea")
    print("Opcion 5 - Salir del programa")
    try:
        opcion = int(input("\nSeleccione una opción del 1 al 5: "))
    except ValueError:
        print("\nDebes ingresar un número válido.\n")
        continue 
    if opcion == 1 :
        print("\nSeleccionaste la opcion 1: Agregar una tarea")
        tarea = input("Ingresa el contenido de la tarea: ")
        tareas[tarea] = False  # False indica que no está completada
        print("Tarea agregada con éxito!\n") 
    elif opcion == 2 :
        print("\nSeleccionaste la opción 2: Ver todas las tareas")
        if not tareas:  
            print("Parece que el cuaderno está vacío, intenta agregar alguna tarea primero\n")
        else:
            for i, (tarea, estado) in enumerate(tareas.items(), start=1):
                estado_texto = "✅ Completada" if estado else "❌ Sin completar"
                print(f"Tarea número {i}: {tarea} - Estado: {estado_texto}")
    elif opcion == 3 :
        tarea_completar = input("Ingresa la tarea que quieres marcar como completada: ")
        if tarea_completar in tareas:
            tareas[tarea_completar] = True
            print("Tarea marcada como completada.\n")
        else:
            print("No se encontró la tarea.\n")
    elif opcion == 4 :
        print("Seleccionaste la opcion 4: Eliminar una tarea")
        tarea_eliminar = input("Ingresa la tarea que quieres eliminar: ")
        if tarea_eliminar in tareas:
            del tareas[tarea_eliminar]
            print("Tarea eliminada con éxito.\n")
        else:
            print("No se encontró la tarea.\n")
    elif opcion == 5 :
        print("\nAdios, vuelva pronto!")
        salir = True
    else : 
        print("\nParece que no seleccionaste una opcion valida, por favor intentalo de nuevo.\n")    