salir = False
cuaderno = []
control_tareas = []
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
        cuaderno.append(tarea)
        control_tareas.append(False)
        print("Tarea agregada con exito! \n")  
    elif opcion == 2 :
        print("\nSeleccionaste la opción 2: Ver todas las tareas")
        if not cuaderno:  
            print("Parece que el cuaderno está vacío, intenta agregar alguna tarea primero\n")
        else:
            for i, tarea in enumerate(cuaderno):  
                estado = "✅ Completada" if control_tareas[i] else "❌ Pendiente"
                print(f"{i + 1}. {tarea} - {estado}")  
    elif opcion == 3 :
        print("Seleccionaste la opcion 3: Marcar una tarea como completada")
        num_tarea = 1
        for mis_tareas in control_tareas :
            
            if mis_tareas == False :
                estado = "Sin completar"
            else :
                estado = "Completada"     
            print(f"Tarea {num_tarea} con estado {estado}")
            
            num_tarea += 1
        numero_tarea = int(input("Para cambiar el estado de una tarea a completado ingrese el numero de la tarea: "))
        try :
            control_tareas[(numero_tarea - 1)] = True
            print("Perfecto su tarea se cambio a completada\n")
        except IndexError :
            print("Parece que no tienes ese numero de tarea\n")
    elif opcion == 4 :
        print("Seleccionaste la opcion 4: Eliminar una tarea")
        eliminar_tarea = int(input("Seleccione el numero de la tarea que deseas eliminar: "))
        try :
            cuaderno.pop(eliminar_tarea - 1)
            print("La tarea se elimino correctamente!\n")
        except IndexError:
            print("Parece que no tienes ese numero de tarea\n")
    elif opcion == 5 :
        print("\nAdios, vuelva pronto!")
        salir = True
    else : 
        print("\nParece que no seleccionaste una opcion valida, por favor intentalo de nuevo.\n")    