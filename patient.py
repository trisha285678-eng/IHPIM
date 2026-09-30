from storage import load_data, save_data
from utils import get_non_empty, get_int


class Patient:
    def __init__(self, patient_id, name, age, gender, phone, address):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address

    def to_dict(self):
        return self.__dict__


class PatientManager:
    FILE = "data/patients.json"

    def __init__(self):
        self.patients = load_data(self.FILE)

    def _save(self):
        save_data(self.FILE, self.patients)

    def add_patient(self):
        patient_id = get_non_empty("Patient ID: ")
        if any(p["patient_id"] == patient_id for p in self.patients):
            print("Patient ID already exists.")
            return

        name = get_non_empty("Name: ")
        age = get_int("Age: ", 0, 120)
        gender = get_non_empty("Gender: ")
        phone = get_non_empty("Phone: ")
        address = get_non_empty("Address: ")

        patient = Patient(patient_id, name, age, gender, phone, address)
        self.patients.append(patient.to_dict())
        self._save()
        print("Patient registered successfully.")

    def list_patients(self):
        if not self.patients:
            print("No patient records found.")
            return
        for p in self.patients:
            print(f'{p["patient_id"]} | {p["name"]} | Age: {p["age"]} | {p["gender"]} | {p["phone"]}')

    def search_patient(self):
        key = get_non_empty("Enter Patient ID or name: ").lower()
        matches = [p for p in self.patients
                   if key in p["patient_id"].lower() or key in p["name"].lower()]
        if not matches:
            print("No matching patient found.")
            return
        for p in matches:
            print(p)

    def update_patient(self):
        patient_id = get_non_empty("Enter Patient ID to update: ")
        for p in self.patients:
            if p["patient_id"] == patient_id:
                print("Leave a field blank to keep the current value.")
                name = input(f'Name [{p["name"]}]: ').strip()
                phone = input(f'Phone [{p["phone"]}]: ').strip()
                address = input(f'Address [{p["address"]}]: ').strip()
                if name:
                    p["name"] = name
                if phone:
                    p["phone"] = phone
                if address:
                    p["address"] = address
                self._save()
                print("Patient updated successfully.")
                return
        print("Patient not found.")
