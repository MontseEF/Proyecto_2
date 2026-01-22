from datetime import datetime


# Valida la fecha y hora para agendar citas
def is_weekday(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.weekday() < 5  # 0 = lunes, 4 = viernes
    except ValueError:
        return False


# Genera franja horaria de 09:00 a 14:00 en intervalos de 30 minutos
def generate_time_slots():

    slots = []
    hour = 9
    minute = 0

    while True:
        slots.append(f"{hour:02d}:{minute:02d}")
        minute += 30

        if minute >= 60:
            minute = 0
            hour += 1

        if hour == 14 and minute == 0:
            break

    return slots


def get_booked_times_for_date(appointments, date_str):
    return sorted([a["time"] for a in appointments if a["date"] == date_str])


def get_available_times_for_date(appointments, date_str):
    all_slots = generate_time_slots()
    booked = set(get_booked_times_for_date(appointments, date_str))
    return [t for t in all_slots if t not in booked]


def show_agenda_for_date(appointments, date_str):
    day = [a for a in appointments if a["date"] == date_str]

    if not day:
        print(f"No hay citas para {date_str}.")
        return

    print("\n" + "-" * 40)
    print(f"AGENDA DEL DÍA {date_str}")
    print("-" * 40)

    for a in sorted(day, key=lambda x: x["time"]):
        print(
            f"{a['time']} | ID de cita: {a['appointment_id']} | "
            f"ID de paciente: {a['patient_id']} | Motivo: {a['reason']}"
        )

    print("-" * 40)


def consult_agenda(appointments):
    date_str = input("Ingrese fecha (DD-MM-YYYY): ").strip()

    if not is_weekday(date_str):
        print("Fecha inválida o no es día hábil (lunes a viernes).")
        return

    show_agenda_for_date(appointments, date_str)

    available = get_available_times_for_date(appointments, date_str)
    print(f"Disponibilidad: {len(available)} horarios libres.")
    if available:
        print("Horas disponibles:", ", ".join(available))


def book_appointment_flow(appointments, patients, next_appointment_id, patient_id):
    date_str = input("Ingrese fecha (DD-MM-YYYY): ").strip()

    if not is_weekday(date_str):
        print("Fecha inválida o no es día hábil (lunes a viernes).")
        return None, next_appointment_id

    available = get_available_times_for_date(appointments, date_str)
    if not available:
        print("No hay disponibilidad para esa fecha.")
        return None, next_appointment_id

    print("Horas disponibles:", ", ".join(available))

    time_str = input("Ingrese hora (HH:MM): ").strip()
    if time_str not in available:
        print("Hora inválida o no disponible.")
        return None, next_appointment_id

    reason = input("Motivo de la cita: ").strip()

    new_appointment = {
        "appointment_id": next_appointment_id,
        "patient_id": patient_id,
        "date": date_str,
        "time": time_str,
        "reason": reason,
    }

    appointments.append(new_appointment)
    next_appointment_id += 1

    print(f"Cita agendada. ID de cita: {new_appointment['appointment_id']}")
    return new_appointment, next_appointment_id


def cancel_appointment_flow(appointments):
    if not appointments:
        print("No hay citas registradas.")
        return None

    raw = input("Ingrese ID de cita a cancelar: ").strip()
    if not raw.isdigit():
        print("ID de cita inválido.")
        return None

    app_id = int(raw)

    for i, a in enumerate(appointments):
        if a["appointment_id"] == app_id:
            confirm = (
                input(
                    f"¿Seguro que desea cancelar la cita {app_id} "
                    f"del {a['date']} a las {a['time']}? (s/n): "
                )
                .strip()
                .lower()
            )

            if confirm == "s":
                appointments.pop(i)
                print("Cita cancelada.")
                return a
            else:
                print("Cancelación abortada.")
                return None

    print("No se encontró una cita con ese ID de cita.")
    return None
