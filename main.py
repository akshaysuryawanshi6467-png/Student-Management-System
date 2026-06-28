from database import connect_db, create_table

create_table()

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
        (name, age, course)
    )
    conn.commit()
    conn.close()
    print("Student added successfully!")

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        print(student)

    conn.close()

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
