# Report-Card-Manager-

🎓 Student Report Card Manager

A console-based grade management system built in Python using Object-Oriented Programming (OOP) principles.
This tool helps manage student records, store subject-wise marks, calculate averages & grades, and persist data in a JSON file.

🚀 Features

Add Student – create a new student with subject scores

Update Scores – add or update subject marks for a student

View Report – display subject scores, average, and grade (A/B/C/Fail)

Delete Student – remove a student record by ID

Save & Load Data – store data in grades.json for persistence

🛠️ Technologies Used

Python 3

JSON for data storage

Object-Oriented Programming (OOP)

📂 Project Structure
ReportCardManager/
│── student_report_card.py   # Main program
│── grades.json              # Student data file (auto-created if missing)
│── README.md                # Project description

▶️ How to Run

Clone this repository:

git clone https://github.com/your-username/ReportCardManager.git
cd ReportCardManager


Run the program:

python student_report_card.py


Follow the menu options in the console.

📝 Example Usage
===== Student Report Card Manager =====
1. Add Student
2. Update Scores
3. View Report
4. Delete Student
5. Save Data
6. Exit
Enter choice: 1
Enter student name: Alice
Enter subject (or 'done' to finish): Math
Enter score for Math: 95
Enter subject (or 'done' to finish): Science
Enter score for Science: 88
Enter subject (or 'done' to finish): done
✅ Student 'Alice' added with ID 1

📌 Evaluation Points

Proper class structure (Student, GradeManager)

Encapsulation of student data and grading logic

Input validation & error handling

JSON file I/O for persistence

Clean report formatting

📜 License

This project is licensed under the MIT License.
