# Recolección de datos del paciente
def collect_patient_data():
    owner_name = input("Nombre del tutor: ").strip()
    owner_phone = input("Teléfono: ").strip()
    patient_name = input("Nombre del paciente: ").strip()
    species = input("Especie: ").strip()

    while True:
        age_input = input("Edad: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Por favor ingrese un número válido para la edad.")

    return {
        "owner_name": owner_name,
        "owner_phone": owner_phone,
        "patient_name": patient_name,
        "species": species,
        "age": age,
    }
