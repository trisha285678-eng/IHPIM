from storage import load_data, save_data
from utils import get_float, get_non_empty


class Bill:
    def __init__(self, bill_id, patient_id, consultation, tests, medicines):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.consultation = consultation
        self.tests = tests
        self.medicines = medicines
        self.total = consultation + tests + medicines
        self.status = "Unpaid"

    def to_dict(self):
        return self.__dict__


class BillingManager:
    FILE = "data/bills.json"
    PATIENT_FILE = "data/patients.json"

    def __init__(self):
        self.bills = load_data(self.FILE)

    def _save(self):
        save_data(self.FILE, self.bills)

    def create_bill(self):
        bill_id = get_non_empty("Bill ID: ")
        if any(b["bill_id"] == bill_id for b in self.bills):
            print("Bill ID already exists.")
            return

        patient_id = get_non_empty("Patient ID: ")
        if not any(p["patient_id"] == patient_id for p in load_data(self.PATIENT_FILE)):
            print("Patient does not exist.")
            return

        consultation = get_float("Consultation charge: ", 0)
        tests = get_float("Test charges: ", 0)
        medicines = get_float("Medicine charges: ", 0)

        bill = Bill(bill_id, patient_id, consultation, tests, medicines)
        self.bills.append(bill.to_dict())
        self._save()
        print(f"Bill created. Total amount: ₹{bill.total:.2f}")

    def list_bills(self):
        if not self.bills:
            print("No bills found.")
            return
        for b in self.bills:
            print(
                f'{b["bill_id"]} | Patient: {b["patient_id"]} | '
                f'Total: ₹{b["total"]:.2f} | Status: {b["status"]}'
            )
