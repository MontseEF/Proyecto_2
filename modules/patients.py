from modules.data_input import collect_patient_data

#Buscar si el paciente ya existe

def find_patient_by_phone_name_and_species(patients, owner_phone, patient_name, species):
    for patient in patients:
        if (patient['owner_phone'].strip() == owner_phone.strip() and 
            patient['patient_name'].strip().lower() == patient_name.strip().lower() and
            patient['species'].strip().lower() == species.strip().lower()):
            return patient
    return None

#Agregar nuevo paciente
def create_patient(patients, patient_data, patient_id):
    new_patient = {
        'patient_id': patient_id,
        'owner_name': patient_data['owner_name'],
        'owner_phone': patient_data['owner_phone'],
        'patient_name': patient_data['patient_name'],
        'species': patient_data['species'],
        'age': patient_data['age']
    }

    patients.append(new_patient)
    return new_patient

#Registro pacientes
def register_patient_flow(patients, next_patient_id):
    """
    Opción 1:
    - Datos del paciente
    - Revisar si existe (teléfono + nombre + especie)
    - Si existe: retornar ID existente
    - Si no: crear y aumentar next_patient_id
    Devuelve : (patient_id, next_patient_id, was_created)
    """
    patient_data = collect_patient_data()

    existing = find_patient_by_phone_name_and_species(
        patients,
        patient_data['owner_phone'],
        patient_data['patient_name'],
        patient_data['species']
    )

    if existing is not None:
        return existing['patient_id'], next_patient_id, False

    created = create_patient(patients, patient_data, next_patient_id)
    next_patient_id += 1
    return created['patient_id'], next_patient_id, True

