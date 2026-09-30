from storage import load_data, save_data
from utils import get_non_empty


class Doctor:
    def __init__(self, doctor_id, name, department, phone):
        self.doctor_id = doctor_id
        self.name = name
        self.department = department
        self.phone = phone

    def to_dict(self):
        return self.__dict__


class DoctorManager:
    FILE = "data/doctors.json"

    def __init__(self):
        self.doctors = load_data(self.FILE)

    def _save(self):
        save_data(self.FILE, self.doctors)

    def add_doctor(self):
        doctor_id = get_non_empty("Doctor ID: ")
        if any(d["doctor_id"] == doctor_id for d in self.doctors):
            print("Doctor ID already exists.")
            return

        name = get_non_empty("Doctor name: ")
        department = get_non_empty("Department: ")
        phone = get_non_empty("Phone: ")

        doctor = Doctor(doctor_id, name, department, phone)
        self.doctors.append(doctor.to_dict())
        self._save()
        print("Doctor added successfully.")

    def list_doctors(self):
        if not self.doctors:
            print("No doctor records found.")
            return
        for d in self.doctors:
            print(f'{d["doctor_id"]} | Dr. {d["name"]} | {d["department"]} | {d["phone"]}')

    def search_doctor(self):
        key = get_non_empty("Enter Doctor ID or name: ").lower()
        matches = [d for d in self.doctors
                   if key in d["doctor_id"].lower() or key in d["name"].lower()]
        if not matches:
            print("No matching doctor found.")
            return
        for d in matches:
            print(d)
