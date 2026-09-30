import json
from pathlib import Path

DATA_DIR = Path("data")


def ensure_data_files():
    DATA_DIR.mkdir(exist_ok=True)
    for name in ["patients.json", "doctors.json", "appointments.json", "records.json", "bills.json"]:
        path = DATA_DIR / name
        if not path.exists():
            path.write_text("[]", encoding="utf-8")


def load_data(file_name):
    path = Path(file_name)
    if not path.exists():
        path.parent.mkdir(exist_ok=True)
        path.write_text("[]", encoding="utf-8")
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(file_name, data):
    path = Path(file_name)
    path.parent.mkdir(exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
