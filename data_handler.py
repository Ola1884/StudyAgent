import json
import os

DATA_FILE = "student_data.json"

def load_data():
    """Load data from JSON file with backward compatibility"""
    if not os.path.exists(DATA_FILE):
        return {"courses": [], "exams": []}
    try:
        with open(DATA_FILE, "r", encoding='utf-8') as f:
            data = json.load(f)
            # Backward compatibility for old keys
            if "Tasks" in data:
                data["courses"] = data.pop("Tasks")
            if "Exams" in data:
                data["exams"] = data.pop("Exams")
            # Ensure keys exist
            if "courses" not in data:
                data["courses"] = []
            if "exams" not in data:
                data["exams"] = []
            return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return {"courses": [], "exams": []}

def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)