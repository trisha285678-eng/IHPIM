from datetime import datetime
from storage import load_data, save_data
from utils import get_non_empty


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time, reason):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.reason = reason
        self.status = "Booked"

    def to_dict(self):
        return self.__dict__


class AppointmentManager:
    FILE = "data/appointments.json"
    PATIENT_FILE = "data/patients.json"
    DOCTOR_FILE = "data/doctors.json"

    def __init__(self):
        self.appointments = load_data(self.FILE)

    def _save(self):
        save_data(self.FILE, self.appointments)

    def _exists(self, file_name, key, value):
        return any(item[key] == value for item in load_data(file_name))

    def book_appointment(self):
        appointment_id = get_non_empty("Appointment ID: ")
        if any(a["appointment_id"] == appointment_id for a in self.appointments):
            print("Appointment ID already exists.")
            return

        patient_id = get_non_empty("Patient ID: ")
        doctor_id = get_non_empty("Doctor ID: ")

        if not self._exists(self.PATIENT_FILE, "patient_id", patient_id):
            print("Patient does not exist. Register the patient first.")
            return
        if not self._exists(self.DOCTOR_FILE, "doctor_id", doctor_id):
            print("Doctor does not exist. Add the doctor first.")
            return

        date = get_non_empty("Date (DD-MM-YYYY): ")
        time = get_non_empty("Time (HH:MM): ")
        reason = get_non_empty("Reason for visit: ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            datetime.strptime(time, "%H:%M")
        except ValueError:
            print("Invalid date/time format.")
            return

        appointment = Appointment(
            appointment_id, patient_id, doctor_id, date, time, reason
        )
        self.appointments.append(appointment.to_dict())
        self._save()
        print("Appointment booked successfully.")

    def list_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return
        for a in self.appointments:
            print(
                f'{a["appointment_id"]} | Patient: {a["patient_id"]} | '
                f'Doctor: {a["doctor_id"]} | {a["date"]} {a["time"]} | '
                f'{a["status"]}'
            )

    def cancel_appointment(self):
        appointment_id = get_non_empty("Appointment ID to cancel: ")
        for a in self.appointments:
            if a["appointment_id"] == appointment_id:
                if a["status"] == "Cancelled":
                    print("Appointment is already cancelled.")
                else:
                    a["status"] = "Cancelled"
                    self._save()
                    print("Appointment cancelled.")
                return
        print("Appointment not found.")
