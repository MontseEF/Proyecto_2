from modules.patients import register_patient_flow

#creación de menú

def show_menu():
    print("=== Menú Principal ===")
    print(" BIENVENIDOS A LA AGENDA VETERINARIA")
    print("1. Agregar nuevo paciente")
    print("2. Consultar agenda")
    print("3. Agendar cita")
    print("4. Cancelar cita")
    print("5. Listado pacientes")
    print("6. Buscar paciente")
    print("7. Salir")
    choice = input("Seleccione una opción (1-7): ")
    return choice


def run_menu(patients, next_patient_id):
    while True:
        choice = show_menu()

        if choice == '1':
            patient_id, next_patient_id, was_created = register_patient_flow(patients, next_patient_id)
            if was_created:
                print(f"Paciente registrado con ID: {patient_id}")
            else:
                print(f"El paciente ya existe con ID: {patient_id}")

        elif choice == '2':
            print("Funcionalidad de consultar agenda no implementada aún.")

        elif choice == '3':
            print("Funcionalidad de agendar cita no implementada aún.")

        elif choice == '4':
            print("Funcionalidad de cancelar cita no implementada aún.")

        elif choice == '5':
            print("Funcionalidad de listado de pacientes no implementada aún.")

        elif choice == '6':
            print("Funcionalidad de buscar paciente no implementada aún.")

        elif choice == '7':
            print("Saliendo del programa. ¡Hasta luego!")
            return next_patient_id

        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 7.")
    
