# Agenda Veterinaria – Sistema de Reservas

Sistema de consola desarrollado en Python para la gestión de pacientes y reservas de horas en una veterinaria.  
El proyecto utiliza una **arquitectura modular**, permitiendo escalabilidad y mantenimiento sencillo.

---

## 📌 Funcionalidades principales

- Registro de pacientes (mascotas)
- Validación para evitar pacientes duplicados
- Agenda de horas con:
  - Horario configurable (09:00 a 14:00)
  - Intervalos de 30 minutos
  - Restricción a días hábiles (lunes a viernes)
- Agendamiento de citas
- Consulta de agenda por fecha
- Cancelación de citas
- Listado y búsqueda de pacientes

---

## 🗂️ Estructura del proyecto

veterinaria_reservas/
│
├── main.py
├── README.md
│
└── modules/
├── menu.py
├── patients.py
├── reservations.py
├── data_input.py


### 📄 Descripción de módulos

- **main.py**  
  Punto de entrada del sistema. Inicializa datos y ejecuta el menú principal.

- **menu.py**  
  Controla la navegación del usuario y conecta las distintas funcionalidades.

- **patients.py**  
  Gestión de pacientes:
  - Registro
  - Búsqueda
  - Listado
  - Validación de duplicados

- **reservations.py**  
  Gestión de citas:
  - Generación de horarios
  - Validación de fechas hábiles
  - Agendamiento
  - Consulta de agenda
  - Cancelación de citas

- **data_input.py**  
  Manejo de entrada de datos del usuario (inputs validados).

---

## 🧠 Decisiones de diseño

- **Arquitectura modular**:  
  Cada responsabilidad está separada en su propio módulo, facilitando mantenimiento y escalabilidad.

- **Uso de listas y diccionarios**:  
  Los datos se almacenan en memoria, permitiendo un CRUD completo sin dependencias externas.

- **Formato de fecha estándar**:  
  Se utiliza `DD-MM-YYYY` para facilitar la comprensión del usuario.

- **Validaciones integradas**:  
  Se validan fechas, horarios disponibles y duplicidad de pacientes.

---

## ⚠️ Limitaciones actuales

- Los datos no se persisten (no se guardan en archivos ni base de datos).
- La cancelación de citas se realiza mediante **ID de citas**, lo que puede no ser intuitivo para el usuario.
- No se manejan feriados ni horarios especiales.
- No existe autenticación de usuarios.

---

## 🔧 Mejoras y escalabilidad futura

- 🔄 **Cancelar citas por Patient ID**  
  En futuras versiones, la cancelación de citas debería permitir:
  - Ingresar el `ID de paciente`
  - Mostrar todas las citas asociadas
  - Permitir seleccionar cuál cancelar

- 💾 Persistencia de datos  
  Guardar pacientes y citas en archivos (`.json`, `.csv`) o base de datos.

- 📅 Gestión avanzada de agenda  
  - Manejo de feriados
  - Horarios personalizados por día

- 🖥️ Interfaz gráfica o web  
  Migrar el sistema a una interfaz gráfica o aplicación web.

---

## ▶️ Ejecución del programa

Desde la carpeta raíz del proyecto:

```bash
python main.py
