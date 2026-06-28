import mysql.connector

def connect_db():
    return mysql.connector.connect
(
        host="localhost",
        user="root",
        password="your_password",
        database="student_db"
    )

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            course VARCHAR(100)
        )
    """)
    conn.commit()
    conn.close()
