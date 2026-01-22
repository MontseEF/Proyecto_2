from modules.patients import (
    register_patient_flow,
    list_patients,
    find_patient_by_id,
    find_patient_by_phone_name_and_species,
)

from modules.reservations import (
    consult_agenda,
    book_appointment_flow,
    cancel_appointment_flow,
)


# Menú principal
def show_menu():
    print("\n=== Menú Principal ===")
    print("BIENVENIDOS A SU VETERINARIA DE CONFIANZA")
    print("1. Agregar nuevo paciente")
    print("2. Consultar agenda (por fecha)")
    print("3. Agendar cita")
    print("4. Cancelar cita")
    print("5. Listado pacientes")
    print("6. Buscar paciente")
    print("7. Salir")
    choice = input("Seleccione una opción (1-7): ").strip()
    return choice


def run_menu(patients, next_patient_id, appointments, next_appointment_id):
    while True:
        choice = show_menu()

        # 1) Agregar nuevo paciente (y opcionalmente agendar)
        if choice == "1":
            patient_id, next_patient_id, was_created = register_patient_flow(
                patients, next_patient_id
            )

            if was_created:
                print(f"Paciente registrado con ID: {patient_id}")
            else:
                print(f"El paciente ya existe con ID: {patient_id}")

            # Preguntar si quiere agendar ahora (aunque ya exista, igual puede agendar)
            book_now = input("¿Desea agendar una cita ahora? (s/n): ").strip().lower()
            if book_now == "s":

                # Reutilizamos la lógica de opción 3 (agendar)
                patient = find_patient_by_id(patients, patient_id)
                if patient is None:
                    print("Error: no se encontró el paciente recién creado.")
                else:
                    _, next_appointment_id = book_appointment_flow(
                        appointments, patients, next_appointment_id, patient_id
                    )

        # 2) Consultar agenda
        elif choice == "2":
            consult_agenda(appointments)

        # 3) Agendar cita (por Patient ID)
        elif choice == "3":
            raw = input("Ingrese ID de paciente: ").strip()
            if not raw.isdigit():
                print("ID de paciente inválido.")
                continue

            patient_id = int(raw)
            patient = find_patient_by_id(patients, patient_id)

            if patient is None:
                print("No existe ese ID. Registre primero el paciente (opción 1).")
                continue

            _, next_appointment_id = book_appointment_flow(
                appointments, patients, next_appointment_id, patient_id
            )

        # 4) Cancelar cita (por Appointment ID) y opcional reagendar

        elif choice == "4":
            canceled = cancel_appointment_flow(appointments)

            if canceled:
                rebook = input("¿Desea reagendar esta cita? (s/n): ").strip().lower()
                if rebook == "s":
                    _, next_appointment_id = book_appointment_flow(
                        appointments,
                        patients,
                        next_appointment_id,
                        canceled["patient_id"],
                    )

        # 5) Listado pacientes

        elif choice == "5":
            list_patients(patients)

        # 6) Buscar paciente por teléfono + nombre + especie

        elif choice == "6":
            phone = input("Teléfono del tutor: ").strip()
            patient_name = input("Nombre del paciente: ").strip()
            species = input("Especie: ").strip()

            found = find_patient_by_phone_name_and_species(
                patients, phone, patient_name, species
            )

            if found:
                print(
                    f"Encontrado: ID {found['patient_id']} | "
                    f"{found['patient_name']} ({found['species']}) | "
                    f"Tutor: {found['owner_name']} | Tel: {found['owner_phone']} | Edad: {found['age']}"
                )
            else:
                print("No se encontró paciente con esos datos.")

        # 7) Salir (devolver contadores)

        elif choice == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            return next_patient_id, next_appointment_id

        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 7.")
