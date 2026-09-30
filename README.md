# Integrated Hospital Patient Information Management System

## 1. Project Overview
The **Integrated Hospital Patient Information Management System** is a beginner-friendly Python console application designed for a first-year B.Tech student.

The project demonstrates how Python programming concepts can be used to manage basic hospital information in one system. It stores patient, doctor, appointment, medical record and billing information using JSON files.

This is an academic demonstration project. It is **not intended for real hospital use** and does not implement production-level medical-data security.

## 2. Main Features
- Patient registration, viewing, searching and updating
- Doctor registration and searching
- Appointment booking, viewing and cancellation
- Medical record entry and patient-wise viewing
- Basic bill creation and bill viewing
- Input validation and simple error handling
- Persistent local storage using JSON files
- Modular Python files
- Basic unit tests

## 3. Technologies Used
- Python 3
- JSON file storage
- Object-Oriented Programming
- Functions and modules
- Lists and dictionaries
- Conditional statements and loops
- Exception handling
- unittest
- Git/GitHub

## 4. Project Structure
```text
integrated_hospital_patient_information_management_system/
│
├── main.py
├── patient.py
├── doctor.py
├── appointment.py
├── records.py
├── billing.py
├── storage.py
├── utils.py
├── test_system.py
├── requirements.txt
├── statement.md
├── README.md
└── data/
    ├── patients.json
    ├── doctors.json
    ├── appointments.json
    ├── records.json
    └── bills.json
```

## 5. How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:
```bash
python main.py
```

## 6. How to Test
Run:
```bash
python -m unittest test_system.py
```

## 7. Example Workflow
1. Register a patient.
2. Add a doctor.
3. Book an appointment using the existing patient and doctor IDs.
4. Add a medical record.
5. Create a bill.
6. View stored information.

## 8. Important Note
The sample system is intended only for academic learning. Do not enter real patient information into this project.
