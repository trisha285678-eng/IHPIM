from storage import load_data, save_data
from utils import get_non_empty


class MedicalRecord:
    def __init__(self, record_id, patient_id, doctor_id, diagnosis, prescription, notes):
        self.record_id = record_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.prescription = prescription
        self.notes = notes

    def to_dict(self):
        return self.__dict__


class RecordManager:
    FILE = "data/records.json"
    PATIENT_FILE = "data/patients.json"

    def __init__(self):
        self.records = load_data(self.FILE)

    def _save(self):
        save_data(self.FILE, self.records)

    def add_record(self):
        record_id = get_non_empty("Record ID: ")
        if any(r["record_id"] == record_id for r in self.records):
            print("Record ID already exists.")
            return

        patient_id = get_non_empty("Patient ID: ")
        if not any(p["patient_id"] == patient_id for p in load_data(self.PATIENT_FILE)):
            print("Patient does not exist.")
            return

        doctor_id = get_non_empty("Doctor ID: ")
        diagnosis = get_non_empty("Diagnosis: ")
        prescription = get_non_empty("Prescription: ")
        notes = input("Additional notes (optional): ").strip()

        record = MedicalRecord(
            record_id, patient_id, doctor_id, diagnosis, prescription, notes
        )
        self.records.append(record.to_dict())
        self._save()
        print("Medical record added.")

    def view_records(self):
        patient_id = get_non_empty("Enter Patient ID: ")
        matches = [r for r in self.records if r["patient_id"] == patient_id]
        if not matches:
            print("No records found for this patient.")
            return
        for r in matches:
            print("-" * 50)
            print(f'Record ID: {r["record_id"]}')
            print(f'Doctor ID: {r["doctor_id"]}')
            print(f'Diagnosis: {r["diagnosis"]}')
            print(f'Prescription: {r["prescription"]}')
            print(f'Notes: {r["notes"]}')
