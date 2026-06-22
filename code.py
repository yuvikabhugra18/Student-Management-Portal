import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    class_name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")
conn.commit()

def add_student():
    name = input("Student Name: ")
    class_name = input("Class: ")
    marks = int(input("Marks: "))

    cursor.execute(
        "INSERT INTO students(name, class_name, marks) VALUES (?, ?, ?)",
        (name, class_name, marks)
    )
    conn.commit()
    print("Student Added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for s in students:
        print(s)

def update_marks():
    student_id = int(input("Student ID: "))
    new_marks = int(input("New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (new_marks, student_id)
    )
    conn.commit()
    print("Marks Updated!")

def delete_student():
    student_id = int(input("Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )
    conn.commit()
    print("Student Deleted!")

def search_student():
    name = input("Enter Student Name: ")

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    results = cursor.fetchall()

    for r in results:
        print(r)

def top_performer():
    cursor.execute(
        "SELECT * FROM students ORDER BY marks DESC LIMIT 1"
    )

    student = cursor.fetchone()

    if student:
        print("\nTop Performer:")
        print(student)

while True:
    print("\n===== Student Management Portal =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Top Performer")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        top_performer()
    elif choice == "7":
        break
    else:
        print("Invalid Choice")

conn.close()
