import unittest
from billing import Bill
from patient import Patient
from doctor import Doctor
from appointment import Appointment


class TestSystemClasses(unittest.TestCase):

    def test_patient_creation(self):
        p = Patient("P001", "Asha", 20, "Female", "9999999999", "Bhopal")
        self.assertEqual(p.patient_id, "P001")
        self.assertEqual(p.age, 20)

    def test_doctor_creation(self):
        d = Doctor("D001", "Rahul", "General Medicine", "8888888888")
        self.assertEqual(d.department, "General Medicine")

    def test_appointment_status(self):
        a = Appointment("A001", "P001", "D001", "30-09-2026", "10:30", "Check-up")
        self.assertEqual(a.status, "Booked")

    def test_bill_total(self):
        b = Bill("B001", "P001", 500, 300, 200)
        self.assertEqual(b.total, 1000)


if __name__ == "__main__":
    unittest.main()
