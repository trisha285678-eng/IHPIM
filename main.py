from patient import PatientManager
from doctor import DoctorManager
from appointment import AppointmentManager
from records import RecordManager
from billing import BillingManager
from storage import ensure_data_files
from utils import print_header, get_int, pause


def patient_menu(manager):
    while True:
        print_header("PATIENT MANAGEMENT")
        print("1. Register patient")
        print("2. View all patients")
        print("3. Search patient")
        print("4. Update patient")
        print("5. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            manager.add_patient()
        elif choice == "2":
            manager.list_patients()
        elif choice == "3":
            manager.search_patient()
        elif choice == "4":
            manager.update_patient()
        elif choice == "5":
            return
        else:
            print("Invalid choice.")
        pause()


def doctor_menu(manager):
    while True:
        print_header("DOCTOR MANAGEMENT")
        print("1. Add doctor")
        print("2. View all doctors")
        print("3. Search doctor")
        print("4. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            manager.add_doctor()
        elif choice == "2":
            manager.list_doctors()
        elif choice == "3":
            manager.search_doctor()
        elif choice == "4":
            return
        else:
            print("Invalid choice.")
        pause()


def appointment_menu(manager):
    while True:
        print_header("APPOINTMENT MANAGEMENT")
        print("1. Book appointment")
        print("2. View appointments")
        print("3. Cancel appointment")
        print("4. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            manager.book_appointment()
        elif choice == "2":
            manager.list_appointments()
        elif choice == "3":
            manager.cancel_appointment()
        elif choice == "4":
            return
        else:
            print("Invalid choice.")
        pause()


def record_menu(manager):
    while True:
        print_header("MEDICAL RECORD MANAGEMENT")
        print("1. Add medical record")
        print("2. View patient records")
        print("3. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            manager.add_record()
        elif choice == "2":
            manager.view_records()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")
        pause()


def billing_menu(manager):
    while True:
        print_header("BILLING MANAGEMENT")
        print("1. Create bill")
        print("2. View bills")
        print("3. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            manager.create_bill()
        elif choice == "2":
            manager.list_bills()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")
        pause()


def main():
    ensure_data_files()

    patient_manager = PatientManager()
    doctor_manager = DoctorManager()
    appointment_manager = AppointmentManager()
    record_manager = RecordManager()
    billing_manager = BillingManager()

    while True:
        print_header("INTEGRATED HOSPITAL PATIENT INFORMATION MANAGEMENT SYSTEM")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Medical Records")
        print("5. Billing")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            patient_menu(patient_manager)
        elif choice == "2":
            doctor_menu(doctor_manager)
        elif choice == "3":
            appointment_menu(appointment_manager)
        elif choice == "4":
            record_menu(record_manager)
        elif choice == "5":
            billing_menu(billing_manager)
        elif choice == "6":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
