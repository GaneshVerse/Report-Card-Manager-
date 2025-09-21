import json

# ---------------- Student Class ---------------- #
class Student:
    id_counter = 1  # Auto-generate unique IDs

    def __init__(self, name):
        self.id = Student.id_counter
        Student.id_counter += 1
        self.name = name
        self.subjects = {}  # {subject: score}

    def add_subject(self, subject, score):
        """Add or update a subject score."""
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100.")
        self.subjects[subject] = score

    def calculate_average(self):
        """Calculate average score across all subjects."""
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def get_grade(self):
        """Assign grade based on average score."""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    def to_dict(self):
        """Convert student object to dictionary for JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "subjects": self.subjects
        }

    @classmethod
    def from_dict(cls, data):
        """Recreate a student object from dictionary."""
        student = cls(data["name"])
        student.id = data["id"]
        student.subjects = data["subjects"]
        if student.id >= Student.id_counter:
            Student.id_counter = student.id + 1
        return student


# ---------------- GradeManager Class ---------------- #
class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, subjects):
        student = Student(name)
        for subject, score in subjects.items():
            student.add_subject(subject, score)
        self.students.append(student)
        print(f"✅ Student '{name}' added with ID {student.id}")

    def update_scores(self, student_id, subject, score):
        for student in self.students:
            if student.id == student_id:
                student.add_subject(subject, score)
                print(f"✅ Updated {student.name}'s {subject} score to {score}")
                return
        print("❌ Student not found.")

    def view_report(self, student_id):
        for student in self.students:
            if student.id == student_id:
                print(f"\n📘 Report for {student.name} (ID: {student.id})")
                print("-" * 40)
                for subject, score in student.subjects.items():
                    print(f"{subject}: {score}")
                avg = student.calculate_average()
                print(f"\nAverage: {avg:.2f}")
                print(f"Grade: {student.get_grade()}")
                print("-" * 40)
                return
        print("❌ Student not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print(f"🗑️ Deleted student {student.name} (ID: {student_id})")
                return
        print("❌ Student not found.")

    def save_to_file(self, filename="grades.json"):
        data = [student.to_dict() for student in self.students]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"💾 Data saved to {filename}")

    def load_from_file(self, filename="grades.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.students = [Student.from_dict(d) for d in data]
            print(f"📂 Loaded data from {filename}")
        except FileNotFoundError:
            print("⚠️ No saved data found.")


# ---------------- Console Menu ---------------- #
def main():
    manager = GradeManager()
    manager.load_from_file()

    while True:
        print("\n===== Student Report Card Manager =====")
        print("1. Add Student")
        print("2. Update Scores")
        print("3. View Report")
        print("4. Delete Student")
        print("5. Save Data")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            subjects = {}
            while True:
                sub = input("Enter subject (or 'done' to finish): ")
                if sub.lower() == "done":
                    break
                try:
                    score = int(input(f"Enter score for {sub}: "))
                    subjects[sub] = score
                except ValueError:
                    print("❌ Invalid score. Enter a number between 0–100.")
            manager.add_student(name, subjects)

        elif choice == "2":
            try:
                sid = int(input("Enter student ID: "))
                sub = input("Enter subject: ")
                score = int(input(f"Enter new score for {sub}: "))
                manager.update_scores(sid, sub, score)
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "3":
            try:
                sid = int(input("Enter student ID: "))
                manager.view_report(sid)
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "4":
            try:
                sid = int(input("Enter student ID to delete: "))
                manager.delete_student(sid)
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "5":
            manager.save_to_file()

        elif choice == "6":
            manager.save_to_file()
            print("👋 Exiting... Data saved.")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
