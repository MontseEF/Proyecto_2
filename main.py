from modules.menu import run_menu


# Entry point del programa
def main():
    patients = []
    next_patient_id = 1

    appointments = []
    next_appointment_id = 1

    next_patient_id, next_appointment_id = run_menu(
        patients, next_patient_id, appointments, next_appointment_id
    )


if __name__ == "__main__":
    main()
