import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysqldatabase'
)
cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS students_db")
conn.commit()

# Switch to the database
cursor.execute("USE students_db")

# Create students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id CHAR(20) PRIMARY KEY,
        student_name VARCHAR(255) NOT NULL,
        student_email VARCHAR(255) NOT NULL,
        uid CHAR(20) NOT NULL
    )
""")

# Create attendance table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id CHAR(20),
        session_date DATE NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    )
""")

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()
