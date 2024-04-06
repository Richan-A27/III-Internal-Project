import mysql.connector

#MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqldatabase"
)

#Create a cursor
cursor = db.cursor()

#Create students_db database
cursor.execute("CREATE DATABASE IF NOT EXISTS students_db")
cursor.execute("USE students_db")

# Create a table for students
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
)
""")
# Create a table for attendance
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    time TIME,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
)
""")

#commit the changes and close the database connection
db.commit()
db.close()

