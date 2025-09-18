# students will be stored like this:
# [{"name": "Bashir", "Score": 85, "grade": "A"}]

students = []

#  file name for saving records
FILE_NAME = "grades.txt"

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter student    name: ").strip()

    score = get_valid_score()
    grade = calculate_grade(score)
    student = {"name": name, "score": score, "grade": grade}
    students.append(student)
    print(f"{name} added successfully")

def view_all():
    if not students:
        print("No students found.")
    else:
        for s in students:
            print(f"Name: {s['name']} | Score: {s['score']} | Grade: {s['grade']}")

def search_students():
    name = input("Enter name to search: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found name: {s['name']} Score: {s['score']} | Grade: {s['grade']}")
        return print("Student not found")

def save_to_file():
    with open(FILE_NAME, "w") as f:
        for s in students:
            f.write(f"{s['name']}, {s['score']}, {s['grade']}\n")

def load_from_file():
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, score, grade = line.strip().split(",")
                students.append({"name": name, "score": int(score), "grade": grade})
    except FileNotFoundError:
        pass

def main():
    load_from_file()

    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Add student")
        print("2. View All")
        print("3. Search Student")
        print("4. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_students()
        elif choice == "4":
            save_to_file()
            print("Data saved. Goodbye!")


def get_valid_score(prompt="Enter score (0-100): "):
    while True:
        raw = input(prompt).strip()
        try:
            score = int(raw)
        except ValueError:
            print("Invalid input. Please type a number, e.g. 75.")
            continue
        if 0 <= score <= 100:
            return score
        print("Score must be between 0 and 100.")

if __name__ == "__main__":
    main()